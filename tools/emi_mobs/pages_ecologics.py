# Phase 5: Ecologics (2.3.12). Sources: the decompiled jar (CoconutCrab, Penguin, Squirrel), its biome modifiers and
# config/ecologics-common.toml (coconutCrabSpawnChance 0.2, foxesAttackSquirrels on).
# Foods: isFood is the tempt tag for the Coconut Crab and the Penguin, Honeycomb for the Squirrel (Walnuts only tempt it
# and win its trust), so all three get a survivalreimagined:<mob>_food reference tag.
# Penguins override spawnChildFromBreeding (they get pregnant), so BabyEntitySpawnEvent never fires and ISO's
# breeding fail chance and twins don't apply: they get breeds_alone.no_twins (pages_vanilla_passive.py) instead.

E = "ecologics"
PAGES = {
    (E, "coconut_crab"): (["Comes out of some of the Coconuts that smash when falling from Coconut trees on Beaches. With a Coconut on its back it takes less damage and fights back when hit; badly hurt, the shell breaks into Coconut Slices and it runs from players instead. Give it a Coconut to put a new one on its back. It takes no fall damage."], ["food", "breeds_alone", "lifespan.short"]),
    (E, "penguin"): (["Lives in groups in Frozen Oceans, Frozen Rivers and Snowy Plains. It swims fast, holds its breath for a long time, slides on ice, hunts fish and picks up fish from the ground to eat. Standing near a big group of Penguins gives you Regeneration. After mating, a Penguin gives birth some time later, and a chick drops a Penguin Feather when it grows up."], ["food", "breeds_alone.no_twins", "lifespan.medium"]),
    (E, "squirrel"): (["Lives in Plains and climbs walls and trees. It runs from Foxes. Walnuts make it follow you and can win its trust: a trusting Squirrel picks up Saplings and plants them."], ["food", "breeds_alone", "lifespan.short"]),
}
