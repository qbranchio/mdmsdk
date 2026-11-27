# mdmsdk docs site

The developer docs for mdmsdk: Astro Starlight, static output, served at `https://qbranchio.github.io/mdmsdk`.

## Setup

Node 22.23.4 or later.

```sh
npm ci
```

## Run

```sh
npm run dev      # local server with reload
npm run preview  # serve the last build
```

## Test

```sh
npm run build
```

The build runs four steps and fails on any of them:

1. `scripts/sync-contract.mjs` copies `../openapi/openapi.yaml` and the Scalar bundle into `public/`. Neither copy is committed.
2. `astro check` type-checks the config, pages, and components.
3. `astro build` renders the pages, `llms.txt`, and `llms-full.txt`, and validates every internal link.
4. `scripts/denylist.mjs` reads every file in `dist/` and fails on a string that must not be published.

## Layout

- `src/content/docs/`: the pages. One idea per page.
- `src/pages/reference.astro`: the API reference, Scalar over the published contract.
- `src/components/Terminal.astro`: the placeholder for the home page terminal. Replace the region between its `rite-terminal` markers.
- `src/styles/theme.css`: colors, type scale, and diagram colors.
- `astro.config.ts`: site URL, base path, sidebar, plugins.

Internal links carry the base path (`/mdmsdk/...`). When the site moves to its own domain, change `base` in `astro.config.ts` and the links; the build names any that were missed.
