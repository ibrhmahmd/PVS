# What each Level needs. The Journey goes through these in order.
# "target" is how many points end a flying Level. Smaller = shorter Level.
#   (The Launch pad has no target: it ends when the Hero boards the Ship.)
# "story" is what happens next in the Hero's Mission, shown on the Fact card in cyan.
# "fact" is the science fact shown on the same Fact card in white.

# The Hero's Mission, shown on the Title screen.
TITLE_STORY = [
    "The Hero's mission: fly to Europa, Jupiter's icy moon,",
    "and find out if its hidden ocean could hold life."
]

LEVELS = [
    {
        "name": "Level 1: Launch pad",
        "background": "backgrounds/launch_pad",
        "story": [
            "3, 2, 1... liftoff! The Ship is up.",
            "Now dodge the space junk around Earth!"
        ],
        "fact": [
            "Rockets carry their own oxygen,",
            "because there is no air in space",
            "to burn their fuel."
        ],
    },
    {
        "name": "Level 2: Earth orbit",
        "background": "backgrounds/earth",
        "target": 10,
        "story": [
            "Phew, out of Earth's orbit!",
            "Next comes the asteroid belt.",
            "Shoot the rocks to clear the way!"
        ],
        "fact": [
            "Earth's sky is crowded!",
            "Thousands of old satellites and rocket parts",
            "circle our planet at 28,000 km/h."
        ],
    },
    {
        "name": "Level 3: Asteroid belt",
        "background": "backgrounds/belt",
        "target": 15,
        "story": [
            "Through the belt! Europa's geysers are",
            "blasting ice into space. Break the ice",
            "(two hits each) to fly close and scan its ocean!"
        ],
        "fact": [
            "The asteroid belt sits between Mars and Jupiter.",
            "It holds millions of space rocks,",
            "but they are so far apart that ships",
            "can fly through safely."
        ],
    },
    {
        "name": "Level 4: Europa",
        "background": "backgrounds/europa",
        "target": 12,
        "story": [
            "The scan worked: Europa's ocean is real!",
            "Now on to the giant planet itself."
        ],
        "fact": [
            "Under Europa's icy crust hides a salty ocean",
            "with about twice as much water",
            "as all of Earth's oceans!"
        ],
    },
]

# Shown on the win screen after the last Level.
WIN_STORY = [
    "Mission complete! The Hero scanned",
    "Europa's ocean and reached Jupiter."
]
WIN_FACT = [
    "Jupiter is the biggest planet. It is a gas giant",
    "with a famous Great Red Spot, a storm",
    "that has raged for hundreds of years."
]
