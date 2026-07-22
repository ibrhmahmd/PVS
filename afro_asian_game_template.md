
# Game Technical Documentation | التوثيق الفني للعبة

---

## 1. Game Overview | نظرة عامة على اللعبة

| Field | Value |
|-------|-------|
| **Game Title** | Crab Game |
| **Genre** | Multi-genre (Platformer / Survival / Catcher) |
| **Description** | An ocean-themed educational adventure game following a crab's journey through 6 chapters — from escaping a kitchen, dodging predators, avoiding pollution, helping other sea creatures, to reuniting with family. Each level introduces unique mechanics while raising awareness about marine life and ocean conservation. |
| **Target Age Group** | 8-14 years old |
| **Resolution** | 1200x600 |
| **Frame Rate** | 60 FPS |
| **Language** | English |

### Dependencies | المكتبات المستخدمة

| Library | Purpose |
|---------|---------|
| `pgzero` | Game runtime engine |
| `pygame` | Low-level graphics/audio (bundled with pgzero) |
| `random` | Randomized game elements (spawning, directions) |

<!-- Screenshot: Start screen of your game -->

<details>
<summary>Example: Ibn Battota Game</summary>

| Field | Value |
|-------|-------|
| **Game Title** | Ibn Battota Game |
| **Genre** | Educational Platformer (multi-genre levels) |
| **Description** | An educational platformer game based on the travels of Ibn Battota (14th-century Moroccan explorer). Players navigate through 5 historical cities, collecting artifacts and solving puzzles. |
| **Target Age Group** | 10-16 years old |
| **Resolution** | 1280x720 |
| **Frame Rate** | 60 FPS |
| **Language** | English |

### Dependencies

| Library | Purpose |
|---------|---------|
| `pgzero` | Game runtime engine |
| `pygame` | Low-level graphics (overlay surfaces) |
| `random` | Level generation, item spawning, shuffle |
| `os` | File path handling |

</details>

---

## 2. Game Mechanics | آليات اللعبة

### Physics Constants | ثوابت الفيزياء

| Constant | Value | Description |
|----------|-------|-------------|
| `GRAVITY` | 0.5 – 0.8 | Downward acceleration per frame (varies by level) |
| `JUMP_POWER` | -12 to -16 | Initial upward velocity on jump (negative = up) |
| `MOVE_SPEED` | 3 – 8 | Horizontal pixels per frame (varies by level) |
| `BIRD_SPEED` | 2 | Falling speed of birds (Level 2) |
| `POLLUTION_SPEED` | 2 | Falling speed of trash (Level 3) |
| `FISH_SPEED` | 7 | Patrol speed of evil fish (Level 5) |

### Controls | التحكم

| Input | Action | Context |
|-------|--------|---------|
| ← → Arrow Keys / A D | Move left/right | All levels |
| SPACE | Jump | Platformer levels (1, 4, 5, 6) |
| R | Restart level | On game over or win screen |
| ENTER | Return to level select | On win screen |
| Mouse Click | Select level / Start / Mute | Menu screens |

### Victory Conditions | شروط الفوز

| Level | Win Condition | Lose Condition |
|-------|---------------|----------------|
| 1. Kitchen Escape | Reach the goal at top-right | None — can retry anytime |
| 2. Beach Run | Survive birds for 30s, then reach the ocean wave | Bird collision |
| 3. Sea Floor Dodging | Survive pollution for 10s, then follow the turtle | Trash collision |
| 4. Shrimp Help | Collect all 17 algae food items | Timer runs out (60s) |
| 5. Predator Chase | Survive patrolling fish for 45 seconds | Fish collision |
| 6. Home Sweet Home | Reach your crab family at the sanctuary | None — final level |

### Scoring System | نظام النقاط

| Mechanic | Points | Notes |
|----------|--------|-------|
| Complete a level | Unlock progression | No numeric score — progression-based |
| Collect food (Level 4) | -1 remaining | Collect all 17 to win |
| Survive timer | Win | Timer-based levels end in victory |
| Collision with hazard | Game Over | Restart via R key |

<details>
<summary>Example: Ibn Battota Game</summary>

### Physics Constants

| Constant | Value | Description |
|----------|-------|-------------|
| `GRAVITY` | 0.5 | Downward acceleration per frame |
| `JUMP_STRENGTH` | -12 | Initial upward velocity on jump |
| `MOVE_SPEED` | 6 | Horizontal pixels per frame (10 in Damascus) |
| `GROUND_Y` | 650 | Y position of the ground line |

### Controls

