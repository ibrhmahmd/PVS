# Issues

## #1 — Studio documentation, poster and presentation `[docs]`

**Status:** rebuilt from the project-showcase templates 2026-10-22; waiting for the team to fill the yellow boxes

Afro-Asian Technology Competition 2026, Games category. One set of deliverables for Pixel Verse Studios with both games (Crab Quest and Space X: Journey to Jupiter). English only, in the website's design system. Reference layout: `egy_law/docs/poster` (Ma'at).

- [x] Studio documentation (Afro-Asian template sections 1-9, one block per game): `docs/documentation/` as Markdown + PDF
- [x] Poster, 1000×2000 mm portrait: `docs/poster/` as HTML + PDF + preview PNG
- [x] Presentation, about 10 slides, 16:9: `docs/presentation/` as HTML → PDF and an editable PPTX
- [x] Team: five members shown as names + portraits (Mariam Alaa, Selim Loai, Mohamed Loai, Medhat Ali, Salah Mohamed)
- [x] Rename the 'Sleem' label on `pixel-verse-studios/studio-lore.html` to Selim
- [ ] Poster QR code: **needs the studio URL from the user** (placeholder: itch.io studio page)
- [x] Remove the superseded `Afro-Asian Doc Template.md` from the repo root

Space X screenshots were captured from the real game (headless run), not mocked up. Files and build script live in `docs/`.

2026-10-22: rebuilt `docs/` from the `project-showcase` templates (English only, AFFIAT Aswan Finals 2026 logos kept, QR now points at the GitHub Pages address). The earlier hand-made kit and its editable PPTX are in git history (commit `8160cd4` and later). Still open: the yellow boxes (tagline, problem, solution, audience, name story, learning, marketing, email), and GitHub Pages must be turned on for the QR code to work.
