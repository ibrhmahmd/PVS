# The shared game state. Every screen reads and changes these values.

# Which screen we are on: "TITLE", "PLAYING", "FACT_CARD", "GAME_OVER" or "WIN"
mode = "TITLE"

# Which Level we are in: 0 = Launch pad, 1 = Earth orbit, 2 = Asteroid belt, 3 = Europa
level_number = 0

score = 0
high_score = 0

# Points earned in this Level only.
level_points = 0

# Each Level sets this to True when it is finished. Then the Fact card shows.
level_cleared = False

# If the player loses, "retry" puts the score back to what it was when the Level began.
level_start_score = 0

health = 3
paused = False
