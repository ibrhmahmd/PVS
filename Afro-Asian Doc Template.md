# Game Technical Documentation | التوثيق الفني للعبة

---

## 1. Game Overview | نظرة عامة على اللعبة

| Field | Value |
|-------|-------|
| **Game Title** | Space X |
| **Genre** | Educational Space Shooter (arcade) |
| **Description** | An educational space shooter. The player steers a ship, shoots falling asteroids and protects three hearts. When the ship runs out of hearts, the game shows a fact about one randomly chosen body of the solar system (the Sun and the eight planets), so every loss teaches something new. |
| **Target Age Group** | 5-99 years old |
| **Resolution** | 800x600 |
| **Frame Rate** | 60 FPS (Pygame Zero default) |
| **Language** | English |

### Dependencies | المكتبات المستخدمة

| Library | Purpose |
|---------|---------|
| `pgzero` | Game runtime engine (`Actor`, `screen`, `keyboard`, `music`) |
| `pygame` | Fullscreen toggle, loading the fact image, crash sound effect |
| `random` | Asteroid spawn position, random fact selection |

<!-- Screenshot: Start screen of your game -->

---

## 2. Game Mechanics | آليات اللعبة

### Gameplay Constants | ثوابت اللعب

| Constant | Value | Description |
|----------|-------|-------------|
| Ship speed | 9 px/frame | Horizontal movement; the ship stays between x = 50 and x = 750 |
| Bullet speed | 10 px/frame | Bullets travel upward and are removed above the screen |
| Starting health | 3 hearts | Drawn at the top-right |
| Asteroid spawn interval | `max(20, 60 - score/2)` frames | Starts at 60 and shrinks to 20 as the score grows |
| Asteroid speed | `3 + min(score/10, 5)` px/frame | Starts at 3 and caps at 8 |
| Level | `1 + score // 30` | Display only; difficulty comes from the score |
| Music volume | 0.9 | Looping background track |
| Crash sound volume | 0.4 | Played when an asteroid hits the ship |

### Controls | التحكم

| Input | Action | Context |
|-------|--------|---------|
| ← → Arrow Keys | Move the ship left/right | While playing |
| SPACE | Start the game / fire a bullet | Title screen / while playing |
| P | Pause / resume | While playing |
| R | Restart | Game over screen |
| F | Toggle fullscreen | Any time |

### Victory Conditions | شروط الفوز

| Mode | Win Condition | Lose Condition |
|------|---------------|----------------|
| Endless run | None. The goal is to beat the high score | Health reaches 0 |

### Scoring System | نظام النقاط

| Mechanic | Effect | Notes |
|----------|--------|-------|
| Shoot an asteroid | +1 score | The asteroid and the bullet are both removed |
| Asteroid hits the ship | -1 health | Plays the crash sound |
| Asteroid falls past the bottom of the screen | -1 health | Missing an asteroid costs a heart |
| Reach 30, 60, 90... points | Level +1 | Shown at the bottom-right |
| Health reaches 0 | Game over | Shows a solar-system fact, then R restarts |
| High score | Best score of the session | Kept in memory only, reset when the game closes |

---

## 3. Screen Flow | تدفق الشاشات

### State Diagram | مخطط الحالات

```
        ┌──────────────────┐
        │   TITLE SCREEN   │
        │ logo + tagline   │
        └────────┬─────────┘
                 │ SPACE
                 ▼
        ┌──────────────────┐   P    ┌──────────────┐
        │     PLAYING      │◄──────►│    PAUSED    │
        │ shoot asteroids  │   P    │ music stops  │
        └────────┬─────────┘        └──────────────┘
                 │ health = 0
                 ▼
        ┌──────────────────┐
        │    GAME OVER     │
        │ planet fact +    │
        │ image            │
        └────────┬─────────┘
                 │ R (resets score, health, level)
                 └──────────────► PLAYING
```

### Screen Reference | دليل الشاشات

