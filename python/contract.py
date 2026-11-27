"""Writes .contract.yaml: openapi/openapi.yaml prepared for openapi-python-client.

The generator drops a property typed `type: [null, array]` (a nullable array)
and cannot nest a component that is itself nullable. The same meanings written
with `anyOf: [..., {type: null}]` it handles, so those rewrites are applied
here. The published contract is unchanged.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent


def rewrite(node: Any) -> Any:
    if isinstance(node, dict):
        node = {k: rewrite(v) for k, v in node.items()}
        t = node.get("type")
        if isinstance(t, list) and "null" in t and "array" in t and len(t) == 2:
            desc = node.pop("description", None)
            node.pop("type")
            array = {"type": "array", **node}
            node = {"anyOf": [array, {"type": "null"}]}
            if desc is not None:
                node["description"] = desc
        return node
    if isinstance(node, list):
        return [rewrite(v) for v in node]
    return node


def nullable_components(doc: dict[str, Any]) -> None:
    """A component that is itself nullable (type [null, object]) becomes a plain
    object, and every reference to it becomes anyOf [$ref, null]."""
    schemas: dict[str, Any] = doc.get("components", {}).get("schemas", {})
    names = set()
    for name, schema in schemas.items():
        t = schema.get("type") if isinstance(schema, dict) else None
        if isinstance(t, list) and "null" in t:
            rest = [x for x in t if x != "null"]
            schema["type"] = rest[0] if len(rest) == 1 else rest
            names.add(name)

    def walk(node: Any) -> Any:
        if isinstance(node, dict):
            ref = node.get("$ref")
            if isinstance(ref, str) and ref.rsplit("/", 1)[-1] in names:
                extra = {k: v for k, v in node.items() if k != "$ref"}
                return {"anyOf": [{"$ref": ref}, {"type": "null"}], **extra}
            return {k: walk(v) for k, v in node.items()}
        if isinstance(node, list):
            return [walk(v) for v in node]
        return node

    doc["paths"] = walk(doc.get("paths", {}))
    doc.setdefault("components", {})["schemas"] = walk(schemas)


def main() -> None:
    doc = yaml.safe_load((ROOT.parent / "openapi" / "openapi.yaml").read_text())
    nullable_components(doc)
    (ROOT / ".contract.yaml").write_text(yaml.safe_dump(rewrite(doc), sort_keys=False))


if __name__ == "__main__":
    main()
