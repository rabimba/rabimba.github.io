# Repository Guidelines

## Project Structure & Module Organization
This repository is a Hugo Blox academic site. Core content lives in `content/`, with leaf bundles like `content/publication/<slug>/index.md` and `content/events/<slug>/index.md`. Layout overrides are in `layouts/` (partials in `layouts/partials/`). Styling and assets live in `assets/` (`assets/css/custom.css`, `assets/scss/custom.scss`, and media under `assets/media/`). Static files are served from `static/`. PDFs for publications are stored in `Publications/`. Site configuration is under `config/_default/`, with module wiring in `hugoblox.yaml` and `go.mod`.

## Build, Test, and Development Commands
- `pnpm install`: install frontend tooling (Tailwind and related dependencies).
- `pnpm dev`: run the local Hugo server with fast render disabled for accurate previews.
- `pnpm build`: build the production site with minification via Hugo.
- `hugo server -D`: optional, serves draft content when you need to preview drafts.

## Coding Style & Naming Conventions
Use YAML front matter in `content/` and keep dates in `YYYY-MM-DD` format. New content should follow the existing slug style: lowercase with hyphens, and use `index.md` within a folder (leaf bundle). Match existing formatting in CSS (4-space indentation in `assets/css/custom.css`) and keep edits focused in `assets/css/` or `assets/scss/` rather than inline styles in templates.

## Testing Guidelines
No automated test framework is configured. Validate changes by running `pnpm build` to catch Hugo build errors and by checking the local preview with `pnpm dev`. For content-heavy changes, spot-check affected pages and links.

## Commit & Pull Request Guidelines
Commit history uses short, direct messages (e.g., "Update", "Removed pdf"). Keep messages concise and content-focused; add a scope when helpful (e.g., `content: add qucowe paper`). For PRs, include a brief summary, list of key pages touched, and link to any source material for publications or CV updates. Add screenshots when modifying layouts or styling. Note any new files added to `Publications/`.

## Automation & Data Updates
Repository root includes helper scripts (e.g., `create_pubs.py`, `update_pubs.py`, `convert_cv_to_md.py`) for updating publication and CV content. If you use them, review generated Markdown and ensure referenced PDFs exist under `Publications/`.
