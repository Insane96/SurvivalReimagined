# Upcoming
* Fixed recycling tools giving full output
* Bundles can be dyed again
* Enabled Vanilla Backport's modern bundle interface (scroll to select the item to take out); disabled Quark's Rotating Bundles as it conflicts with it

# 4.6.0
* Repair kits can now repair items up to 100% instead of 80%
* Removed Inventory Totem
* Removed Underlay
* Explosive rune delay reduced from 5 to 3 seconds
* Hang Glider durability consumption doubled (1 every 5 ticks instead of 10) and durability halved (818 -> 409)
* Removed duplicate Name Tag recipes, only the vanilla-like one (paper + any nugget) is kept
* Disabled Quark's Compasses Work Everywhere, compasses spin randomly in the Nether and End again
* Supplementaries' Blast Armor Trim can now be duplicated with 1 diamond, like the vanilla ones
* Enhanced AI Leaders now wear a full trimmed copper, chainmail, golden, iron or (rarely) diamond armor and a banner on their head; reinforcements chance now reaches 100% at 3 damage instead of 1
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
