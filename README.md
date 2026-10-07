# Pixel Verse Studios website

The marketing website for Pixel Verse Studios and its two games, **Crab Quest** and **Space X**.

## How it works

It is four plain web pages. There is no server, no database and no build step.

| File | What it shows |
|---|---|
| `index.html` | Home: the big hero, the two games, the studio philosophy |
| `games.html` | Both games in full: chapters, controls, characters, planets |
| `heros-journey.html` | The "Story Spine" story of each game, beat by beat |
| `studio-lore.html` | The studio story, the team, how the games are made |

Every page uses the same three shared parts:

- `assets/css/styles.css` — all the looks, in one file. Colours and sizes are at the top.
- `assets/js/site.js` — one job: click a screenshot to see it big (the lightbox).
- `assets/img/` — every picture. The originals are kept in `design/source-media/`.

The header and footer are copied into each page, so a change to them must be made in all four pages.

## Run it

Open `index.html` in a browser, or serve the folder:

```sh
python3 -m http.server 8000   # then open http://localhost:8000
```

## Check it

```sh
python3 scripts/check_site.py
```

It checks the titles, the links, the nav, that every screenshot can be enlarged, that the real game content is still there, and that every picture is used.

## Put it online

Upload the folder to any static host (Netlify, GitHub Pages, Vercel). Nothing needs to be built first.

## Limits

These are choices made on purpose to keep the site simple:

- **No forms.** There is no newsletter signup and no contact form, so visitors cannot send us anything from the site. The Contact link goes to the "Get in touch" text on the Studio & Lore page.
- **No mobile menu button.** On a phone the nav links sit in a row under the logo and wrap onto a second line.
- **Header and footer are copied** into all four pages, not shared. Change all four.
- **Fonts and icons come from Google** (Google Fonts and Material Symbols). Offline, the site falls back to plain fonts and the footer icons do not show.
- **The footer links (itch.io, Discord, YouTube, Terms, Privacy) point nowhere yet** (`href="#"`). See issue #4.
- **The CSS is written by hand.** New looks mean new rules in `styles.css`. There is no tool that makes them for you.