| Input | Action | Context |
|-------|--------|---------|
| ← → Arrow Keys | Move left/right | Platformer levels (Tangier, Cairo) |
| ↑ Arrow Key / SPACE | Jump | Platformer levels |
| SPACE | Dismiss mission / Continue | All screens |
| Mouse Click | Select city / Flip card / Click back | Map, Fez, all menus |

### Victory Conditions

| Level | Win Condition | Lose Condition |
|-------|---------------|----------------|
| Tangier | Collect all 10 artifacts | None — can retry anytime |
| Fez | Match all 8 pairs | Timer reaches 0 (90 seconds) |
| Cairo | Collect all 8 items | None — can retry anytime |
| Damascus | Reach score of 50 | None — can retry anytime |

### Scoring System

| Mechanic | Points | Notes |
|----------|--------|-------|
| Collect good item (Quran, Lamp) | +1 or +2 | Varies by item |
| Collect rare item (Dirhams) | +5 | Silver coins |
| Hit scorpion | -10 | Bad item |
| Hit rock | -5 | Bad item |
| Score floor | 0 | Cannot go negative |

</details>

---

## 3. Screen Flow | تدفق الشاشات

### State Diagram | مخطط الحالات

```
                    ┌──────────────┐
                    │ START SCREEN │
                    │ (start_btn)  │
                    └──────┬───────┘
                           │ click Play
                           ▼
                    ┌──────────────┐
                    │ LEVEL SELECT │
                    │  (6 levels)  │
                    └──┬──┬──┬──┬──┘
                       │  │  │  │
          ┌────────────┘  │  │  └────────────┐
          ▼               ▼  ▼               ▼
   ┌────────────┐ ┌────────────┐ ┌────────────┐
   │  LEVEL 1   │ │  LEVEL 2   │ │  LEVEL 3   │
   │  Kitchen   │ │  Beach Run │ │ Sea Floor  │
   │  Escape    │ │            │ │  Dodging   │
   └─────┬──────┘ └─────┬──────┘ └─────┬──────┘
         │ win          │ win/lose      │ win/lose
         └──────────────┴───────────────┘
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
   ┌────────────┐  ┌────────────┐  ┌────────────┐
   │  LEVEL 4   │  │  LEVEL 5   │  │  LEVEL 6   │
   │  Shrimp    │  │  Predator  │ │  Home      │
   │  Help      │  │  Chase     │ │  Sweet Home│
   └─────┬──────┘  └─────┬──────┘  └─────┬──────┘
         │ win           │ win           │ win
         └───────────────┴───────────────┴──► START SCREEN
```

### Screen Reference | دليل الشاشات

| Screen | Module / File | Description | Transitions To |
|--------|---------------|-------------|----------------|
| Start | `start_screen.py` | Title screen with logo, animated fish, start button | Level Select |
| Level Select | `level_select.py` | 6 level buttons in a 3x2 grid | Any Level |
| Level 1 | `level_1.py` | Platformer — reach the goal | Level Select (on win) |
| Level 2 | `level_2.py` | Survival — dodge birds, reach the wave | Level Select (on win/lose) |
| Level 3 | `level_3.py` | Survival — dodge pollution, follow turtle | Level Select (on win/lose) |
| Level 4 | `level_4.py` | Platformer — collect algae as shrimp | Level Select (on win/lose) |
| Level 5 | `level_5.py` | Survival — dodge patrolling fish | Level Select (on win/lose) |
| Level 6 | `level_6.py` | Platformer — reach crab family | Start Screen (on win) |

### Global UI Elements | عناصر الواجهة العامة

| Element | Position | Description |
|---------|----------|-------------|
| Mute Button | Top-right (WIDTH-50, 50) | Toggles background music on/off |

<details>
<summary>Example: Ibn Battota Game</summary>

### State Diagram

```
                    ┌──────────────┐
                    │ START SCREEN  │
                    │ (start_btn)   │
                    └──────┬───────┘
                           │ click Play
                           ▼
                    ┌──────────────┐
                    │  WORLD MAP    │
                    │ 13 cities     │◄──────────────┐
                    └──┬──┬──┬──┬──┘               │
          ┌────────────┘  │  │  └────────────┐     │
          ▼               ▼  ▼               ▼     │
   ┌────────────┐  ┌────────────┐  ┌────────────┐  │
   │  TANGIER   │  │    FEZ     │  │   CAIRO    │  │
   │ Platformer │  │   Memory   │  │ Platformer │  │
   │ 10 items   │  │ 8 pairs    │  │ 8 items    │  │
   └─────┬──────┘  └─────┬──────┘  └─────┬──────┘  │
         │ win           │ win           │ win     │
         └───────────────┴───────────────┴─────────┘
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
   ┌────────────┐  ┌────────────┐  ┌────────────┐
   │  DAMASCUS  │  │  TIMBUKTU  │  │  (future)  │
   │  Catcher   │  │ Platformer │  │            │
   │ Score 50+  │  │ 10 items   │  │            │
   └─────┬──────┘  └─────┬──────┘  └────────────┘
         │ win           │ win
         └───────────────┴──────────► WORLD MAP
```

