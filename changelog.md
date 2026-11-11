# Upcoming
* Known issue: unwaxed Lightning Rods don't attract lightning (Vanilla Backport bug). Wax them with a Honeycomb, waxed and oxidized ones work
* Fixed fog not getting denser in the rain and starting farther than intended: Cirrus overrode Insane's Survival Overhaul's fog distance (disabled Cirrus' "Fog uses horizon color")
* Removed Incubation's Nests: they only worked with Chickens, not with Naturalist's Ducks and Turkeys. They're no longer craftable or generated in the world
* Disabled Quark's Ender Watcher: Supplementaries' Voidman Head already emits a redstone signal when looked at
* Added EMI info pages for Supplementaries' blocks and items, and for the vanilla blocks and items changed by Amendments, explaining what they do. Also added pages for Bits and Balance's Glow Goo, Boatload's boats, Clayworks' Kiln and Pottery Table, Graves, Hang Gliders, Labels, the Saw and Straw Statues
* Updated Mods
  * Bits and Balance 2.5.2 -> 2.5.3
  * Collective 8.85 -> 8.86
  * CreativeCore 2.13.53 -> 2.13.54
  * Experience Tweaks 1.1.6.0 -> 1.1.6.1
    * Anvil repairs in EMI now respect the max repair (e.g. a Netherite Shovel repaired with a Diamond now shows half a repair instead of a full one)
    * Anvil repairs in EMI now have a tooltip showing how much durability each material repairs, the max repair and how many materials are needed
  * InsaneLib 2.5.3.0 -> 2.5.3.1
    * Fixed the Rope Arrow and Spectral Arrow (from Glow Goop) Fletching Table recipes missing when first loading a world, until `/reload`

# 4.9.1
* Removed EMI Loot
* Wither Skeletons no longer spawn with Wither Coated on their sword
* The saturation required for food to heal over time instead of instantly now accounts for the 40% saturation increase (4 -> 5.6), so foods heal as they did before it
* Prickly Pears now grow slower outside Deserts and without sunlight, like Cactus
* Reduced Prickly Pear nutrition (2.8 -> 2.1 health) and Cooked Prickly Pear nutrition (6 -> 5 health over time)
* Copper Horse Armor can now be recycled in the Blast Furnace into 5 Copper Ingots, like other Horse Armors
* Naturalist animals' meat drop chance reduced: 50% -> 40% (+20% per Looting level), like other animals
* Updated Mods
  * Bits and Balance 2.5.1 -> 2.5.2
  * Collective 8.84 -> 8.85
  * InsaneSurvivalOverhaul 5.15.0.0 -> 5.15.1.0
    * Netherite rebalanced to be closer to Diamond but much more durable
      * Netherite tools and weapons durability increased: 2437 -> 3650 (Axe 1950 -> 2920)
      * Netherite attack speed penalty reduced: 12.5% -> 5%, Netherite now deals slightly more DPS than Diamond
      * Netherite Armor durability increased: 429 / 624 / 585 / 507 -> 635 / 924 / 866 / 751
      * Netherite Armor points reduced: 4 / 7 / 6 / 3 -> 3.5 / 6 / 5.5 / 3 (20 -> 18 total)
      * Netherite Armor sprint slowdown reduced: 70% -> 60%
    * Quartz Arrows reworked: they now deal more damage (0.5 -> 2.5), but 40% of it is converted into Piercing Damage, instead of a bonus Piercing hit
      * Power and the bow's damage multiplier now affect the Piercing part too
      * Recipe is now more expensive: 1 Arrow + 1 Quartz -> 1 Quartz Arrow (was 2 Arrows + 1 Quartz -> 2)
    * Runed items can no longer be recycled in the Blast Furnace
    * Rotten Flesh drops are now converted to Cloth 25% of the time (was 35%), but Torches crafted with Cloth now give 4 instead of 3
    * Meat drop chance from Cows, Sheep, Mooshrooms, Pigs, Hoglins, Chickens and Rabbits reduced: 50% -> 40% (+20% per Looting level)
    * Elder animals now get the same bonuses as adults: they drop double loot and Elder Sheep drop double wool when sheared
    * Leashed mobs are now pulled towards the holder from 10 blocks instead of 6
    * Wardens, Elder Guardians and bosses that kill a player no longer get the Player Killer bounty
    * The Main Bed info message is no longer displayed if you already have a main bed set
    * Fixed babies being considered elders
  * RuneEnchanting 1.4.4.0 -> 1.4.5.0
    * Atmospheric has been split into two Runes, existing Atmospheric Runes become Sunlit
      * Sunlit: gain mining and brushing speed under the sun. Can be applied to mining tools, shears and brushes
      * Moonlit: gain attack speed under the moon light. Can be applied to weapons
      * Removed the reduced durability consumption in the rain
    * Increased Thorns damage chance (25% -> 35%)
    * Charged Jump now reaches Jump Boost X in 2.5 seconds (was Jump Boost VIII in 3.2 seconds)
    * Dwarfing now gives the max bonus mining speed in the Nether
    * Fixed bows and crossbows with Multishot starting to draw/load with fewer arrows than required, then not shooting/loading anything. They now can't be used at all without enough arrows

# 4.9.0
* Added Progressive Bosses
* Added EMI Loot
* Added JEI
  * This makes Kiln recipes show up in EMI
* Removed Beautiful Potions
* Removed Bits and Balance's Kiln recipe and its EMI category, as Clayworks already adds a Kiln
* Leaders now have a 25% chance to drop their Banner when killed by a player (previously guaranteed)
* Sculk Shriekers are now extremely hard to break and immune to explosions
* Increased Maple Cream Pie saturation (5.04 -> 20.16, now eaten in 4.08 seconds)
* Advancements with multiple criteria now list the ones still missing instead of the ones already obtained
* Fixed Haste and Mining Fatigue descriptions mentioning attack speed, which they don't affect
* Updated Mods
  * Bits and Balance 2.5.0 -> 2.5.1
    * Wood can no longer be cut in the Stonecutter, use the Sawmill instead
  * Collective 8.82 -> 8.84
  * Enhanced AI 4.2.7.1 -> 4.2.7.2
  * InsaneLib 2.5.2.0 -> 2.5.3.0
  * InsaneSurvivalOverhaul 5.14.4.0 -> 5.15.0.0
    * Reworked the Beacon: the vanilla recipe now gives a new Beacon, with a single selectable effect and a level for it
      * 15 effects available: Speed, Jump Boost, Block Reach, Haste, Fire Resistance, Vigour, Invisibility, Strength, Resistance, Night Vision, Slow Falling, Regeneration, Regenerating Absorption, Entity Reach and Ghostly
      * Each effect level requires a certain number of pyramid layers, up to 4 (e.g. Strength I and II require 3 layers, Strength III requires 4)
      * Range is 16 blocks + a bonus based on the blocks of the pyramid, reduced by higher effect levels, up to 181 blocks with a full Netherite pyramid
      * Also affects tamed animals
      * If the pyramid gets smaller, the effect level is lowered, or the effect is suspended if the pyramid is too short. The selection is kept and works again once the pyramid is rebuilt
      * No longer requires payments
    * Golden Carrots can no longer be fed to Horses, Donkeys and Mules and no longer attract them, which are now attracted by Apples and Carrots
    * Auto breeding chance now decreases gradually when there are more than 10 animals of the same type within 16 blocks, stopping at 16 (previously full chance until stopping at 18)
    * Fixed Air Affinity making mining off ground faster than on ground
    * Fixed Glow Blocks and their alignment HUD disappearing from some angles when behind walls
    * Fixed Regenerating Absorption effect having no name and icon
  * Moonlight 3.8.2 -> 3.8.3
  * RuneEnchanting 1.4.3.0 -> 1.4.4.0
    * Brushes now have 2 sockets and can get durability Runes, Reach and Telekinesis (sends the uncovered item directly to your inventory)
    * Efficiency (+100%), Atmospheric (up to +150% under the sun) and Curse of Inefficiency (-50%) now affect brushing speed
    * Sculk Catalysts (50%) and Sculk (0.1%) now have a chance to drop a random Rune, Curses included, when broken without Silk Touch
    * Runes in item tooltips are now sorted by name, with Curses first
  * Shields+ 2.3.0.2 -> 2.3.1.0
    * Removed the Ablaze Rune, the Flame Rune now applies to Shields and does the same. Existing Ablaze Runes are converted to Flame

# 4.8.2
* Mobs (zombies and leaders) now spawn with ISO's Copper equipment instead of the Vanilla Backport's one, that couldn't be smelted
* Mobs from Spawners and Trial Spawners can no longer be Leaders, and mobs from Trial Spawners can no longer be Miners
* Angry Creepers no longer explode on death
* Drowned now have a 7.5% chance (+1.25% per Looting level) to drop a Trident Fragment
* Tridents are now repaired with Turtle Scutes (up to 25%) instead of Prismarine Shards and Crystals, which are no longer obtainable
* Tridents can also be repaired with Trident Fragments, each one repairs 50%
* Naturalist animals' meat drops now follow the new livestock rules: 50% chance (+20% per Looting level) to drop 1 meat, or 1-3 for Boars, Elephants, Rhinos and Mammoths (previously guaranteed or 0-2, without Looting)
* Maple Cream Pie is now the same as Pumpkin Pie (saturation 12.6 -> 5.04, eaten in 1.92 seconds) and no longer gives Haste
* Lowered Tropical Stew nutrition
* Fixed conflicting Cake recipes, one of which crafted a Maple Cream Pie
* Fixed Maple Cream Pie being named Cake
* Updated Mods
  * Collective 8.80 -> 8.82
  * CreativeCore 2.13.52 -> 2.13.53
  * Ecologics 2.3.10 -> 2.3.10 (hotfix)
  * Enhanced AI 4.2.7.0 -> 4.2.7.1
    * Fixed attacked animals not making nearby animals panic
  * Every Compat 2.11.56 -> 2.11.57
    * Improved the textures of Storage Drawers' Drawers for modded woods
  * Incendium: Biomes Only 3.1.0 -> 3.2.0
  * InsaneLib 2.5.1.0 -> 2.5.2.0
  * InsaneSurvivalOverhaul 5.14.3.0 -> 5.14.4.0
    * Camels, Sniffers and Armadillos can no longer be bred manually, like other animals
    * When an animal falls in love on its own, the closest animal of the same type within 8 blocks also falls in love. Auto breeding chance lowered to compensate: 2 animals take ~1 hour on average, 10 animals ~12.5 minutes
    * Fixed Looting lowering the meat, fish and Rabbit Foot drop chance instead of increasing it
    * Cows, Mooshrooms, Sheep, Chickens and Rabbits now have a 50% chance (+20% per Looting level) to drop meat (previously 30%, Rabbits 60%)
    * Pigs and Hoglins now have a 50% chance (+20% per Looting level) to drop 1-3 Porkchops
    * Chickens drop 1-2 Feathers instead of 1-3
    * Mooshrooms can be stewed or milked every 60 minutes instead of 20
    * Well Fed animals no longer produce as fast: Chickens lay eggs every ~11 minutes instead of ~7.5, milking cooldown is reduced by 25%
    * Young animals now produce like Elders (+20% egg laying time, +50% milking cooldown)
    * Pumpkin Pie, Apple Pie, Spider Eye and Honey Bottle now give less saturation, and Pies are eaten faster
    * Fixed Honey Bottles not having lowered nutrition
    * Fixed Shortbows not usable as furnace fuel
    * Fixed EMI showing Recycling recipes' output without the output multiplier
    * Fixed Hoglins, Goats, Axolotls and Frogs still being breedable manually
    * Fixed dropped Netherite equipment not being immune to fire, lava and explosions
  * Moonlight 3.8.1 -> 3.8.2
  * OctoLib 0.6.2 -> 0.6.3

# 4.8.1
* Removed Archeological
* Removed Quark's Golden Apple Crate, as Golden Apples are removed
* Re-enabled Quark's Rotating Bundles
* Bundles can no longer be dyed, as colored Bundles aren't compatible with Quark's Rotating Bundles
* Halved the Arrow bonus damage of Runes
  * Sharpness 100% -> 50%
  * Bane of Hissing, Impaling, Water Coolant, Smite and Bane of Noses 200% -> 100%
  * Rage and Fire Surge (max) 300% -> 150%
* Efficiency Rune now gives +100% Mining Speed, instead of +80% and +2.5
* Enduring Rune no longer gives +80 flat Durability, only the +200%
* Reduced the Damage Reduction of Blast, Fire, Projectile, Melee and Magic Protection Runes from 40% to 30%
* Parched now have Enhanced AI's skeleton behaviours and the same drops as other Skeletons
* Nautiluses can no longer be bred manually, like other animals
* Pale Oak and Poplar now follow the same rules as other woods: Buttons and Pressure Plates need Redstone, leaves no longer drop Saplings, which are crafted from leaves with Shears
* Hoes now also harvest Bushes, Firefly Bushes and Dry Grass
* Dispenser Minecarts now stack to 16 like other Minecarts
* Copper and Netherite Horse Armor and Nautilus Armor now stack to 16 like other Horse Armor
* Maple Cookies now give Energy Boost
* Tropical Stew now uses the drinking animation
* Speaker Blocks now require an Amethyst Shard instead of an Emerald
* Tridents crafted with Trident Fragments now require Turtle Scutes instead of Prismarine Shards, which are no longer obtainable
* Redstone Randomizers now require a Nautilus Shell instead of a Prismarine Crystal, which is no longer obtainable
* Removed Supplementaries' Bed recipe from Feather Blocks, as it skipped Cloth and Wool
* Bones can no longer be smelted into Bone Meal, as it gave more than crafting
* Shortbows can now be found in Vaults alongside Bows and Crossbows
* Normal Vaults can now also contain Diamond, Ice, Quartz and Explosive Arrows or a Quiver
* Philip's Ruins' chests with fixed Enchanted Books, enchanted gear, Emeralds or Golden Apples now use loot tables, so they give Runes instead
* Nerfed the loot of Philip's Ruins' surface structures: Ancient Ruins, Ancient Towers and Level Three Ruins now use the low-tier loot instead of diamonds and diamond gear
* Philip's Ruins' Ocean Ruins and Ocean Fortress chests no longer contain diamond gear (Diamonds are still there)
* Fixed 6 empty chests in Philip's Ruins' Field Stone Ruins and Level Two Ruins
* Updated Mods
  * Collective 8.75 -> 8.80
  * Ecologics 2.3.9 -> 2.3.10
    * Dispensers now work with Spiles and Maple Sap Cauldrons
    * Spiles and Maple Sap Cauldrons now output a comparator signal
    * Fixed Hanging Coconut dupe
  * Enhanced AI 4.2.6.0 -> 4.2.7.0
  * InsaneSurvivalOverhaul 5.14.2.0 -> 5.14.3.0
    * Increased Diamond Armor durability (Helmet / Chestplate / Leggings / Boots): 209 / 304 / 285 / 247 -> 363 / 528 / 495 / 429
    * Increased Netherite Armor durability: 204 / 296 / 278 / 241 -> 429 / 624 / 585 / 507
    * Decreased Golden Armor durability: 72 / 104 / 98 / 85 -> 44 / 64 / 60 / 52
    * Increased Golden tools and weapons durability from 64 to 102 (Axe from 51 to 82)
    * Shortbows can now have the same Runes as Bows
    * Minecarts with entities and Chest Minecarts now force load chunks only while moving, fixing RAM usage growing while exploring (e.g. because of Mineshafts' Chest Minecarts)
    * Fixed Bows feature overriding the bonus damage of Runes on Arrows
    * Fixed Ominous Trial Vaults never dropping the Divine Fragment (now 80% chance)
  * Item Block Info HUD 1.1.1.1 -> 1.1.1.2
  * Moonlight 3.7.2 -> 3.8.1
  * Particle Rain 4.0.2 -> 4.0.3
    * Fixed rain being less dense than it should
    * Fixed wind sound and sandstorms appearing outside the Overworld
    * Reversed wind direction to match the clouds
  * RuneEnchanting 1.4.0.1 -> 1.4.3.0
    * Runes can now be placed in Chiseled Bookshelves
    * Enchanted Books in Chiseled Bookshelves generated in structures are now replaced with random Runes
    * Protection and Feather Falling Rune tooltips now state that their Damage Reduction is capped at 80% combined
    * Fixed weapon Runes working when hitting in melee with Bows and Crossbows
    * Fixed Bastions favoring Swift Sneak and Ancient Cities favoring Soul Speed
    * Fixed Melee Protection also reducing damage not caused by melee attacks, such as fall, lava, falling blocks and Creeper explosions
    * Fixed Ominous Trial Vaults not favoring their specific Runes
  * Sawmill 1.8.1 -> 1.9.0
  * Shields+ 2.3.0.1 -> 2.3.0.2
    * Wooden Shields can now be used as furnace fuel

# 4.8.0
* Added Hellish Trials
* Added Moog's Nether Structures
* Removed Eternal Nether
* Brushes now have 1 Rune socket and can have the Luck Rune, which increases brushing rewards (except Emeralds)
* Increased the search radius of Explorer Maps from 75 to 600 chunks
* Naturalist mobs no longer get Enhanced AI's movement and swim speed bonus
* Re-enabled the Crafter and the Observer
* Disabled Vanilla Backport's Locator Bar
* Disabled Vanilla Backport's new Bundle interface
* Philip's Ruins' Ancient Crypt now has low-tier loot instead of diamond gear
* Added missing effect descriptions (Returning, Displacement, Resurfacing, Bioluminescence, Antivenom, Breath of the Nautilus, Resilience)
* Updated Mods
  * Bits and Balance 2.4.3 -> 2.5.0
    * Reworked brushing loot, which now gives more Runes
  * Collective 8.73 -> 8.75
  * Ecologics 2.3.8 -> 2.3.9
    * Added Maple trees, with Sap, Syrup and a full wood set
  * InsaneSurvivalOverhaul 5.14.0.0-beta -> 5.14.2.0
    * Saplings now require Shears in the recipe
    * Spectral Arrows in the Fletching Table now take 2 Arrows and 1 Glowstone Dust and make 2 Spectral Arrows
    * Added Potion of Recall

# 4.7.0
* Added Ecologics
* Added Naturalist
* Added Every Compat and Stone Zone
* Added a Desert Ruins Map, found in Abandoned Camp chests (15% chance)
* Spectral Arrows and Rope Arrows are now crafted in the Fletching Table; Rope Arrows can still be refilled in the crafting grid
* You are no longer slowed down in snow
* Doubled the chance of Enhanced AI mobs blocking with a shield
* Enabled Vanilla Backport's modern bundle interface (scroll to select the item to take out); disabled Quark's Rotating Bundles as it conflicts with it
* Bundles can be dyed again
* Disabled Quark's Crabs
* Fried Eggs can no longer be cooked in furnaces
* Fixed recycling tools giving full output
* Fixed Dungeons and Taverns books in Desert and Jungle Ruins loot being plain or empty instead of giving a rune
* Updated Mods
  * Amendments 2.2.5 -> 2.2.7
  * Balm 21.0.66 -> 21.0.67
  * Cirrus 1.4.1 -> 1.4.2
  * Collective 8.69 -> 8.73
  * CreativeCore 2.13.51 -> 2.13.52
  * Fancy World Animations 1.2.31 -> 1.3.4
  * InsaneLib 2.5.0.4-alpha -> 2.5.1.0
    * Fixed right-clicking items into Sacks in the inventory causing them to split by 99
    * Endermen can no longer teleport inside full blocks that can be passed through (e.g. cobwebs, powder snow), where they could get stuck
    * Fixed an error spamming the server log when a server list ping fails

# 4.6.0
* Removed Inventory Totem
* Removed Underlay
* Enhanced AI Leaders now wear a full trimmed copper, chainmail, golden, iron or (rarely) diamond armor and a banner on their head; reinforcements chance now reaches 100% at 3 damage instead of 1
* Repair kits can now repair items up to 100% instead of 80%
* Hang Glider durability consumption doubled (1 every 5 ticks instead of 10) and durability halved (818 -> 409)
* Disabled Quark's Compasses Work Everywhere, compasses spin randomly in the Nether and End again
* Explosive rune delay reduced from 5 to 3 seconds
* Supplementaries' Blast Armor Trim can now be duplicated with 1 diamond, like the vanilla ones
* Removed duplicate Name Tag recipes, only the vanilla-like one (paper + any nugget) is kept
* Fixed mobs spawning with Vanilla Backport copper tools instead of Insane's Survival Overhaul ones
* Updated mods
  * Amendments 2.1.11 -> 2.2.5
    * Walls, fences and panes now all connect to each other
    * Added a smooth hotbar slot animation
    * Axolotl buckets show the color of the axolotl inside
    * Following pets teleport with you instantly when you teleport
  * Ambient Sounds 6.3.10 -> 6.3.11
  * Collective 8.58 -> 8.69
  * Enhanced AI 4.2.4.0 -> 4.2.6.0
    * Shielding now works like vanilla shields: only damage coming from the front can be blocked, but projectiles and explosions can be blocked too
    * Fixed skeletons randomly strolling away while shooting
    * Fixed polar bears attacking without cubs nearby, witches no longer healing raiders and foxes attacking anything that hurt something
    * Fixed leaders spawning far less reinforcements than intended
    * Fixed Actual Blindness reducing mobs follow range way more than intended
    * Fixed miner mobs being unable to mine blocks that don't need a specific tool (e.g. glass, wool)
  * Experience Tweaks 1.1.5.1 -> 1.1.6.0
  * InsaneLib 2.4.33.2 -> 2.5.0.4-alpha
    * Mods now have a config screen in the Mods list
    * Fixed falling blocks getting stuck forever on top of slime blocks
  * InsaneSurvivalOverhaul 5.13.0.0 -> 5.14.0.0-beta
    * Blocks in the Nether are now 1.5x harder to break
    * Iron, golden and copper items without durability (bars, chains, lanterns, buckets, doors, hoppers, minecarts, rails, anvils, ...) can now be recycled in the Blast Furnace, giving back 75% of the materials
    * Horse Armors can now be recycled into 5 ingots (or diamonds) instead of 1 nugget
    * Iron, golden and chainmail equipment can no longer be smelted into 1 nugget, recycle them in the Blast Furnace instead
    * Golden Armor total armor increased from 5 to 9, Chainmail Armor decreased from 15.5 to 13
    * The delay between breaking blocks is now based on the actual mining speed against the broken block (Efficiency, Haste, etc. included)
    * Thrown tridents damage is now based on the trident attack damage
    * Fixed health regen reduction while in combat not working properly
    * Fixed Stuck Arrows dropping arrows 100 times less than intended, any arrow type now counts
    * Fixed items picked up by mobs (e.g. lost by players) no longer being guaranteed to drop after their chunk was reloaded
    * Fixed Better Hardcore Death deleting the block at the player's feet
    * Fixed tired players being able to sleep with monsters nearby and Tired levels being gained too early
    * Fixed chunks force loaded by minecarts staying loaded forever after a server restart
    * Fixed repair kits consuming other items in the crafting grid
    * Lots of other fixes
  * Mobs Properties Randomness 6.1.10.0 -> 6.2.1.0
  * ModernFix 5.27.26 -> 5.27.27
  * No Hunger 2.1.0.1 -> 2.1.1.0
    * Eating a food that heals over time no longer replaces a higher health left to regenerate
    * Fixed the food tooltip showing half of the real overtime regeneration duration, now also takes into account Well Fed and Curse of Malnutrition
    * Fixed the overtime regen overlay not showing after logging in, respawning or changing dimension
  * Platform 1.4 -> 1.4.2
  * Puzzles Lib 21.1.64 -> 21.1.66
  * Quark 4.1-487 -> 4.1-488
    * Forgotten Hat no longer gives 1 armor
    * Foxhounds now also sleep on smokers and blast furnaces
    * Pumpkins and skulls can now be equipped with Expanded Item Interactions
  * RuneEnchanting 1.3.2.3 -> 1.4.0.0
    * Bows and crossbows now share all their runes (e.g. Multishot on bows, Infinity on crossbows); Quick Charge and Curse of Slow Charge now also affect bows
    * Melee weapon runes (Sharpness, Smite, Fire Surge, Explosive, ...) can now be applied to bows and crossbows and work on the arrows shot
    * Power has been removed and merged into Sharpness
    * Reworked Electrocution: dealing damage charges the weapon, after 20 damage the hit discharges on the target and the 4 nearest entities
    * Decreased Leather armor sockets
    * Curse of Blood Pact and Blood-fueled damage now bypasses armor
    * Items with more runes than sockets have their runes inactive until removed with a grindstone
    * Fixed the bonus damage from runes such as Hunter being ignored
    * Fixed runes on weapons and tools working while held in the offhand
    * Lots of other fixes
  * Stamina 2.0.0.4 -> 2.1.0.0
    * Stamina consumed by jumping is now affected by the out of combat multiplier, like sprinting
    * Fixed attacking other players not counting as being in combat
    * Fixed stamina not being locked when health dropped below the threshold while sprinting
  * Tiny Takeover Backport 1.6.3 -> 1.8.2
  * Vanilla Backport 1.1.7.10 -> 1.2.2
    * Added features from the Copper Age drop (Copper Golems, Copper Chests, copper lanterns, chains and bars, ...)
      * Copper Chains cost 3 copper nuggets, like Iron Chains
      * Copper Chests, Bars, Chains and Lanterns can be recycled in the Blast Furnace
    * Added features from the Mounts of Mayhem drop (Nautiluses, Zombie Horses, Camel Husks, Parched skeletons, ...)
    * Added the Dappled Forest from the Wilderness Bound drop
    * Thrown Ender Pearls now load chunks while traveling
  * Vibrant Parrots 21.1.0 -> 21.1.1

# 4.5.9
* Enhanced AI: TNT-like creepers chance reduced from 25% to 5%
* Updated mods
  * Collective 8.56 -> 8.58
  * InsaneSurvivalOverhaul 5.12.6.0 -> 5.13.0.0
    * Firework Rockets recipes now output 5 instead of 3 and Firework Stars 2 instead of 1
    * Firework Stars can now be added to already crafted Firework Rockets
    * Lava now smelts 256 items instead of 100
    * Chickens can no longer auto breed
    * Fixed Shulker Boxes losing auto pick-up when placed and broken
    * Fixed zombies replacing zombie villagers keeping vanilla enchantments instead of having them converted to runes
  * Platform 1.3.3 -> 1.4
  * Stamina 2.0.0.3 -> 2.0.0.4
    * Fixed stamina overlay shaking differently from hearts at low health

# 4.5.8
* Fixed Deep Ruins and Underground Ruins maps never dropping from archaeology
* Updated mods
  * Bits and Balance 2.4.1 -> 2.4.3
  * Collective 8.53 -> 8.56
  * Experience Tweaks 1.1.4.0 -> 1.1.5.1
    * Mace (Breeze Rods), Elytra (Phantom Membranes) and Wolf Armor (Armadillo Scutes) can now be repaired in the anvil
    * Fixed Turtle Shell anvil repair not working
    * Fixed crafting grid repair recipes consuming more materials than needed
    * Many other anvil fixes
  * InsaneLib 2.4.33.1 -> 2.4.33.2
  * Item Block Info HUD 1.1.1.0 -> 1.1.1.1
  * No Hunger 2.1.0.0 -> 2.1.0.1
    * Fixed overtime regen overlay shaking differently from hearts at low health
  * Stamina 2.0.0.2 -> 2.0.0.3
  * Supplementaries 4.0.1 -> 4.0.2
    * Fixed a dupe with the pulley

# 4.5.7
* Re-enabled Hoppers and Hopper Minecarts
* Item Block Info HUD: removed coordinates when holding compass
* In servers, time will now stop when no players are online
* Enduring rune bonus durability increased from +100% to +200% (3x)
* Updated mods
  * Collective 8.51 -> 8.53
  * InsaneSurvivalOverhaul 5.12.5.0-beta -> 5.12.6.0
    * Mobs named with a Name Tag now show a death message in chat when they die
    * Fixed Chainmail armor not recyclable like other metal armors
  * Lithostitched 1.8.0 -> 1.8.1
  * MidnightLib 1.9.3 -> 1.10.0
  * Stamina 2.0.0.1 -> 2.0.0.2

# 4.5.6
First public release
