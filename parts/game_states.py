# The shared game state. Every screen reads and changes these values.

# Which screen we are on: "INTRO", "PLAYING", "FACT_CARD", "GAME_OVER" or "WIN"
mode = "INTRO"

# Which Level we are in: 0 = Earth, 1 = Asteroid belt, 2 = Europa
level_number = 0

score = 0
high_score = 0

# Points earned in this Level only. The Level ends when this reaches its target.
level_points = 0

# If the player loses, "retry" puts the score back to what it was when the Level began.
level_start_score = 0

health = 3
paused = False
