---
name: Neo-Arcade Narrative
colors:
  surface: '#0f131c'
  surface-dim: '#0f131c'
  surface-bright: '#353943'
  surface-container-lowest: '#0a0e17'
  surface-container-low: '#181b25'
  surface-container: '#1c1f29'
  surface-container-high: '#262a34'
  surface-container-highest: '#31353f'
  on-surface: '#dfe2ef'
  on-surface-variant: '#cbc3d7'
  inverse-surface: '#dfe2ef'
  inverse-on-surface: '#2c303a'
  outline: '#958ea0'
  outline-variant: '#494454'
  surface-tint: '#d0bcff'
  primary: '#d0bcff'
  on-primary: '#3c0091'
  primary-container: '#a078ff'
  on-primary-container: '#340080'
  inverse-primary: '#6d3bd7'
  secondary: '#4cd7f6'
  on-secondary: '#003640'
  secondary-container: '#03b5d3'
  on-secondary-container: '#00424e'
  tertiary: '#4edea3'
  on-tertiary: '#003824'
  tertiary-container: '#00a572'
  on-tertiary-container: '#00311f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e9ddff'
  primary-fixed-dim: '#d0bcff'
  on-primary-fixed: '#23005c'
  on-primary-fixed-variant: '#5516be'
  secondary-fixed: '#acedff'
  secondary-fixed-dim: '#4cd7f6'
  on-secondary-fixed: '#001f26'
  on-secondary-fixed-variant: '#004e5c'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#0f131c'
  on-background: '#dfe2ef'
  surface-variant: '#31353f'
typography:
  display-hero:
    fontFamily: Space Grotesk
    fontSize: 56px
    fontWeight: '700'
    lineHeight: 64px
    letterSpacing: -0.03em
  display-hero-mobile:
    fontFamily: Space Grotesk
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-xl-mobile:
    fontFamily: Space Grotesk
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-sm:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-badge:
    fontFamily: Space Grotesk
    fontSize: 13px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.08em
  label-code:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.04em
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 2rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system fuses golden-era 16-bit arcade nostalgia with contemporary neo-brutalism and heartfelt cinematic storytelling. It serves indie game developers, digital collectors, and passionate narrative-driven gamers who appreciate both tactile craft and polished digital execution.

The interface evokes the tactile thrill of dropping a physical coin into an arcade cabinet combined with the emotional warmth of a high-production hero's quest. Visually, the design emphasizes hard edges, high-contrast structural containment, glowing cathode-ray tube (CRT) light touches, and uncompromising clarity. Neo-brutalist heavy outlines and stark drop-shadow offsets collide with radiant cybernetic neon accents, creating an aesthetic that feels both rebellious and meticulously engineered.

## Colors

The palette operates strictly under a rich, high-contrast dark mode environment rooted in the aesthetic of a powered-on CRT display and plastic cartridge chassis.

- **Background Foundations**: Canvas base is Deep Void (`#090D16`), with surface elevation and container layers built upon Cartridge Black (`#0F172A`) and Chassis Charcoal (`#1E293B`).
- **Primary — Electric Violet (`#8B5CF6`)**: Expresses the magic, wonder, and core hero journey narrative points; used for top-level brand markers, primary action buttons, and focal rewards.
- **Secondary — Retro Cyan (`#06B6D4`)**: Denotes technology, cyberspace, and player stat interfaces; used for secondary controls, terminal indicators, and interactive highlights.
- **Tertiary — Neon Arcade Green (`#10B981`)**: Signals live states, achievements, health bars, inventory drops, and active player statuses.
- **Accent Coral (`#F97316`)**: Reserved for urgent alerts, critical quest logs, "Boss" encounters, and high-impact calls to action.
- **Structural White (`#FFFFFF`) & Grid Silver (`#94A3B8`)**: Pure crisp white borders generate uncompromising neo-brutalist boundary contrast, while neutral silvers handle subdued labels and structural grid lines.

## Typography

The type system prioritizes technical legibility paired with retro arcade attitude:

- **Display & Headings (Space Grotesk)**: Chosen for its sharp geometric terminals, idiosyncratic character angles, and futuristic tech heritage. When rendered in uppercase with tight tracking, it channels 16-bit arcade marquee headers without sacrificing readability across devices.
- **Body & Longform Narrative (Inter)**: Handles all studio chronicles, quest summaries, patch notes, and UI explanations. Inter provides maximum legibility at all densities, countering the bold visual weight of the neo-brutalist surfaces.
- **Labels, Badges, & Stats (Space Grotesk)**: Styled in full-caps or tight-spaced weights to deliver the crunch of terminal readouts, level trackers, and cartridge serial stamps.

