# Phase 5: Vanilla Backport (1.2.2), mobs registered in the minecraft namespace. Sources: the decompiled jar
# (CamelHusk, CopperGolem, Creaking, HappyGhast, Nautilus, ZombieNautilus, Parched, SulfurCube and their spawn managers
# and mixins) and config/vanillabackport-common.toml. Item mechanics already on EMI pages (Harness, Dried Ghast,
# Nautilus Armor, Creaking Heart, Copper Golem Statue) are only summarized here.
# Shared texts (food, breeds_alone, skeleton) come from pages_vanilla_passive.py and pages_vanilla_hostile.py.

# The Zombie Nautilus eats what the Nautilus eats (same isFood), and has no tag of its own.
FOOD_QUERY = {"zombie_nautilus": "nautilus_food"}

M = "minecraft"
PAGES = {
    (M, "camel_husk"): (["Some of the Husks in Deserts ride one, with a Parched behind them. Once its riders are gone it can be saddled and ridden like a Camel, but it can't be bred. It despawns like a monster until you interact with it."], ["food"]),
    (M, "copper_golem"): ([
        "Build one by placing a Carved Pumpkin on a Block of Copper. It takes items from Copper Chests and puts them in nearby chests that already hold the same item, or in empty ones. Use it with an empty hand to take what it's carrying.",
        "It oxidizes over time, and once fully oxidized it can turn into a statue. Scrape it with an Axe to remove the oxidation, or wax it with a Honeycomb to stop it; lightning also removes some.",
    ], []),
    (M, "creaking"): (["Comes out of a Creaking Heart in the Pale Garden at night, and vanishes at sunrise. It only moves when no one is looking at it and can't be killed by attacking it: every hit makes Resin Clumps grow around its heart. Break the Creaking Heart to destroy it."], []),
    (M, "happy_ghast"): ([
        "Hatches as a Ghastling from a Dried Ghast left in water. Ghastlings stay close to players, and feeding them makes them grow up faster.",
        "Put a Harness on an adult to ride it with up to three friends: the first player steers, and it holds still while someone stands on top of it. It heals slowly, faster in the rain or in the clouds, and Speed and Slowness change how fast it flies. It can't be bred.",
    ], ["food"]),
    (M, "nautilus"): (["Lives in oceans, more often in temperate and warm ones than in cold ones. It hunts Pufferfish, charges at whoever hurts it and can't be poisoned. Pufferfish can tame it: a tamed Nautilus can be saddled and ridden underwater, wears armor, gives its rider Breath of the Nautilus and dashes forward on command. Wild ones despawn until you interact with them."], ["food", "breeds_alone"]),
    (M, "parched"): (["Lives in Deserts, and some ride a Camel Husk behind a Husk. It doesn't burn in sunlight, and its arrows give Weakness."], ["skeleton"]),
    (M, "sulfur_cube"): ([
        "Lives in Sulfur Caves and never attacks. Use a block on an adult to make it swallow it: it stops wandering, can be pushed around and leashed, and the block changes how it moves and bounces. Wood makes it bouncy, ice makes it slide, Wool makes it light, Honeycomb Blocks make it sticky and Magma Blocks make it hurt on touch.",
        "One holding TNT explodes when lit with Flint and Steel, set on fire or powered by redstone. Shear it to get the block back, or catch it in a Bucket. When killed it splits into two babies, and a baby fed its food grows up faster.",
    ], ["food"]),
    (M, "zombie_nautilus"): (["In oceans, half of the Drowned ride one; in warm oceans it's covered in coral. It burns in sunlight unless it wears armor, which wears out instead. Without a rider it can be tamed with Pufferfish, then saddled and ridden underwater like a Nautilus, but it can't be bred."], ["food"]),
}
