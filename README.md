# Doofinder API Reference Docs

Source for the Doofinder developer documentation site — Search API, Management API, Stats API, Recommendations API, and Category Merchandising API.

## Local development

Install the [Mintlify CLI](https://www.npmjs.com/package/mint):

```bash
npm i -g mint
```

Run the preview server from the root of this repo (where `docs.json` lives):

```bash
mint dev
```

Open `http://localhost:3000` in your browser.

## AI-assisted writing

To configure your AI coding tool to understand Mintlify components and conventions:

```bash
npx skills add https://mintlify.com/docs
```

This installs Mintlify's writing skill for Claude Code, Cursor, Windsurf, and similar tools.

## Publishing

Changes merged to the default branch are deployed automatically via the Mintlify GitHub app. Configure it from the [Mintlify dashboard](https://dashboard.mintlify.com/settings/organization/github-app).

## Troubleshooting

- **Preview not starting** — run `mint update` to get the latest CLI version.
- **Page shows 404** — make sure `docs.json` is present in the directory where you run `mint dev`.
- **Links broken after a rename** — update both `docs.json` navigation and any `href` references in MDX files.

## Resources

- [Mintlify documentation](https://mintlify.com/docs)
- [Doofinder Admin Panel](https://admin.doofinder.com)
- [Doofinder Support](https://support.doofinder.com)