### Screen Reference

| Screen | Module | Description | Transitions To |
|--------|--------|-------------|----------------|
| Start | `start_screen.py` | Title screen with play button | World Map |
| World Map | `world_map.py` | 13 cities, character navigation | Any Level |
| Tangier | `levels/level_tangier.py` | Platformer — collect 10 artifacts | World Map (on win) |
| Fez | `levels/level_fez.py` | Memory card — match 8 pairs in 90s | World Map (on win/lose) |
| Cairo | `levels/level_cairo.py` | Platformer + moving platforms — collect 8 items | World Map (on win) |
| Damascus | `levels/level_damascus.py` | Falling items catcher — score 50+ | World Map (on win) |
| Timbuktu | `levels/level_timbuktu.py` | Platformer — collect 10 artifacts | World Map (on win) |

### Global UI Elements

| Element | Position | Description |
|---------|----------|-------------|
| Mute Button | Top-right (WIDTH-60, 60) | Toggles background music on/off |
| Back Button | (80, 50) | Returns to world map from any level |
| Mission Overlay | Center screen | Semi-transparent briefing before each level starts |

</details>

---

## 4. Level Design | تصميم المراحل

### Level 1: Kitchen Escape 🪟

| Field | Value |
|-------|-------|
| **Theme / Setting** | Kitchen — escaping from a countertop |
| **Level Type** | Platformer |
| **Background** | `level_1_bg.jpg` |
| **Background Music** | `background_music` |
| **Number of Items** | 1 (goal) |
| **Number of Platforms** | 7 |
| **Special Mechanics** | Gravity, jumping, platform collision |
| **Victory Condition** | Reach the empty goal at top-right |

#### Platforms

| Platform | Position (x, y) | Type |
|----------|-----------------|------|
| p1 | (200, 500) | Static |
| p2 | (400, 400) | Static |
| p3 | (200, 250) | Static |
| p4 | (500, 250) | Static |
| p5 | (650, 180) | Static |
| p6 | (750, 300) | Static |
| p7 | (950, 150) | Static |

---

### Level 2: Beach Run 🦅

| Field | Value |
|-------|-------|
| **Theme / Setting** | Beach — escaping birds to reach the ocean |
| **Level Type** | Survival / Dodger |
| **Background** | `level_2_bg.jpg` |
| **Background Music** | `background_music` |
| **Number of Items** | Unlimited (birds spawning) |
| **Number of Platforms** | N/A |
| **Special Mechanics** | Falling birds (spawn every 20 frames), 30-second survival timer, ocean wave goal appears after timer |
| **Victory Condition** | Survive 30 seconds, then reach the ocean wave |

#### Enemies

| Enemy | Image File | Speed | Notes |
|-------|------------|-------|-------|
| Bird | `bird` | 2 px/frame falling | Spawns every 20 frames at random x |

---

### Level 3: Sea Floor Dodging 🐢

| Field | Value |
|-------|-------|
| **Theme / Setting** | Sea floor — dodging pollution to reach a turtle |
| **Level Type** | Survival / Dodger |
| **Background** | `level_3_bg.jpg` |
| **Background Music** | `background_music` |
| **Number of Items** | Unlimited (trash spawning) |
| **Number of Platforms** | N/A |
| **Special Mechanics** | Falling trash (spawn every 10 frames), 10-second survival timer, turtle goal appears after timer |
| **Victory Condition** | Survive 10 seconds, then reach the sea turtle |

#### Hazards

| Hazard | Image File | Speed | Notes |
|--------|------------|-------|-------|
| Trash 1 | `trash_1` | 2 px/frame falling | Random selection |
| Trash 2 | `trash_2` | 2 px/frame falling | Random selection |
| Trash 3 | `trash_3` | 2 px/frame falling | Random selection |
| Trash 4 | `trash_4` | 2 px/frame falling | Random selection |

---

### Level 4: Shrimp Help 🦐

| Field | Value |
|-------|-------|
| **Theme / Setting** | Underwater rocks — helping an exhausted crab |
| **Level Type** | Platformer / Collection |
| **Background** | `level_4_bg.jpg` |
| **Background Music** | `background_music` |
| **Number of Items** | 17 (algae food) |
| **Number of Platforms** | 23 (using `empty_goal` as platform visuals) |
| **Special Mechanics** | Gravity, jumping, 60-second timer, collect all food before time runs out |
| **Victory Condition** | Collect all 17 algae food items within 60 seconds |