| Screen | Module / File | Description | Transitions To |
|--------|---------------|-------------|----------------|
| Title | `game.py` (`game_started = False`) | Logo, tagline, "Press Space to Start" | Playing |
| Playing | `game.py` | Ship, bullets, asteroids, hearts, score, level, high score | Paused, Game Over |
| Paused | `game.py` (`paused = True`) | "PAUSED" overlay, music stopped | Playing |
| Game Over | `game.py` (`health <= 0`) | Random solar-system fact from `game_data.py`, "GAME OVER", "Press R to Restart" | Playing |

### Global UI Elements | عناصر الواجهة العامة

| Element | Position | Description |
|---------|----------|-------------|
| Score | Top-left | Current score |
| Hearts | Top-right | One heart per remaining health |
| High Score | Bottom-left | Best score of the session |
| Level | Bottom-right | `1 + score // 30` |

---

## 4. Level Design | تصميم المراحل

Space X has no separate levels. It is one endless run whose difficulty rises with the score.

| Score | Level shown | Spawn interval | Asteroid speed |
|-------|-------------|----------------|----------------|
| 0 | 1 | 60 frames | 3.0 |
| 30 | 2 | 45 frames | 6.0 |
| 60 | 3 | 30 frames | 8.0 (cap) |
| 80+ | 3+ | 20 frames (floor) | 8.0 |

### Educational Facts | الحقائق التعليمية

After each game over, one entry of `space_info_list` (`game_data.py`) is picked at random. Each entry is an image plus a few lines of text:

| Body | Image |
|------|-------|
| Sun | `Sun.png` |
| Mercury | `Mercury.png` |
| Venus | `Venus.png` |
| Earth | `Earth.png` |
| Mars | `Mars.png` |
| Jupiter | `Jupiter.png` |
| Saturn | `Saturn.png` |
| Uranus | `Uranus.png` |
| Neptune | `Neptune.png` |

---

## 5. Asset Inventory | جرد الموارد

### Images | الصور

| Category | File Name | Path | Used In |
|----------|-----------|------|---------|
| Background | `space_background` | `images/backgrounds/` | All screens |
| Background | `uropa` | `images/backgrounds/` | (available asset) |
| Character | `ship` | `images/characters/` | Player ship |
| Character | `hero` | `images/characters/` | (available asset) |
| UI Button | `continue`, `left`, `pause`, `right` (.jpeg) | `images/buttons/` | (available assets) |
| UI Icon | `health` | `images/` | Hearts |
| UI Logo | `logogame` | `images/` | Title screen |
| Hazard | `asteroid` | `images/` | Falling asteroids |
| Projectile | `bullet` | `images/` | Ship's bullets |
| Fact image | `Sun`, `Mercury`, `Venus`, `Earth`, `Mars`, `Jupiter`, `Saturn`, `Uranus`, `Neptune` | `images/` | Game Over fact screen |
| Environment | `Moon`, `Astoriods Belts` | `images/` | (available assets) |

### Audio | الصوتيات

| Type | File Name | Path | Purpose |
|------|-----------|------|---------|
| Background Music | `music.mp3` | `music/` | Loops while playing |
| Sound Effect | `crash.mp3` | `music/` | Asteroid hits the ship |

### Total Asset Count | إجمالي الموارد

| Type | Count |
|------|-------|
| Backgrounds | 2 |
| Characters | 2 |
| UI Elements (buttons, heart, logo) | 6 |
| Hazards / Projectiles | 2 |
| Fact images | 9 |
| Other space images | 2 |
| Audio files | 2 |
| **Total** | **25** |

---

## 6. Educational Content | المحتوى التعليمي

### Learning Objectives | أهداف التعلم

By the end of this project, the student will be able to:

1. Understand the game loop (draw → update → input events) in Pygame Zero
2. Manage game state with variables and flags (`game_started`, `paused`, `health`)
3. Implement collision detection between a ship, bullets and asteroids
4. Scale difficulty with the player's score
5. Store content in a data structure (`space_info_list`) and show it at random
6. Learn basic facts about the Sun and the planets of the solar system

### Cultural / Historical Context | السياق الثقافي / التاريخي

| Topic | Description |
|-------|-------------|
| The Sun | The star at the centre of the solar system and the source of daytime light |
| Mercury | The smallest planet and the closest to the Sun |
| Venus | The hottest planet in the solar system |
| Earth to Neptune | Each game over shows the facts for one of them, with an image |

