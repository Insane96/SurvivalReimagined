SHARED = {}

M = "minecraft"
PAGES = {
    (M, "blaze"): (["Lives in Nether Fortresses and other Nether structures, and in Infernal Dunes and Volcanic Deltas. Also comes from spawners and from the trial spawners of Hellish Trials. Its bursts of fireballs vary in length and speed, sometimes with two fireballs at a time."], []),
    (M, "elder_guardian"): (["Lives in Ocean Monuments, some waiting in place and some coming out of trial spawners. It has extra absorption hearts, heals a little with each hit and calls Elder Minions, weaker Guardians that swim faster. Every Elder Guardian killed makes the others nearby stronger: tougher, quicker to attack and to call minions."], []),
    (M, "ghast"): (["Lives in Nether Wastes, Soul Sand Valleys, Basalt Deltas and other open Nether biomes. It sometimes shoots several fireballs in a row, and some keep shooting even when they can't see you, faster, to blast through cover."], []),
    (M, "hoglin"): (["Lives in Crimson Forests and Bastion Remnants. Taken to the Overworld or the End, it turns into a Zoglin."], ["breeds_alone"]),
    (M, "magma_cube"): (["Lives in Basalt Deltas, Nether Wastes and many other Nether biomes, and in Nether Fortresses and other Nether structures, some from spawners. It can be bigger, jumps more often, moves fast in lava and only hurts when it jumps at you or lands on you, not by touching you. A Slime killed on a Magma Block splits into Magma Cubes."], []),
    (M, "piglin"): (["Lives in Crimson Forests, Nether Wastes and Ash Barrens, and in Bastion Remnants and other Nether structures. It climbs ladders, lunges at you and sprints when close."], []),
    (M, "piglin_brute"): (["Only found in Bastion Remnants and a few other Nether structures, some from spawners. It climbs ladders, lunges at you and sprints when close."], []),
    (M, "shulker"): (["Lives in End Cities and End Gate Fortresses. It's armored even while open, and once hurt it only opens partway while shooting. It shoots less often, but its Levitation is much stronger and shorter, and its bullets vanish when it dies."], []),
    (M, "strider"): (["Lives on the lava seas of almost every Nether biome."], ["breeds_alone"]),
    (M, "wither_skeleton"): (["Lives in Nether Fortresses and other Nether structures, and in Withered Forests. It climbs ladders, lunges at you, sprints when close and some are smaller. Some carry a Bow: they shoot from farther and more often, back away if you get close and their arrows wither you instead of setting you on fire."], []),
    (M, "zoglin"): (["A Hoglin taken to the Overworld or the End turns into one. Also comes from spawners in some ruins."], []),
    (M, "zombified_piglin"): (["Lives in Nether Wastes and Crimson Forests, and in Nether Fortresses and other Nether structures. It's never a baby and some are smaller. It climbs ladders, lunges at you, sprints when close and bites back if you hit it without a weapon. It sometimes picks up other mobs and throws them at you, and sometimes rides other mobs."], []),
}

# Bosses without a spawn egg (Vanilla Backport only ships textures, the items are not registered):
# not written by write_pages.py, waiting for a decision on which item gets the page.
NO_EGG = {
    (M, "ender_dragon"): ([
        "Lives in the End and can be respawned with four End Crystals on the exit portal. Respawning it with four Corrupted End Crystals, made with a Dragon Egg, summons the much stronger Corrupted Ender Dragon.",
        "It heals over time and from the End Crystals, more from Corrupted ones, and destroying a crystal while it's healing the Dragon hurts it. Crystals can't be set off by other explosions, more towers are caged and some hide a crystal inside. Once it's below half health, it can bring crystals back, together with Phantoms.",
        "Hitting it in flight hurts it more than when it's perched, and explosions hurt it less. Damage makes it angry, faster and more aggressive. It shoots acid balls that leave a lingering cloud, charges at you, calls Shulker minions and sometimes stops to charge a blast that throws you far away.",
    ], []),
    (M, "wither"): ([
        "Built from four Soul Sand or Soul Soil and three Wither Skeleton Skulls. Putting Corrupted Soul Sand in the middle, made with one, two or three Nether Stars, summons a stronger Wither: Armored, Summoner or Ultimate. The Ultimate Wither can only be summoned in the Nether.",
        "It heals over time and from the mobs it kills, fires bursts of skulls when hit, and charges at you once it's below half health or when it can't see you. It explodes when it dies, so get away.",
        "The Armored Wither is covered in armor, the Summoner calls Wither Minions, some with Bows, and heals much faster, and the Ultimate does all of this and hits harder. Their explosions break even blocks that resist the normal Wither.",
    ], []),
}