## Layout & Spacing

The layout is grounded in a rigid 12-column neo-brutalist desktop structure (collapsing to 6 columns on tablet and 4 columns on mobile). 

- **Grid Alignment**: Every primary container aligns visibly to coordinate lines. Canvas boundaries sit against a persistent retro perspective grid pattern etched in faint midnight steel (`#1E293B` at 30% opacity).
- **Rhythm**: Element spacing follows a strict 8px base unit. Internal component spacing stays compact and modular, reinforcing the dense, information-rich feel of an arcade dashboard or HUD.
- **Form-Factor Scaling**:
  - **Desktop (1200px+)**: 12 columns, 24px (`1.5rem`) gutters, 32px to 64px section margins. Heavy asymmetrical card arrangements and dual-column quest log split-screens.
  - **Tablet (768px – 1199px)**: 6 columns, 24px gutters, 24px margins. Cards stack to single or double columns with edge-to-edge structural divider bars.
  - **Mobile (under 768px)**: 4 columns, 16px (`1rem`) gutters, 16px margins. Off-axis shadows shift to simplified 2px offsets to maximize usable viewport width.

## Elevation & Depth

Visual depth abandons standard blurred drop shadows in favor of neo-brutalist hard-edge planar offsets and CRT luminous radiance.

- **Hard-Offset Block Shadows**: Raised elements feature a solid 0-blur offset shadow using Deep Midnight (`#000000`) or saturated arcade tones (Electric Violet or Cyan). Default elevation uses `box-shadow: 4px 4px 0px 0px #000000`. Interactive hover states translate `-2px, -2px` with shadow expanding to `6px 6px 0px 0px`.
- **Structural Outlines**: All interactive containers, dialogs, and modules use a crisp 2px solid border (`#FFFFFF` on dark surfaces, or `#8B5CF6` / `#06B6D4` on highlighted states).
- **CRT Glow & Scanlines**: Key accent elements (interactive terminals, active health bars, quest markers) emit an exterior neon bloom (`box-shadow: 0 0 12px rgba(6, 182, 212, 0.4)`). A faint horizontal scanline pseudo-layer overlay (1px alternating bands with 3% opacity) sits over key media cards to emulate arcade glass.

## Shapes

The shape language is strictly uncompromising: `0` (Sharp corners throughout). 

- Every button, card, input field, dialogue overlay, and tab utilizes `border-radius: 0px`.
- To reference 16-bit arcade aesthetics, specialized elements utilize 45-degree chamfered "notch" cuts (`clip-path: polygon(...)`) on top-left and bottom-right corners (4px to 8px cuts) to emulate cartridge slots, level badges, and cybernetic inventory frames.

## Components

### Chunky Arcade Buttons
- **Primary**: Solid Electric Violet (`#8B5CF6`) fill, pure white 2px border, black bold label text or crisp white, with a hard `4px 4px 0px #000000` shadow. On active/pressed state, the button translates `+4px, +4px` and shadow collapses to `0px 0px`.
- **Secondary**: Solid Cartridge Black (`#0F172A`) fill, Cyan (`#06B6D4`) 2px border, Cyan text, with a Cyan `4px 4px 0px #06B6D4` hard shadow.
- **Boss / Action (CTA)**: Sunset Coral (`#F97316`) fill with white border and black drop offset.

### Level-Up & Feature Cards
- Constructed with Cartridge Black (`#0F172A`) surfaces, framed by a 2px solid white or chassis border.
- Header bar features a distinct contrasting title strip with pixel-corner badge tags and stat trackers.
- Hover states trigger an Electric Violet glow outline paired with the hard-edge shadow shift.

### Retro Pixel Badges & Tags
- Compact, full-caps Space Grotesk chips encased in a 1.5px solid neon border.
- Background uses a 10% tinted fill matching the respective category color (Green for "ONLINE", Coral for "HARDCORE", Cyan for "DEMO AVAILABLE").

### Form Inputs & Terminal Fields
- Dark Void (`#090D16`) inner fills with inset look or high-contrast 2px border in Chassis Charcoal.
- Focused state swaps border to glowing Retro Cyan (`#06B6D4`) with a monospaced-style blinking block cursor placeholder.

### Checkboxes & Radios
- Hard square geometry (`0px` radius).
- Unchecked: `#0F172A` background with 2px white border.
- Checked: `#10B981` (Arcade Green) solid fill featuring a stark geometric center square block instead of a soft checkmark.

### Quest Log Accordions & Stat HUDs
- Striped list rows partitioned by 1px solid `#1E293B` divider rules.
- Expansion tabs leverage arcade-style `[+]` and `[-]` monospace indicators rather than standard chevrons.