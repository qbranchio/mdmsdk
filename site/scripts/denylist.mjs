// Fails the build when a built file carries a string that must never be
// published: a private path, module, host, or address. It reads every file
// under dist/ as bytes, so pages, scripts, the contract copy, llms.txt, and
// search index fragments are all covered.
import { readdir, readFile } from 'node:fs/promises';
import { dirname, join, relative, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const dist = resolve(dirname(fileURLToPath(import.meta.url)), '../dist');

// Matching is exact and case-sensitive: "device management API" is ordinary
// prose, and bundled libraries carry strings such as "Internal/" that are
// not ours.
const denied = [
  'docs/specs',
  'jarrodb',
  'nanomdm',
  'x-go-',
  '.mdm.test',
  'Management API',
  'internal/',
  '10.77.',
  '127.0.0.41',
];

/** @param {string} dir @returns {Promise<string[]>} */
async function walk(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  const nested = await Promise.all(
    entries.map((entry) => {
      const path = join(dir, entry.name);
      return entry.isDirectory() ? walk(path) : Promise.resolve([path]);
    }),
  );
  return nested.flat();
}

/** @param {string} text @param {number} at @param {number} length */
function excerpt(text, at, length) {
  return text
    .slice(Math.max(0, at - 40), at + length + 40)
    .replace(/[^\x20-\x7e]+/g, ' ')
    .trim();
}

let files;
try {
  files = await walk(dist);
} catch {
  console.error(`denylist: ${dist} not found; run astro build first`);
  process.exit(2);
}
if (files.length === 0) {
  console.error('denylist: dist/ is empty');
  process.exit(2);
}

const hits = [];
for (const file of files) {
  // latin1 maps each byte to one character, so offsets are byte offsets and
  // binary files are searched too.
  const text = (await readFile(file)).toString('latin1');
  for (const term of denied) {
    for (let at = text.indexOf(term); at !== -1; at = text.indexOf(term, at + 1)) {
      hits.push({ file: relative(dist, file), term, at, context: excerpt(text, at, term.length) });
    }
  }
}

if (hits.length > 0) {
  for (const hit of hits) {
    console.error(`denylist: ${hit.file}@${hit.at}: "${hit.term}" in "${hit.context}"`);
  }
  console.error(`denylist: ${hits.length} match(es) in ${new Set(hits.map((h) => h.file)).size} file(s)`);
  process.exit(1);
}
console.log(`denylist: ${files.length} files clean`);