#### Items / Collectibles

| Item Name | Image File | Points | Special |
|-----------|------------|--------|---------|
| Algae Food | `crab_food_algae` | 1 (collect) | 17 total — collect all to win |

#### Platforms

| Platform | Position (x, y) | Type |
|----------|-----------------|------|
| p1 | (50, 425) | Static |
| p2 | (130, 425) | Static |
| p3 | (300, 435) | Static |
| p4 | (150, 255) | Static |
| p5 | (350, 265) | Static |
| p6 | (440, 350) | Static |
| p7 | (50, 125) | Static |
| p8 | (100, 125) | Static |
| p9 | (270, 155) | Static |
| p10 | (880, 495) | Static |
| p11 | (1070, 495) | Static |
| p12 | (1150, 495) | Static |
| p13 | (950, 400) | Static |
| p14 | (1010, 400) | Static |
| p15 | (695, 385) | Static |
| p16 | (910, 310) | Static |
| p17 | (1080, 295) | Static |
| p18 | (1150, 295) | Static |
| p19 | (720, 235) | Static |
| p20 | (765, 235) | Static |
| p21 | (990, 180) | Static |
| p22 | (1125, 150) | Static |
| p23 | (825, 105) | Static |

---

### Level 5: Predator Chase 🦈

| Field | Value |
|-------|-------|
| **Theme / Setting** | Ocean floor — evading a patrolling predator fish |
| **Level Type** | Survival / Platformer |
| **Background** | `level_5_bg.jpg` |
| **Background Music** | `background_music` |
| **Number of Items** | N/A |
| **Number of Platforms** | N/A (flat ground) |
| **Special Mechanics** | Gravity, jumping, patrolling evil fish (bounces left/right at speed 7), 45-second survival timer |
| **Victory Condition** | Survive 45 seconds without being caught |

#### Enemies

| Enemy | Image File | Speed | Notes |
|-------|------------|-------|-------|
| Evil Red Fish | `evil_red_fish_right` / `evil_red_fish_left` | 7 px/frame horizontal | Patrols left/right, flips sprite |

---

### Level 6: Home Sweet Home 🪸

| Field | Value |
|-------|-------|
| **Theme / Setting** | Protected coral sanctuary — reuniting with family |
| **Level Type** | Platformer |
| **Background** | `level_6_bg.png` |
| **Background Music** | `background_music` |
| **Number of Items** | N/A |
| **Number of Platforms** | N/A (flat ground) |
| **Special Mechanics** | Gravity, jumping, family reunion at end |
| **Victory Condition** | Reach your crab family at the right side |

#### Family Members

| Character | Image File | Position (x, y) | Notes |
|-----------|------------|-----------------|-------|
| Crab Family 1 | `crab_medium` | (WIDTH-200, HEIGHT-60) | Goal target |
| Crab Family 2 | `crab_medium` | (WIDTH-150, HEIGHT-80) | Goal target |

<details>
<summary>Example: Ibn Battota Game</summary>

### Level 1: Tangier

| Field | Value |
|-------|-------|
| **Theme / Setting** | Tangier, Morocco — coastal city |
| **Level Type** | Platformer |
| **Background** | `bg_tangier.png` |
| **Background Music** | `background_music` |
| **Number of Items** | 10 |
| **Number of Platforms** | 10 |
| **Special Mechanics** | Leaf particle effects, gravity, jumping |
| **Victory Condition** | Collect all 10 artifacts |

#### Items / Collectibles

| Item Name | Image File | Points | Special |
|-----------|------------|--------|---------|
| Prayer Mat | `items/collectibles/prayer_mat` | 1 | — |
| Leather Sandals | `items/collectibles/leather_sandals` | 1 | — |
| Compass | `items/collectibles/compass` | 1 | — |
| Holy Quran | `items/collectibles/holy_quran` | 1 | — |
| Woolen Djellaba | `items/collectibles/woolen_djellaba` | 1 | — |
| Water Skin | `items/collectibles/water_skin` | 1 | — |
| Silver Dirhams | `items/collectibles/silver_dirhams` | 1 | — |
| Oil Lamp | `items/collectibles/oil_lamp` | 1 | — |
| Travel Documents | `items/collectibles/travel_documents` | 1 | — |
| Inkwell and Kalam | `items/collectibles/inkwell_and_kalam` | 1 | — |

#### Platforms

