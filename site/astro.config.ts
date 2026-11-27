import starlight from '@astrojs/starlight';
import mermaid from 'astro-mermaid';
import { defineConfig } from 'astro/config';
import starlightLinksValidator from 'starlight-links-validator';
import starlightLlmsTxt from 'starlight-llms-txt';

const repo = 'https://github.com/qbranchio/mdmsdk';
const description =
  'Go and Python SDKs for the mdm API: manage tenants, members, groups, devices, profiles, and commands for Apple devices.';

// GitHub Pages serves the site under /mdmsdk until it has a domain of its own.
export default defineConfig({
  site: 'https://qbranchio.github.io',
  base: '/mdmsdk',
  output: 'static',
  trailingSlash: 'always',
  integrations: [
    // Before starlight, so it sees the mermaid fences first. Colors come from
    // src/styles/theme.css, which follows the site theme without a re-render.
    mermaid({
      theme: 'base',
      autoTheme: false,
      enableLog: false,
      mermaidConfig: {
        fontFamily: 'system-ui, -apple-system, "Segoe UI", sans-serif',
        flowchart: { curve: 'linear', nodeSpacing: 40, rankSpacing: 44 },
        sequence: { mirrorActors: false },
      },
    }),
    starlight({
      title: 'mdmsdk',
      description,
      favicon: '/favicon.svg',
      customCss: ['./src/styles/theme.css'],
      social: [{ icon: 'github', label: 'GitHub', href: repo }],
      editLink: { baseUrl: `${repo}/edit/main/site/` },
      expressiveCode: {
        themes: ['github-dark-default', 'github-light-default'],
        useStarlightUiThemeColors: true,
        styleOverrides: { borderRadius: '6px', frames: { shadowColor: 'transparent' } },
        // Shell blocks are one command to copy: no window chrome around them.
        defaultProps: { overridesByLang: { 'sh,bash,shell': { frame: 'none' } } },
      },
      sidebar: [
        { label: 'Quickstart', slug: 'quickstart' },
        {
          label: 'Concepts',
          items: [
            'concepts/accounts-and-tenants',
            'concepts/members-and-groups',
            'concepts/devices',
            'concepts/profiles',
            'concepts/declarations',
            'concepts/commands',
            'concepts/webhooks',
            'concepts/apple-credentials',
          ],
        },
        {
          label: 'Guides',
          items: [
            'guides/authentication',
            'guides/browser',
            'guides/idempotency-and-retries',
            'guides/errors',
            'guides/webhooks',
          ],
        },
        {
          label: 'Reference',
          items: [
            { label: 'API reference', link: '/reference/' },
            'agents',
          ],
        },
      ],
      plugins: [
        starlightLinksValidator({
          // Served outside the docs collection: the Scalar page and the files
          // the plugin and the sync script add.
          exclude: ['/mdmsdk/reference/', '/mdmsdk/llms.txt', '/mdmsdk/llms-full.txt', '/mdmsdk/openapi.yaml'],
        }),
        starlightLlmsTxt({
          projectName: 'mdmsdk',
          description,
          // The home page terminal is for people; agents get the pages.
          customSelectors: { all: ['#terminal'] },
          details: [
            'The API is REST under `https://enroll.dev/api/v1`. Callers are account clients (OAuth client credentials) and delegated tokens the API issues for one tenant.',
            'Errors are RFC 9457 problems: branch on `code`, never on `status` or `title`, and quote `instance` when reporting one.',
            'Policy reaches devices only as declarations, and commands and several writes are asynchronous.',
          ].join('\n\n'),
          optionalLinks: [
            {
              label: 'OpenAPI contract',
              url: 'https://qbranchio.github.io/mdmsdk/openapi.yaml',
              description: 'the published contract the SDKs are generated from',
            },
            { label: 'Repository', url: repo, description: 'SDK source, AGENTS.md, and the mdmsdk skill' },
          ],
        }),
      ],
    }),
  ],
});
