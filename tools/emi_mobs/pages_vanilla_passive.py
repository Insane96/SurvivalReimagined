SHARED = {
    "breeds_alone": "It can't be bred by hand: adults fall in love on their own now and then, much more often for a while after you feed them, and less in crowded areas. Breeding is slower, can fail and sometimes gives twins.",
    "breeds": "Breeding is slower, can fail and sometimes gives twins.",
    # For mobs whose babies don't come from spawnChildFromBreeding (eggs, pregnancy): ISO's fail chance and twins
    # hook BabyEntitySpawnEvent, which they never fire.
    "breeds_alone.no_twins": "It can't be bred by hand: adults fall in love on their own now and then, much more often for a while after you feed them, and less in crowded areas.",
    "lifespan.very_short": "Its life is very short: it grows old and dies of old age. Feeding it a Poisonous Potato stops its aging.",
    "lifespan.short": "Its life is short: it grows old and dies of old age. Feeding it a Poisonous Potato stops its aging.",
    "lifespan.medium": "It grows old and dies of old age. Feeding it a Poisonous Potato stops its aging.",
    "lifespan.long": "Its life is long, but it grows old and dies of old age. Feeding it a Poisonous Potato stops its aging.",
    "lifespan.very_long": "Its life is very long, but it grows old and dies of old age. Feeding it a Poisonous Potato stops its aging.",
    "food": "Search #{food} in EMI to see what it eats.",
    "equine": "All of its kind have the same stats, so breeding doesn't give better ones. Once tamed, it doesn't wander far from where you dismount it.",
}

# EMI tag searches that "<mob>_food" would get wrong (#horse_food also finds #minecraft:zombie_horse_food).
FOOD_QUERY = {"horse": "minecraft:horse_food"}