| Platform | Position (x, y) | Type |
|----------|-----------------|------|
| p1 | (300, 600) | Static |
| p2 | (600, 550) | Static |
| p3 | (900, 500) | Static |
| p4 | (450, 450) | Static |
| p5 | (750, 400) | Static |
| p6 | (1100, 370) | Static |
| p7 | (450, 265) | Static |
| p8 | (950, 220) | Static |
| p9 | (1020, 630) | Static |
| p10 | (1220, 630) | Static |

---

### Level 2: Fez

| Field | Value |
|-------|-------|
| **Theme / Setting** | Fez, Morocco — city of knowledge |
| **Level Type** | Memory Card Game |
| **Background** | `bg_fez.png` |
| **Background Music** | `background_music` |
| **Number of Items** | 16 tiles (8 pairs) |
| **Number of Platforms** | N/A |
| **Special Mechanics** | Card flip, pair matching, 90-second timer, auto flip-back after 1s |
| **Victory Condition** | Match all 8 pairs before timer runs out |

#### Items / Collectibles (Symbols)

| Item Name | Image File | Points | Special |
|-----------|------------|--------|---------|
| Law | `items/fez_symbols/symbol_law` | 1 pair | — |
| Astronomy | `items/fez_symbols/symbol_astronomy` | 1 pair | — |
| Medicine | `items/fez_symbols/symbol_medicine` | 1 pair | — |
| Theology | `items/fez_symbols/symbol_theology` | 1 pair | — |
| Mathematics | `items/fez_symbols/symbol_mathematics` | 1 pair | — |
| Philosophy | `items/fez_symbols/symbol_philosophy` | 1 pair | — |
| Geography | `items/fez_symbols/symbol_geography` | 1 pair | — |
| Literature | `items/fez_symbols/symbol_literature` | 1 pair | — |

---

### Level 3: Cairo

| Field | Value |
|-------|-------|
| **Theme / Setting** | Cairo, Egypt — historic marketplace |
| **Level Type** | Platformer with Moving Platforms |
| **Background** | `bg_cairo.jpeg` |
| **Background Music** | `background_music` |
| **Number of Items** | 8 |
| **Number of Platforms** | 5 static + 3 moving |
| **Special Mechanics** | Moving platforms cycle every 50 frames, gravity, jumping |
| **Victory Condition** | Collect all 8 items |

#### Items / Collectibles

| Item Name | Image File | Points | Special |
|-----------|------------|--------|---------|
| Nile Water Glass | `items/cairo/nile_water_glass` | 1 | Cairo-specific |
| Medicine Bottle | `items/cairo/medicine_bottle` | 1 | Cairo-specific |
| Silver Dirhams | `items/collectibles/silver_dirhams` | 1 | Shared asset |
| Holy Quran | `items/collectibles/holy_quran` | 1 | Shared asset |
| Oil Lamp | `items/collectibles/oil_lamp` | 1 | Shared asset |
| Inkwell and Kalam | `items/collectibles/inkwell_and_kalam` | 1 | Shared asset |
| Osterlab | `items/cairo/osterlab` | 1 | Cairo-specific |
| Sugar Cane | `items/cairo/suger_cane` | 1 | Cairo-specific |

#### Moving Platforms

| Platform | Position (x, y) | Active When |
|----------|-----------------|-------------|
| mover_1 | (400, 550) | timer < 50 |
| mover_2 | (950, 450) | 50 ≤ timer < 100 |
| mover_3 | (750, 150) | 100 ≤ timer < 150 |

---

### Level 4: Damascus

| Field | Value |
|-------|-------|
| **Theme / Setting** | Damascus, Syria — bazaar under siege |
| **Level Type** | Falling Items Catcher |
| **Background** | `bg_damascus.jpg` |
| **Background Music** | `background_music` |
| **Number of Items** | Unlimited (spawning) |
| **Number of Platforms** | N/A |
| **Special Mechanics** | Items fall from sky, good (+1/+2/+5) and bad (-5/-10) items, spawn every 7 frames |
| **Victory Condition** | Reach score of 50 |

#### Items / Collectibles

| Item Name | Image File | Points | Special |
|-----------|------------|--------|---------|
| Holy Quran | `items/collectibles/holy_quran` | +1 | Good |
| Oil Lamp | `items/collectibles/oil_lamp` | +2 | Good |
| Silver Dirhams | `items/collectibles/silver_dirhams` | +5 | Good — rare |
| Scorpion | `items/damascus/scorpion` | -10 | Bad — avoid |
| Rock | `items/damascus/rock` | -5 | Bad — avoid |

</details>

---

## 5. Asset Inventory | جرد الموارد

### Images | الصور

