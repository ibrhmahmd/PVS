# AGENTS.md — Pixel Verse Studios

Static site for an indie game studio: four plain HTML pages, `assets/css/styles.css`, `assets/js/site.js`. No build step, no Node, no Tailwind.

**Read `CLAUDE.md` first.** It holds the kid-simple rules, the page rules and the real game facts. The short version:

- Keep code plain enough for a 12-year-old to read: plain functions, loops and `if`s, kid-word comments, no clever tricks, no new libraries.
- Class names say what a thing is (`.card`, `.badge`, `.beat`). Colours and sizes are variables at the top of `styles.css`.
- The header and footer are copied into each page; change all four.
- Never invent game content. Titles are exactly "Crab Quest" and "Space X".
- Removing a feature or safety? Add it to the README **Limits** section.

| Task | Command |
|---|---|
| Verify the site | `python3 scripts/check_site.py` |
| Preview locally | `python3 -m http.server 8000` |

Leave changes uncommitted for review unless told otherwise.
