// The `mdm` command set and /tenants mount for the docs terminal, over the
// in-browser mock. Each command mirrors an SDK call; --show prints it.
import type { CommandDef, EggDef, Entry, MountProvider, Proc, RiteGlobal, Stat } from "./rite"
import { createMock, type Device, type Mock } from "./mock"

const TENANT = "demo"

type Show = "go" | "python" | "curl"
const SHOWS: Show[] = ["go", "python", "curl"]

const snippets: Record<string, Record<Show, (a: string[]) => string>> = {
  me: {
    go: () => "me, err := client.Me.Get(ctx)",
    python: () => "me = client.me.get()",
    curl: () => "curl -s https://enroll.dev/api/v1/me -H \"Authorization: Bearer $TOKEN\"",
  },
  "devices ls": {
    go: () => `for d, err := range client.Devices.List(ctx, "${TENANT}", nil) { ... }`,
    python: () => `for d in client.devices.list("${TENANT}"): ...`,
    curl: () => `curl -s https://enroll.dev/api/v1/tenants/${TENANT}/devices -H "Authorization: Bearer $TOKEN"`,
  },
  "devices show": {
    go: (a) => `device, err := client.Devices.Get(ctx, "${TENANT}", uuid.MustParse("${a[0] ?? "<id>"}"))`,
    python: (a) => `device = client.devices.get("${TENANT}", UUID("${a[0] ?? "<id>"}"))`,
    curl: (a) => `curl -s https://enroll.dev/api/v1/tenants/${TENANT}/devices/${a[0] ?? "<id>"} -H "Authorization: Bearer $TOKEN"`,
  },
  "profiles ls": {
    go: () => `for p, err := range client.Profiles.List(ctx, "${TENANT}") { ... }`,
    python: () => `for p in client.profiles.list("${TENANT}"): ...`,
    curl: () => `curl -s https://enroll.dev/api/v1/tenants/${TENANT}/profiles -H "Authorization: Bearer $TOKEN"`,
  },
  "profiles assign": {
    go: (a) => `a, err := client.Assignments.Create(ctx, "${TENANT}", uuid.MustParse("${a[0] ?? "<profile>"}"), api.AssignmentRequest{Target: "tenant", Levels: levels})`,
    python: (a) => `a = client.assignments.create("${TENANT}", UUID("${a[0] ?? "<profile>"}"), AssignmentRequest(target=AssignmentRequestTarget.TENANT, levels=levels))`,
    curl: (a) => `curl -s -X POST https://enroll.dev/api/v1/tenants/${TENANT}/profiles/${a[0] ?? "<profile>"}/assignments -H "Authorization: Bearer $TOKEN" -d '{"target":"tenant","levels":["supervised","unsupervised"]}'`,
  },
  "commands send": {
    go: (a) => `accepted, err := client.Commands.Send(ctx, "${TENANT}", uuid.MustParse("${a[0] ?? "<device>"}"), api.CommandRequest{Type: "${a[1] ?? "DeviceInformation"}"})`,
    python: (a) => `accepted = client.commands.send("${TENANT}", UUID("${a[0] ?? "<device>"}"), CommandRequest(type_=CommandRequestType("${a[1] ?? "DeviceInformation"}")))`,
    curl: (a) => `curl -s -X POST https://enroll.dev/api/v1/tenants/${TENANT}/devices/${a[0] ?? "<device>"}/commands -H "Authorization: Bearer $TOKEN" -d '{"type":"${a[1] ?? "DeviceInformation"}"}'`,
  },
  "commands ls": {
    go: (a) => `for c, err := range client.Commands.List(ctx, "${TENANT}", uuid.MustParse("${a[0] ?? "<device>"}")) { ... }`,
    python: (a) => `for c in client.commands.list("${TENANT}", UUID("${a[0] ?? "<device>"}")): ...`,
    curl: (a) => `curl -s https://enroll.dev/api/v1/tenants/${TENANT}/devices/${a[0] ?? "<device>"}/commands -H "Authorization: Bearer $TOKEN"`,
  },
}

const json = (v: unknown): string => JSON.stringify(v, null, 2) + "\n"
const short = (id: string): string => id.slice(0, 8)
const pad = (s: string, n: number): string => (s.length >= n ? s : s + " ".repeat(n - s.length))

function findDevice(mock: Mock, ref: string | undefined): Device | undefined {
  return ref ? mock.getDevice(ref) : undefined
}

const showFlag = { show: { long: "show", type: "string" as const, description: "print the SDK call instead: go, python, or curl" } }

/** Wraps a subcommand: --show prints the SDK call; otherwise run. */
function sub(key: string, summary: string, usage: string, run: (p: Proc) => Promise<number | void>): Omit<CommandDef, "name"> {
  return {
    summary, usage, flags: showFlag,
    run: async (p) => {
      const show = p.flags["show"]
      if (typeof show === "string") {
        if (!SHOWS.includes(show as Show)) {
          await p.err(`mdm: --show takes go, python, or curl\n`)
          return 2
        }
        await p.out(snippets[key]![show as Show]([...p.args]) + "\n")
        return 0
      }
      return run(p)
    },
  }
}