| Category | File Name | Path | Used In |
|----------|-----------|------|---------|
| Background | `start-screen-background` | `images/` | Start Screen, Level Select |
| Background | `level_1_bg` | `images/` | Level 1 |
| Background | `level_2_bg` | `images/` | Level 2 |
| Background | `level_3_bg` | `images/` | Level 3 |
| Background | `level_4_bg` | `images/` | Level 4 |
| Background | `level_5_bg` | `images/` | Level 5 |
| Background | `level_6_bg` | `images/` | Level 6 |
| Character | `crab_small` | `images/` | Levels 1-3, 5, 6 (player) |
| Character | `crab_medium` | `images/` | Level 6 (family), Start Screen |
| Character | `shrimp` | `images/` | Level 4 (player) |
| UI Button | `start_btn` | `images/` | Start Screen, Level Select |
| UI Button | `start_btn_hover` | `images/` | Start Screen, Level Select (hover) |
| UI Icon | `music_on` | `images/` | Global mute button |
| UI Icon | `music_off` | `images/` | Global mute button |
| UI Logo | `logo` | `images/` | Start Screen |
| Fish | `clown_fish` | `images/` | Start Screen, Level Select (decoration) |
| Fish | `blue_fish` | `images/` | Start Screen, Level Select (decoration) |
| Fish | `pink_fish` | `images/` | Start Screen, Level Select (decoration) |
| Fish | `green_fish` | `images/` | Start Screen, Level Select (decoration) |
| Fish | `orange_fish` | `images/` | Start Screen, Level Select (decoration) |
| Fish | `gold_fish_small` | `images/` | Level Select (decoration) |
| Fish | `bubble_fish_small` | `images/` | Level Select (decoration) |
| Fish | `evil_red_fish_right` | `images/` | Level 5 (enemy, right) |
| Fish | `evil_red_fish_left` | `images/` | Level 5 (enemy, left) |
| Fish | `fish_1_small` | `images/` | (available asset) |
| Environment | `sea_star_small` | `images/` | Start Screen, Level Select (decoration) |
| Environment | `closed_clam_small` | `images/` | Start Screen, Level Select (decoration) |
| Environment | `opened_clam_small` | `images/` | Start Screen, Level Select (decoration) |
| Environment | `half_clam_small` | `images/` | Start Screen, Level Select (decoration) |
| Environment | `wave` | `images/` | Level 2 (goal) |
| Environment | `turtle` | `images/` | Level 3 (goal) |
| Hazard | `bird` | `images/` | Level 2 (enemy) |
| Hazard | `trash_1` | `images/` | Level 3 (pollution) |
| Hazard | `trash_2` | `images/` | Level 3 (pollution) |
| Hazard | `trash_3` | `images/` | Level 3 (pollution) |
| Hazard | `trash_4` | `images/` | Level 3 (pollution) |
| Collectible | `crab_food_algae` | `images/` | Level 4 (food items) |
| Platform | `platform_counter_small` | `images/` | Level 1 |
| Goal | `empty_goal` | `images/` | Level 1 (goal), Level 4 (platforms) |

### Audio | الصوتيات

| Type | File Name | Path | Purpose |
|------|-----------|------|---------|
| Background Music | `background_music` | `music/` | All screens |

### Total Asset Count | إجمالي الموارد

| Type | Count |
|------|-------|
| Backgrounds | 7 |
| Characters | 3 |
| UI Elements | 5 |
| Fish / Enemies | 9 |
| Environment | 5 |
| Hazards | 5 |
| Collectibles | 1 |
| Platforms / Goals | 2 |
| Music track s | 1 |
| **Total** | **38** |

<details>
<summary>Example: Ibn Battota Game</summary>

### Images

| Category | File Name | Path | Used In |
|----------|-----------|------|---------|
| Background | `start_screen_background` | `images/backgrounds/` | Start Screen |
| Background | `map` | `images/backgrounds/` | World Map |
| Background | `bg_tangier` | `images/backgrounds/` | Level 1 |
| Background | `bg_fez` | `images/backgrounds/` | Level 2 |
| Background | `bg_cairo` | `images/backgrounds/` | Level 3 |
| Background | `bg_damascus` | `images/backgrounds/` | Level 4 |
| Background | `bg_timbuktu` | `images/backgrounds/` | Level 5 |
| City Icon | `tangier`, `fez`, `cairo`, etc. (13) | `images/backgrounds/icons/` | World Map |
| Character | `character` | `images/characters/` | All platformer levels |
| UI Button | `start_btn` | `images/ui/` | Start Screen |
| UI Button | `back_btn` | `images/ui/` | All levels |
| UI Icon | `music_on`, `music_off` | `images/ui/` | Global mute |
| Platform | `platform` | `images/items/platforms/` | Tangier, Cairo |
| Collectible | `prayer_mat`, `compass`, etc. (10) | `images/items/collectibles/` | Tangier |
| Collectible | `nile_water_glass`, `medicine_bottle`, etc. (7) | `images/items/cairo/` | Cairo |
| Symbol | `tile_back` + 8 symbols | `images/items/fez_symbols/` | Fez |
| Hazard | `scorpion`, `rock` | `images/items/damascus/` | Damascus |
| Effect | `leaf`, `sand_particle` | `images/items/` | Tangier, others |
| Overlay | `mission_briefing`, `level_passed_seal` | `images/items/` | All levels |
| Text Image | `text_tangier`, `text_fez`, etc. (5) | `images/levels_texts/` | Mission overlays |

