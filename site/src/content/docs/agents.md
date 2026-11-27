---
title: Agents
description: Install the mdmsdk skill, or point an agent at llms.txt, so it writes a correct integration.
---

The repository is built for agents first. An agent that reads the skill or `llms.txt` can write an integration without reading the rest.

## Install the skill

```sh
npx skills add qbranchio/mdmsdk --skill mdmsdk -a claude-code
```

The skill covers the credential to choose, setup, the call pattern, errors, retries, and the rules that are easy to get wrong.

## Point an agent at the docs

| File | For | Holds |
|---|---|---|
| [llms.txt](https://qbranchio.github.io/mdmsdk/llms.txt) | Any agent | An index of these docs. |
| [llms-full.txt](https://qbranchio.github.io/mdmsdk/llms-full.txt) | Any agent | Every page of these docs in one file. |
| [openapi.yaml](https://qbranchio.github.io/mdmsdk/openapi.yaml) | Any agent | The published contract. |
| [skills/mdmsdk](https://github.com/qbranchio/mdmsdk/tree/main/skills/mdmsdk) | Agents integrating the SDK | The skill and its references. |
| [AGENTS.md](https://github.com/qbranchio/mdmsdk/blob/main/AGENTS.md) | Agents changing the SDK repository | Layout, commands, and rules. |

Without the skill, give the agent one line:

```text
Read https://qbranchio.github.io/mdmsdk/llms-full.txt before writing code that calls the mdm API.
```

## What an agent should know

- Branch on an error's `code`, never on its status or title, and quote `instance`.
- Do not add a retry loop. The SDK retries what is safe.
- A resource outside the caller's reach answers 404, not 403.
- Policy reaches devices only as declarations. A setting's status comes from the device, not from the write.
- Commands and tenant deletion are asynchronous: the answer is 202, and the result arrives later.
- A licence 409 is final until the licence changes.
- Only the operator registers API clients and browser origins.
