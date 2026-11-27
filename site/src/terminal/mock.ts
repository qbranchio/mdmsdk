// An in-browser mock of the mdm API: one tenant, its members, groups,
// devices, profiles, and commands, held per visitor. The shapes follow the
// published contract (openapi/openapi.yaml).

const now = () => new Date().toISOString()
const at = "2026-11-20T09:00:00Z"
const uuid = () => crypto.randomUUID()

export interface Member { id: string; external_id?: string; name: string; groups: string[]; created_at: string; updated_at: string }
export interface Group { id: string; name: string; priority: number; created_at: string; updated_at: string }
export interface Device {
  id: string; member_id: string | null; name: string; status: string; enrollment_id: string | null; udid: string | null
  serial_number: string | null; model: string | null; os_version: string | null; supervised: boolean
  os_latest: string | null; os_behind: boolean; last_seen_at: string | null; created_at: string
  policy: null; settings: unknown[]
}
export interface Profile { id: string; name: string; items: unknown[]; created_at: string; updated_at: string }
export interface Command { command_uuid: string; request_type: string; status: string; result: unknown; error: unknown; created_at: string; updated_at: string }

export function createMock() {
  const kids = { id: "4f1c2a8e-0b6d-4c3e-9a51-7d2e8f6b1a01", name: "Kids", priority: 10, created_at: at, updated_at: at }
  const members: Member[] = [
    { id: "9b3e7c11-5a2f-4d6e-8c40-1f7a2b9d3e02", external_id: "crm-41", name: "Ada", groups: [kids.id], created_at: at, updated_at: at },
    { id: "2d8a4f60-7c1b-4e9a-b35d-6e0c9f2a8b03", external_id: "crm-42", name: "Linus", groups: [], created_at: at, updated_at: at },
  ]
  const device = (id: string, member: string | null, name: string, model: string, os: string, supervised: boolean): Device => ({
    id, member_id: member, name, status: "enrolled", enrollment_id: uuid(), udid: uuid().toUpperCase(),
    serial_number: "F" + id.slice(0, 9).replace(/-/g, "").toUpperCase(), model, os_version: os, supervised,
    os_latest: "27.2", os_behind: os !== "27.2", last_seen_at: at, created_at: at, policy: null, settings: [],
  })
  const devices: Device[] = [
    device("7a6e3c29-1f4b-4d8a-9e20-5b3c1d7f9a04", members[0]!.id, "Ada's iPad", "iPad Air (M3)", "27.2", true),
    device("c3f19b80-6d2e-4a7c-8f15-0e9a4b2d6c05", members[1]!.id, "Linus's iPhone", "iPhone 17", "27.1", false),
    device("e85b2d47-3a9c-4f6e-a710-2c8d5f1b0e06", null, "Kitchen iPad", "iPad (A16)", "27.2", true),
  ]
  const profiles: Profile[] = [
    { id: "1b7d9e42-8c3a-4f50-b6e1-9a2c4d8f3b07", name: "School hours", items: [], created_at: at, updated_at: at },
    { id: "5e2a8c17-4b9d-4e3f-8a62-7c0d1f5b9e08", name: "No App Store", items: [], created_at: at, updated_at: at },
  ]
  const groups: Group[] = [kids]
  const commands = new Map<string, Command[]>()

  const byRef = <T extends { id: string; external_id?: string }>(list: T[], ref: string): T | undefined =>
    list.find((x) => x.id === ref || (ref.startsWith("ext:") && x.external_id === ref.slice(4)))

  return {
    me: () => ({ kind: "account_client", account: { id: "00000000-0000-4000-8000-0000000000aa", name: "Demo account" } }),
    listDevices: () => devices,
    getDevice: (id: string) => devices.find((d) => d.id === id || d.id.startsWith(id)),
    listMembers: () => members,
    getMember: (ref: string) => byRef(members, ref),
    listGroups: () => groups,
    listProfiles: () => profiles,
    getProfile: (id: string) => profiles.find((p) => p.id === id || p.id.startsWith(id)),
    createAssignment: (profile: Profile, target: string, targetId?: string) => ({
      id: uuid(), profile_id: profile.id, target, target_id: targetId ?? null, levels: ["supervised", "unsupervised"], created_at: now(),
    }),
    createCommand: (device: Device, type: string) => {
      const c: Command = { command_uuid: uuid(), request_type: type, status: "outbox", result: null, error: null, created_at: now(), updated_at: now() }
      commands.set(device.id, [...(commands.get(device.id) ?? []), c])
      // The device answers a moment later, as a real one would.
      setTimeout(() => { c.status = "acknowledged"; c.updated_at = now() }, 1500)
      return { command_uuid: c.command_uuid }
    },
    listCommands: (device: Device) => commands.get(device.id) ?? [],
  }
}

export type Mock = ReturnType<typeof createMock>