### Audio

| Type | File Name | Path | Purpose |
|------|-----------|------|---------|
| Background Music | `background_music` | `music/` | All screens |

### Total Asset Count

| Type | Count |
|------|-------|
| Backgrounds | 10 |
| City Icons | 13 |
| Characters | 1 |
| UI Elements | 4 |
| Collectibles | 25+ |
| Platforms | 1 |
| Particle Effects | 2 |
| Overlays | 2 |
| Text Images | 5 |
| Music track s | 1 |
| **Total** | **~64** |

</details>

---

## 6. Educational Content | المحتوى التعليمي

### Learning Objectives | أهداف التعلم

By the end of this project, the student will be able to:

1. Understand game loop architecture (draw → update → events)
2. Implement platformer physics (gravity, jumping, collision detection)
3. Manage multiple screen states with a state machine pattern
4. Design survival/dodger mechanics (spawning, timers, good vs bad elements)
5. Organize game assets and code into modular Python files
6. Understand marine biology concepts and ocean conservation themes

### Cultural / Historical Context | السياق الثقافي / التاريخي

| Topic | Description |
|-------|-------------|
| Marine Life | The game teaches about ocean creatures — crabs, shrimp, sea turtles, fish, and coral ecosystems |
| Ocean Conservation | Levels address real threats: pollution (Level 3), predators (Level 5), and habitat loss |
| Animal Behavior | Crabs migrating to the sea, shrimp as helper species, turtles as ocean guides |
| Food Chains | Understanding predator-prey relationships in ocean ecosystems |
| Coral Sanctuaries | Level 6 highlights the importance of protected marine areas |

### Curriculum Alignment | التوافق مع المنهج

| Skill Area | What the Student Practices |
|------------|---------------------------|
| Problem Solving | Breaking game logic into modular functions, debugging collision |
| Computational Thinking | State machines, conditional branching, timer systems |
| Creativity | Level design, visual storytelling, marine life theming |
| Collaboration | Code reviews between level designers |
| Technical Writing | Documenting game mechanics and assets |

<details>
<summary>Example: Ibn Battota Game</summary>

### Learning Objectatives

1. Understand game loop architecture (draw → update → events)
2. Implement platformer physics (gravity, jumping, collision)
3. Manage multiple screen states with a state machine pattern
4. Design memory matching game logic (pair track ing, timer, flip mechanics)
5. Create falling-item catcher mechanics (spawning, scoring, good vs bad)
6. Organize game assets and code into modular Python files

### Cultural / Historical Context

| Topic | Description |
|-------|-------------|
| Ibn Battota | 14th-century Moroccan explorer who traveled 75,000 miles across Africa, Asia, and Europe |
| Tangier | His birthplace — starting point of his journeys |
| Fez | Center of Islamic scholarship — levels teaches about 8 fields of knowledge |
| Cairo | Historic trade hub — marketplace-themed collectibles |
| Damascus | Ancient city — level themed around surviving a bustling bazaar |
| Timbuktu | Center of African trade and learning — final destination |

### Curriculum Alignment

| Skill Area | What the Student Practices |
|------------|---------------------------|
| Problem Solving | Breaking game logic into modular functions, debugging collision |
| Computational Thinking | State machines, conditional branching, timer systems |
| Creativity | Level design, visual storytelling, cultural theming |
| Collaboration | Code reviews between level designers |
| Technical Writing | Documenting game mechanics and assets |

</details>

---

## 7. Marketing Plan | خطة تسويقية

> **Short version** — for full marketing plans, use the main Afro-Asian template.

### Target Audience | الجمهور المستهدف

- **Primary**: Students ages 8-14 in coding/STEM programs
- **Secondary**: Teachers looking for ocean science-integrated coding projects
- **Tertiary**: Game development communities, Afro-Asian Tech Forum participants

### Platforms | المنصات

- Desktop (Windows) — primary development platform
- School computer labs

