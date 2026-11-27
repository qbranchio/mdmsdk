// Copies the published contract and the Scalar bundle into public/ so the
// build serves them. Neither copy is committed: openapi/openapi.yaml is the
// one source of the contract, and package.json pins the bundle.
import { copyFile, mkdir } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const site = resolve(dirname(fileURLToPath(import.meta.url)), '..');

const copies = [
  [resolve(site, '../openapi/openapi.yaml'), resolve(site, 'public/openapi.yaml')],
  [
    resolve(site, 'node_modules/@scalar/api-reference/dist/browser/standalone.js'),
    resolve(site, 'public/scalar/standalone.js'),
  ],
];

for (const [from, to] of copies) {
  await mkdir(dirname(to), { recursive: true });
  await copyFile(from, to);
  console.log(`sync: ${to.slice(site.length + 1)}`);
}
