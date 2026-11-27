// The part of riteshjs (window.Rite, loaded from the CDN) the docs terminal uses.
export interface Proc {
  argv: readonly string[]
  args: readonly string[]
  flags: Record<string, unknown>
  subcommand: readonly string[]
  out(text: string): Promise<void>
  err(text: string): Promise<void>
}
export interface Entry { name: string; type: "dir" | "file" }
export interface Stat { type: "dir" | "file"; mode: number; uid: number; gid: number; size: number; mtime: number }
export interface MountProvider {
  readonly readonly: boolean
  stat(rel: string, o: object): Promise<Stat>
  list(rel: string, o: object): Promise<Entry[]>
  read(rel: string, o: object): Promise<string>
}
export interface CommandDef {
  name: string
  summary: string
  usage: string
  manual?: string
  flags?: Record<string, { long?: string; short?: string; type: "boolean" | "string" | "number"; description?: string }>
  subcommands?: Record<string, Omit<CommandDef, "name">>
  run?: (p: Proc) => Promise<number | void>
}
export interface EggDef { id: string; trigger: { command: string }; run: (p: Proc) => Promise<number | void | symbol> }
export interface RiteGlobal {
  createRite(o: Record<string, unknown>): { fit(): void; focus(): void; dispose(): void }
  RiteError: new (errno: string, path?: string) => Error
}