### Promotion Ideas | أفكار ترويجية

1. Present at Afro-Asian Tech Forum as an environmental education tool
2. Share gameplay demo video on YouTube
3. Demo at end-of-semester school exhibition
4. Submit to Robofest or similar student competition categories

<details>
<summary>Example: Ibn Battota Game</summary>

### Target Audience

- **Primary**: Students ages 10-16 in coding/STEM programs
- **Secondary**: Teachers looking for history-integrated coding projects
- **Tertiary**: Game development communities, Afro-Asian Tech Forum participants

### Platforms

- Desktop (Windows) — primary development platform
- School computer labs

### Promotion Ideas

1. Present at Afro-Asian Tech Forum as a cultural education tool
2. Share gameplay demo video on YouTube
3. Demo at end-of-semester school exhibition
4. Submit to Robofest or similar student competition categories

</details>

---

## 8. Student Worksheet | ورقة عمل الطالب

> **Instructions**: Copy this section into your own document and fill it in for YOUR game project.

---

### My Game Information | معلومات لعبتي

**Student Name**: ___________________________

**Game Title**: Crab Game

**Date**: ___________________________

---

#### What is your game about? | عن ماذا تتحدث لعبتك؟

An ocean-themed adventure game following a crab's journey through 6 chapters — from escaping a kitchen, dodging predators, avoiding pollution, helping other sea creatures, to reuniting with family. Each level teaches about marine life and ocean conservation.

#### What makes your game special? | ما الذي يجعل لعبتك مميزة؟

The game combines 6 different gameplay styles (platformer, survival, collection) into one cohesive ocean conservation story, raising awareness about real threats to marine ecosystems.

---

### My Game Mechanics | آليات لعبتي

**My game type** (circle one): Platformer / Puzzle / Catcher / Runner / Other: Multi-genre

**Controls in my game**:

| Key/Button | What it does |
|------------|-------------|
| Arrow Keys / A D | Move left/right |
| SPACE | Jump (platformer levels) |
| R | Restart level |
| ENTER | Return to level select |
| Mouse Click | Start / Select level / Mute |

**How does the player win?** | كيف يفوز اللاعب؟

Each level has a unique win condition: reach a goal, survive a timer, or collect all items.

**How does the player lose?** | كيف يخسر اللاعب？

Collide with hazards (birds, trash, predator fish) or run out of time.

---

### My Screens | شاشات لعبتي

| Screen Name | What happens here | How to get here |
|-------------|-------------------|-----------------|
| Start Screen | Title, animated fish, play button | Launch game |
| Level Select | Choose from 6 chapters | Click play |
| Kitchen Escape | Platformer to reach the goal | Click chapter 1 |
| Beach Run | Dodge birds for 30s | Click chapter 2 |
| Sea Floor Dodging | Dodge pollution for 10s | Click chapter 3 |
| Shrimp Help | Collect 17 algae items | Click chapter 4 |
| Predator Chase | Survive fish for 45s | Click chapter 5 |
| Home Sweet Home | Reach your family | Click chapter 6 |

---

### My Levels | مراحل لعبتي

| Level Name | Theme | What to do | Win condition |
|------------|-------|------------|---------------|
| Kitchen Escape | Kitchen | Jump across platforms | Reach the goal |
| Beach Run | Beach | Dodge falling birds | Survive 30s, reach wave |
| Sea Floor Dodging | Sea floor | Dodge falling trash | Survive 10s, reach turtle |
| Shrimp Help | Underwater rocks | Collect algae food | Gather all 17 items |
| Predator Chase | Ocean floor | Evade patrolling fish | Survive 45 seconds |
| Home Sweet Home | Coral sanctuary | Run to your family | Reach crab family |

---

### My Assets | موارد لعبتي

**Images I used**:

| Image | What it is used for |
|-------|---------------------|
| crab_small | Player character (most levels) |
| shrimp | Player character (Level 4) |
| crab_medium | Family members (Level 6) |
| level_1_bg through level_6_bg | Level backgrounds |
| start-screen-background | Menu background |
| platform_counter_small | Platforms (Level 1) |
| empty_goal | Goal/platforms (Levels 1, 4) |
| bird | Enemy (Level 2) |
| trash_1-4 | Hazards (Level 3) |
| crab_food_algae | Collectibles (Level 4) |
| evil_red_fish | Enemy (Level 5) |
| turtle | Goal (Level 3) |
| wave | Goal (Level 2) |
| Various fish | Decorations (menus) |
| start_btn | UI buttons |
| music_on/off | Mute toggle |

**Audio I used**:

| Sound | What it is used for |
|-------|---------------------|
| background_music | Background music for all screens |

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
