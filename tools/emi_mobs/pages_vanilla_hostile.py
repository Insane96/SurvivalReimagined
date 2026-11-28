SHARED = {
    "zombie.1": "Zombies come in different sizes. They climb ladders, lunge at you, sprint when close and bite back if you hit them without a weapon. Some carry a Fishing Rod to pull you in or Ender Pearls to reach you, some pick up other mobs and throw them at you, and some ride other mobs. Leaders call others to help.",
    "zombie.2": "They're better equipped under a full moon, under the open sky and deep underground. In caves some are miners that dig their way to you, more often the deeper you go.",
    "skeleton": "Skeletons shoot from a long range and back away if you get close, but aren't very accurate. They wear armor more often under a full moon and deep underground, and they come in different sizes. They climb ladders, some ride other mobs and leaders call others to help.",
}

M = "minecraft"
Z = ["zombie.1", "zombie.2"]
PAGES = {
    (M, "bogged"): (["Lives in Mangrove Swamps and comes out of the trial spawners of Trial Chambers and Adventure Dungeons. Some are found in Jungle Temples."], ["skeleton"]),
    (M, "breeze"): (["Only comes out of the trial spawners of Trial Chambers and Hellish Trials."], []),
    (M, "cave_spider"): (["Lives in Sulfur Caves and comes from the spawners in Mineshafts and Strongholds. Some of the Spiders in caves are Cave Spiders instead. It barely takes fall damage, sometimes rides other mobs and throws webs that slow you down and poison you."], []),
    (M, "creeper"): ([
        "Lives almost everywhere in the Overworld. Many can blow up through walls, some keep walking while lit and some circle around you. A few blast holes in walls to let other monsters in, and rarely one is Angry, with a much bigger explosion.",
        "Now and then one lights itself and launches at you. It doesn't light from falling, but another explosion can set it off.",
    ], []),
    (M, "drowned"): (["Lives in oceans, rivers and Dripstone Caves. It attacks during the day too and only starts burning in sunlight after a while. It jumps out of water, swims fast, grabs you to drag you underwater and steals your air when it hits. In oceans, half of them ride a Zombie Nautilus."], Z),
    (M, "enderman"): (["Lives almost everywhere, in all three dimensions. It gets angry even if you look at it from the side and climbs ladders. If you attack it from where it can't reach, it teleports. It can also teleport other monsters next to you."], []),
    (M, "endermite"): (["Sometimes comes out of a thrown Ender Pearl. Also found in Strongholds and in the spawners of some ruins."], []),
    (M, "evoker"): (["Lives in Woodland Mansions and joins raids. Its Vexes die with it. It opens doors and slowly heals over time."], []),
    (M, "guardian"): (["Comes out of the trial spawners of Ocean Monuments, and also lives deep down in deep oceans: those are smaller and much weaker. It deals magic damage."], []),
    (M, "husk"): (["Lives in Deserts and is found in Desert Temples. In Deserts it can ride a Camel Husk, with a Parched behind it."], Z),
    (M, "phantom"): (["Comes at night for players who are very tired and under the open sky, and also lives in some Nether biomes. Comes in random sizes, some very big. Its hits slow you down more and more and make you fall slowly, and it grabs you and carries you up in the air until you hit it back."], []),
    (M, "pillager"): (["Lives in Pillager Outposts and Woodland Mansions, and comes in patrols and raids. It shoots accurately from a long range, sometimes keeps its distance, opens doors and slowly heals over time."], []),
    (M, "ravager"): (["Comes with raids, and some are kept in Woodland Mansions. It slowly heals over time."], []),
    (M, "silverfish"): (["Hides in infested blocks in Strongholds and mountains, and comes from Stronghold spawners and Urns broken in caves. When hurt, it wakes up many Silverfish hiding nearby."], []),
    (M, "skeleton"): (["Lives almost everywhere in the Overworld and in some Nether biomes, but not in Nether Fortresses. Also comes from Dungeon spawners. Rarely, one has a Quiver."], ["skeleton"]),
    (M, "slime"): (["Lives underground in slime chunks and in swamps, and comes out of Urns broken in caves. It can be huge, jumps often and only hurts when it jumps at you or lands on you, not by touching you. It takes no fall damage. Small ones can be picked up with a Bucket, and a Slime killed on a Magma Block splits into Magma Cubes."], []),
    (M, "spider"): (["Lives almost everywhere in the Overworld and comes from Dungeon spawners. It barely takes fall damage and other monsters sometimes ride it. It throws webs that slow you down."], []),
    (M, "stray"): (["Lives in Snowy Plains and Ice Spikes, and comes out of the trial spawners of Trial Chambers and Adventure Dungeons."], ["skeleton"]),
    (M, "vex"): (["Summoned by Evokers, and dies with its Evoker. Also comes from spawners in Nether Sanctums. It goes down in a few hits."], []),
    (M, "vindicator"): (["Lives in Woodland Mansions and joins raids. It lunges at you, opens doors and slowly heals over time."], []),
    (M, "warden"): (["Summoned by the Sculk Shriekers of Ancient Cities, in the Deep Dark. Two warnings are enough to summon it, and they take a long time to wear off. It steps up full blocks, hears you from far away and its Darkness and Sonic Boom have a long reach."], []),
    (M, "witch"): (["Lives almost everywhere in the Overworld and in Swamp Huts, and joins raids. It throws many kinds of potions quickly and from far away, drinks potions often and throws helpful ones at nearby monsters. It sometimes keeps its distance and slowly heals over time."], []),
    (M, "zombie"): (["Lives almost everywhere in the Overworld and comes from Dungeon spawners. Some nights, a horde of Zombies comes for a player who has spent a long time in the same area."], Z),
    (M, "zombie_villager"): ([
        "Lives almost everywhere in the Overworld and fills the abandoned villages; a few are also in Igloos and Strongholds. Those in structures don't burn in sunlight. A Villager killed by a Zombie always turns into one.",
        "Curing them is the only way to get Villagers: give a Golden Carrot to one under Weakness. Once cured, it needs a day to recover before it trades or works. Cured Nitwits become normal Villagers that can take a job.",
    ], Z),
}