M = "minecraft"
PAGES = {
    (M, "allay"): (["Found in the cages of Pillager Outposts, in Woodland Mansions and in Adventure Dungeons."], []),
    (M, "armadillo"): (["Lives in Badlands. It can't be brushed: collect the Scutes it sheds now and then, which drop as a block you can place and stack."], ["food", "breeds_alone"]),
    (M, "axolotl"): (["Lives in Lush Caves, and a few are kept in Woodland Mansions."], ["food", "breeds_alone"]),
    (M, "bat"): (["Lives in caves almost everywhere in the Overworld. Also flies out of Urns broken in caves."], []),
    (M, "bee"): (["Comes from Bee Nests on trees in Plains, Meadows, Flower and Birch Forests and Cherry Groves, and from Beehives. Bees stay closer to their hive."], ["food", "breeds", "lifespan.very_short"]),
    (M, "camel"): (["Lives in Deserts. A Chest can be put on it."], ["food", "breeds_alone"]),
    (M, "cat"): (["Tame an Ocelot to get one: it turns into a Cat. A black Cat also lives in Swamp Huts. Cats slowly heal over time."], ["food", "breeds_alone"]),
    (M, "chicken"): ([
        "Lives in plains, forests, taigas and jungles, but not in savannas or swamps. It lays eggs less often.",
        "Only Melon, Pumpkin and Torchflower Seeds feed and breed it: other seeds just make it follow you. Right-click one with an empty hand to carry it on your head: it slows your falls, but also your walking.",
    ], ["breeds", "lifespan.short"]),
    (M, "cod"): (["Lives in temperate and cold oceans. Comes in random sizes."], []),
    (M, "cow"): (["Lives in plains, forests, taigas and jungles, but not in savannas or swamps. It can only be milked once in a while."], ["food", "breeds_alone", "lifespan.long"]),
    (M, "dolphin"): (["Lives in temperate and warm oceans."], []),
    (M, "donkey"): (["Lives in Plains, Meadows and Savannas. Slower than a Horse and with a lower jump, but it can carry a Chest. It swims with you on its back. A tamed Donkey and a tamed Horse can have a Mule."], ["food", "equine", "breeds_alone"]),
    (M, "fox"): (["Lives in taigas and groves, and Naturalist adds it to more forests. It hunts Squirrels and slowly heals over time."], ["food", "breeds_alone"]),
    (M, "frog"): (["Lives in Swamps and Mangrove Swamps. A Frog that eats a Dragonfly drops Froglass of the Dragonfly's color."], ["food", "breeds_alone"]),
    (M, "glow_squid"): (["Lives in dark water almost everywhere in the Overworld, mostly in underwater caves. Comes in random sizes."], []),
    (M, "goat"): (["Lives on snowy slopes and peaks. It can only be milked once in a while."], ["food", "breeds_alone"]),
    (M, "horse"): (["Lives in Plains and Savannas. It steps up two blocks without jumping, swims with you on its back and can carry two players."], ["food", "equine", "breeds_alone", "lifespan.very_long"]),
    (M, "iron_golem"): ([
        "Build one with four Iron Blocks and a Carved Pumpkin. Some are caged in Pillager Outposts or stand guard in Woodland Mansions and Strongholds.",
        "It's very tough. It goes back to where it was made, and Villager smiths repair it. Some monsters attack it on sight.",
    ], []),
    (M, "llama"): (["Lives in Savanna Plateaus and Windswept Hills. Some Llamas carry more than others."], ["food", "equine", "breeds_alone", "lifespan.very_long"]),
    (M, "mooshroom"): (["Lives in Mushroom Fields. It can only be milked or stewed once in a while."], ["food", "breeds_alone", "lifespan.long"]),
    (M, "mule"): (["Born when a tamed Horse and a tamed Donkey fall in love near each other. Like the Donkey it can carry a Chest, and it swims with you on its back."], ["food", "equine"]),
    (M, "ocelot"): (["Lives in Jungles. Taming one turns it into a Cat. It slowly heals over time."], ["food", "breeds"]),
    (M, "panda"): (["Lives in Jungles and Bamboo Jungles."], ["food", "breeds_alone"]),
    (M, "parrot"): (["Lives in Jungles and comes in many colors. Tamed with its food; when two fall in love, one lays a Parrot Egg. It stays on your shoulder while you fly and through short falls: crouch to let it down. With a Parrot on each shoulder and a tamed Bird on your head, you can fly slowly. It slowly heals over time."], ["food", "breeds_alone", "lifespan.very_long"]),
    (M, "pig"): (["Lives in plains, taigas, jungles and Cherry Groves, but not in forests, savannas or swamps."], ["food", "breeds_alone", "lifespan.medium"]),
    (M, "polar_bear"): (["Lives in Snowy Plains, Ice Spikes and frozen oceans."], []),
    (M, "pufferfish"): (["Lives in warm and lukewarm oceans. Comes in random sizes."], []),
    (M, "rabbit"): (["Lives in Deserts, snowy biomes, taigas, Meadows and Cherry Groves, and Naturalist adds it to more forests. It takes less fall damage."], ["food", "breeds_alone", "lifespan.short"]),
    (M, "salmon"): (["Lives in rivers and cold oceans. Comes in random sizes."], []),
    (M, "sheep"): (["Lives in most grassy biomes, but not in savannas or swamps. Its wool grows back more slowly, and grown-up and old Sheep give more wool."], ["food", "breeds_alone", "lifespan.long"]),
    (M, "skeleton_horse"): (["Never found alone: lightning during a thunderstorm can be a trap that spawns four Skeleton Horsemen. The fastest mount, and it swims with you on its back."], ["equine"]),
    (M, "sniffer"): (["Only hatches from Sniffer Eggs, found by brushing Suspicious Sand in Warm Ocean Ruins and Jungle Temples."], ["food", "breeds_alone"]),
    (M, "snow_golem"): (["Build one with two Snow Blocks and a Carved Pumpkin. Its snowballs deal damage and freeze what they hit. It's a bit tougher, climbs ladders and is healed by snowballs."], []),
    (M, "squid"): (["Lives in rivers and oceans. Comes in random sizes."], []),
    (M, "tadpole"): (["Hatches from the Frogspawn that Frogs lay in water."], []),
    (M, "trader_llama"): (["Comes with the Wandering Trader. Some carry more than others."], ["food", "equine", "lifespan.very_long"]),
    (M, "tropical_fish"): (["Lives in warm oceans, Lush Caves and Mangrove Swamps. Comes in random sizes."], []),
    (M, "turtle"): (["Lives on Beaches. Its Scutes drop as a block you can place and stack."], ["food", "breeds_alone"]),
    (M, "villager"): ([
        "Villages are abandoned: Villagers only come from curing Zombie Villagers, apart from a few prisoners in Strongholds, Woodland Mansions and Igloos. They can't breed.",
        "They only sell, each trade for one Emerald. Prices go up with use and don't come back down, stock is restocked once a day and they keep their trades if they lose their job site. They follow you while you hold an Emerald.",
        "They eat to heal, call Iron Golems when in danger and smiths repair Iron Golems. They only fight back against players they really dislike.",
    ], []),
    (M, "wandering_trader"): (["Shows up near players now and then, with Trader Llamas. Sells plants, seeds and explorer maps, abandoned villages included, for one Emerald each, and buys a few items, like Music Discs, Hay Bales and Milk Buckets, for one Emerald."], []),
    (M, "wolf"): (["Lives in forests, taigas and groves. Wolves are faster and slowly heal over time, and tamed ones run to catch up with you. Pet one by crouching and right-clicking with an empty hand. Wolves left sitting for a while lie down. Wild Wolves hunt Deer and Moles, and dig Moles out of the ground."], ["food", "breeds_alone", "lifespan.very_long"]),
    (M, "zombie_horse"): (["Roams Plains, Snowy Plains and Savannas at night, and a tamed Skeleton Horse fed a lot of Rotten Flesh slowly turns into one. Tougher but slower than a Horse; it swims with you on its back."], ["food", "equine"]),
}
