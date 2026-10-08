# What each Level needs. The Journey goes through these in order.
# "target" is how many points end the Level. Smaller = shorter Level.
# "fact" is the Fact card shown when the Level is cleared.

LEVELS = [
    {
        "name": "Level 1: Earth",
        "background": "backgrounds/earth",
        "target": 10,
        "fact": [
            "Earth's sky is crowded!",
            "Thousands of old satellites and rocket parts",
            "circle our planet at 28,000 km/h.",
            "Next stop: the asteroid belt."
        ],
    },
    {
        "name": "Level 2: Asteroid belt",
        "background": "backgrounds/belt",
        "target": 15,
        "fact": [
            "The asteroid belt sits between Mars and Jupiter.",
            "It holds millions of space rocks,",
            "but they are so far apart that ships",
            "can fly through safely.",
            "Next stop: Europa."
        ],
    },
    {
        "name": "Level 3: Europa",
        "background": "backgrounds/europa",
        "target": 12,
        "fact": [
            "Europa is a moon of Jupiter.",
            "Under its icy crust hides a salty ocean",
            "with about twice as much water",
            "as all of Earth's oceans!",
            "Next stop: Jupiter!"
        ],
    },
]

# Shown on the win screen after the last Level.
WIN_FACT = [
    "You reached Jupiter, the biggest planet!",
    "It is a gas giant with a famous Great Red Spot,",
    "a storm that has raged for hundreds of years."
]
