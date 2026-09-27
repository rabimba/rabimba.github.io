---
title: "ConferenceRank"
summary: "One-stop shop to evaluate CS conference & journal venues — CORE/ICORE ranks, SJR quartiles, multi-decade acceptance rates, submission deadlines (AoE), and an MCP server + JSON API for AI agents."
tags:
- Tooling
- Open Source
- MCP
- Research Infrastructure
- AI Agents
date: "2026-01-01"
reading_time: false
featured: true

links:
- icon: globe
  icon_pack: fas
  name: Live Site
  url: https://rabimba.github.io/ConferenceRank/
- icon: github
  icon_pack: fab
  name: GitHub
  url: https://github.com/rabimba/ConferenceRank
---

[ConferenceRank](https://rabimba.github.io/ConferenceRank/) is a unified platform for discovering, evaluating, and tracking computer science conference and journal venues. It aggregates public ranking and bibliometric data into an accessible, interactive interface backed by programmatic APIs.

### Key Features

- **Conference & Journal Rankings** &mdash; Complete CORE / ICORE rankings (A\*, A, B, C) with historical tier tracking, side-by-side with SCImago Journal Rank (SJR) quartiles (Q1–Q4), H-index, and FoR discipline categories.
- **Venue & Journal Suggester** &mdash; Abstract-matching engine using TF-IDF and discipline lexicons to recommend stretch, target, and safe venues for an upcoming paper.
- **Deadlines & Watchlist** &mdash; Submission countdowns normalized to Anywhere on Earth (AoE), with 1-click Google Calendar sync, `.ics` export, and zero-login local browser watchlists.
- **Acceptance Rate Trends** &mdash; Decades of acceptance statistics (submitted, accepted, rates) for leading venues across systems, AI/ML, security, databases, theory, and graphics.

### Built for AI Agents

ConferenceRank is machine-consumable out of the box:

- **MCP Server** (`npx conferencerank-mcp`) &mdash; Exposes six typed tools for MCP-compatible agents: `search_venues`, `get_venue`, `compare_venues`, `suggest_venues`, `upcoming_deadlines`, and `acceptance_stats`.
- **Static JSON API** &mdash; CDN-cached endpoints for conferences, journals, and upcoming deadlines, regenerated on weekly automated GitHub Actions runs.
- **Agent Skill & `llms.txt`** &mdash; Ships full instructions and machine-readable context for agentic workflows.