### Curriculum Alignment | التوافق مع المنهج

| Skill Area | What the Student Practices |
|------------|---------------------------|
| Problem Solving | Debugging collisions and the game-over and restart logic |
| Computational Thinking | Game state, conditions, spawn timers, difficulty scaling |
| Creativity | Designing the ship, asteroids and fact screens |
| Collaboration | Splitting the work between code, art and content |
| Technical Writing | Documenting game mechanics and assets |

---

## 7. Marketing Plan | خطة تسويقية

> **Short version** — for full marketing plans, use the main Afro-Asian template.

### Target Audience | الجمهور المستهدف

- **Primary**: School students who want to learn about the solar system through play
- **Secondary**: Teachers looking for science-integrated coding projects
- **Tertiary**: Casual gamers and Afro-Asian Tech Forum participants

### Platforms | المنصات

- Desktop (Windows), planned as a PyInstaller build
- itch.io page (planned) with the Windows download and a source zip
- School computer labs

### Promotion Ideas | أفكار ترويجية

1. Present at the Afro-Asian Tech Forum as an educational game
2. Share a gameplay demo video and screenshots
3. Demo at an end-of-semester school exhibition
4. Link the game from the Pixel Verse Studios website

---

## 8. Student Worksheet | ورقة عمل الطالب

> **Instructions**: Copy this section into your own document and fill it in for YOUR game project.

---

### My Game Information | معلومات لعبتي

**Student Name**: ___________________________

**Game Title**: Space X

**Date**: ___________________________

---

#### What is your game about? | عن ماذا تتحدث لعبتك؟

An educational space shooter. The player shoots asteroids to protect the ship, and every game over reveals a fact about the Sun or a planet.

#### What makes your game special? | ما الذي يجعل لعبتك مميزة؟

Losing teaches something: each game over shows a new solar-system fact with a picture, so the player learns while trying to beat their high score.

---

### My Game Mechanics | آليات لعبتي

**My game type** (circle one): Platformer / Puzzle / Catcher / Runner / Other: Space shooter

**Controls in my game**:

| Key/Button | What it does |
|------------|-------------|
| ← → Arrow Keys | Move the ship |
| SPACE | Start the game / shoot |
| P | Pause / resume |
| R | Restart after game over |
| F | Fullscreen |

**How does the player win?** | كيف يفوز اللاعب؟

There is no final win. The player tries to get the highest score and learn as many facts as possible.

**How does the player lose?** | كيف يخسر اللاعب؟

An asteroid hits the ship or falls past the bottom of the screen. Each costs one of the 3 hearts.

---

### My Screens | شاشات لعبتي

| Screen Name | What happens here | How to get here |
|-------------|-------------------|-----------------|
| Title | Logo and "Press Space to Start" | Launch the game |
| Playing | Shoot asteroids, watch score, hearts and level | Press SPACE |
| Paused | Game frozen, music stopped | Press P |
| Game Over | A solar-system fact and picture | Lose all 3 hearts |

---

### My Levels | مراحل لعبتي

| Level Name | Theme | What to do | Win condition |
|------------|-------|------------|---------------|
| Endless run | Outer space | Shoot falling asteroids; the level number rises every 30 points | None. Beat the high score |

---

### My Assets | موارد لعبتي

**Images I used**:

| Image | What it is used for |
|-------|---------------------|
| ship | Player ship |
| asteroid | Enemy |
| bullet | Ship's projectile |
| health | Heart icon |
| logogame | Title screen logo |
| space_background | Background |
| Sun, Mercury ... Neptune | Fact screen after game over |

**Audio I used**:

| Sound | What it is used for |
|-------|---------------------|
| music.mp3 | Background music |
| crash.mp3 | Asteroid hits the ship |

---

### What I Learned | ما تعلمته

1. The hardest part of making my game was: _________________________________

2. The most fun part of making my game was: _________________________________

3. If I had more time, I would add: _________________________________

4. One thing I would do differently: _________________________________

---

### Screenshot of My Game | لقطة شاشة من لعبتي

<!-- Paste a screenshot of your game running here -->

---

**Instructor Notes** | ملاحظات المدرس:

_______________________________________________
_______________________________________________