export function mdmCommand(mock: Mock): CommandDef {
  return {
    name: "mdm",
    summary: "the mdm API, against a demo tenant in your browser",
    usage: "mdm <me|devices|profiles|commands> ... [--show go|python|curl]",
    manual: "Each subcommand is one SDK call against a mock of the API that lives in this page. " +
      "Add --show go, --show python, or --show curl to print the call instead. The demo tenant is mounted at /tenants/demo.",
    subcommands: {
      me: sub("me", "who the caller is", "mdm me", async (p) => { await p.out(json(mock.me())) }),
      devices: {
        summary: "devices in the tenant", usage: "mdm devices <ls|show <id>>",
        subcommands: {
          ls: sub("devices ls", "list devices", "mdm devices ls", async (p) => {
            await p.out(pad("ID", 10) + pad("NAME", 18) + pad("MODEL", 16) + pad("iOS", 6) + "SUPERVISED\n")
            for (const d of mock.listDevices()) {
              await p.out(pad(short(d.id), 10) + pad(d.name, 18) + pad(d.model ?? "", 16) + pad(d.os_version ?? "", 6) + (d.supervised ? "yes" : "no") + "\n")
            }
          }),
          show: sub("devices show", "one device", "mdm devices show <id>", async (p) => {
            const d = findDevice(mock, p.args[0])
            if (!d) { await p.err(`mdm: ${p.args[0] ?? "<id>"}: no such device\n`); return 1 }
            await p.out(json(d))
            return 0
          }),
        },
      },
      profiles: {
        summary: "policy profiles", usage: "mdm profiles <ls|assign <profile>>",
        subcommands: {
          ls: sub("profiles ls", "list profiles", "mdm profiles ls", async (p) => {
            for (const pr of mock.listProfiles()) await p.out(`${short(pr.id)}  ${pr.name}\n`)
          }),
          assign: sub("profiles assign", "assign a profile to the whole tenant", "mdm profiles assign <profile>", async (p) => {
            const pr = p.args[0] ? mock.getProfile(p.args[0]) : undefined
            if (!pr) { await p.err(`mdm: ${p.args[0] ?? "<profile>"}: no such profile\n`); return 1 }
            await p.out(json(mock.createAssignment(pr, "tenant")))
            return 0
          }),
        },
      },
      commands: {
        summary: "commands to a device", usage: "mdm commands <send <device> [DeviceInformation|DeviceLock]|ls <device>>",
        subcommands: {
          send: sub("commands send", "send a command; it is queued, then the device answers", "mdm commands send <device> [type]", async (p) => {
            const d = findDevice(mock, p.args[0])
            if (!d) { await p.err(`mdm: ${p.args[0] ?? "<device>"}: no such device\n`); return 1 }
            const type = p.args[1] ?? "DeviceInformation"
            if (type !== "DeviceInformation" && type !== "DeviceLock") { await p.err(`mdm: type is DeviceInformation or DeviceLock\n`); return 2 }
            await p.out(json(mock.createCommand(d, type)))
            await p.out(`# 202 Accepted: try \`mdm commands ls ${short(d.id)}\` in a moment\n`)
            return 0
          }),
          ls: sub("commands ls", "a device's commands", "mdm commands ls <device>", async (p) => {
            const d = findDevice(mock, p.args[0])
            if (!d) { await p.err(`mdm: ${p.args[0] ?? "<device>"}: no such device\n`); return 1 }
            for (const c of mock.listCommands(d)) await p.out(`${short(c.command_uuid)}  ${pad(c.request_type, 18)} ${c.status}\n`)
            return 0
          }),
        },
      },
    },
  }
}

/** /tenants/demo/{devices,members,groups,profiles}/<id>.json, read-only. */
export function tenantsMount(mock: Mock, rite: RiteGlobal): MountProvider {
  const collections: Record<string, () => Array<{ id: string }>> = {
    devices: mock.listDevices, members: mock.listMembers, groups: mock.listGroups, profiles: mock.listProfiles,
  }
  const notFound = (rel: string) => new rite.RiteError("ENOENT", rel)
  const dir: Stat = { type: "dir", mode: 0o555, uid: 0, gid: 0, size: 0, mtime: Date.parse("2026-11-20T09:00:00Z") }
  const resolve = (rel: string): { kind: "dir"; entries: Entry[] } | { kind: "file"; text: string } | undefined => {
    const parts = rel.split("/").filter(Boolean)
    if (parts.length === 0) return { kind: "dir", entries: [{ name: TENANT, type: "dir" }] }
    if (parts[0] !== TENANT) return undefined
    if (parts.length === 1) return { kind: "dir", entries: Object.keys(collections).map((name) => ({ name, type: "dir" as const })) }
    const list = collections[parts[1]!]
    if (!list) return undefined
    if (parts.length === 2) return { kind: "dir", entries: list().map((x) => ({ name: `${x.id}.json`, type: "file" as const })) }
    const item = list().find((x) => `${x.id}.json` === parts[2])
    return parts.length === 3 && item ? { kind: "file", text: json(item) } : undefined
  }
  return {
    readonly: true,
    stat: async (rel) => {
      const r = resolve(rel)
      if (!r) throw notFound(rel)
      return r.kind === "dir" ? dir : { ...dir, type: "file", mode: 0o444, size: r.text.length }
    },
    list: async (rel) => {
      const r = resolve(rel)
      if (!r) throw notFound(rel)
      if (r.kind !== "dir") throw new rite.RiteError("ENOTDIR", rel)
      return r.entries
    },
    read: async (rel) => {
      const r = resolve(rel)
      if (!r) throw notFound(rel)
      if (r.kind !== "file") throw new rite.RiteError("EISDIR", rel)
      return r.text
    },
  }
}

export const memdsk: EggDef = {
  id: "memdsk",
  trigger: { command: "memdsk" },
  run: async (p) => {
    await p.err("memdsk: command not found. did you mean mdmsdk?\n")
    await p.out("(it happens. the letters are right there.)\n")
    return 127
  },
}

export { createMock }
