# Changelog

## Upcoming
* Lowered simple clouds quality
  * This should help performance

## 3.1.0
* Added [Horseman](https://www.curseforge.com/minecraft/mc-mods/horseman)
  * Improves horses
* Added [Scholar](https://www.curseforge.com/minecraft/mc-mods/scholar)
  * Improves book and quill and written books
* Added [Monobank](https://www.curseforge.com/minecraft/mc-mods/monobank)
  * Place your precious items in this safe deposit box storing up to 8k items
  * Safe from Supplementaries' has been disabled
* Added [Regrowth](https://www.curseforge.com/minecraft/mc-mods/regrowth)
  * Villagers will try to build walls, fix paths, torch up dark areas
* Since enchantments are limited, experience is now disabled
* Re-enabled ambient fog

### Changes from Insane Survival Overhaul
**Changes**
* Lowered chance for animals to auto breed
* Ground flint is now slightly more common

**Fixes**
* With experience disabled the jump bar of mounts is no longer hidden

## 3.0.6
* Added farsight
  * On servers, keeps far away chunks not loaded from the server
* Removed Yung's Desert Temples and Jungle Temples
* Enchantments in the enchanting table are now one time use only, so they are consumed on apply
  * This is experimental, let's see how it goes
* Fixed wooden equipment having too much unbreaking

## 3.0.5
* Sprinting is now unlocked at 80% stamina instead of 40%
* Reduced plum restored health
* Fixed vanilla fishing rods not being replaced by tide's
* Fixed not being able to convert rich dirt to dirt with shovels
* Fixed missing many data pack and resource pack files (like Tips)

### Changes from Insane Survival Overhaul
**Addition**
* Simple clouds integration with Tiredness
  * If enabled, thunderous clouds will no longer be removed on sleep and clouds will be fast forwarded
* Tide integration data pack
  * If enabled, will change fish entities to only have a chance to drop the fish

**Changes**
* Minor rework to wooden equipment
  * Wooden equipment now gains +20% attack speed and x2 mining speed when used in sunlight
  * Lowered base mining speed (2.5 -> 2)
  * Lowered % attack speed (+10% -> NONE)
  * Lowered durability (118 -> 108)
  * Lowered unbreaking (80% -> 50% chance to not consume durability)
* Leather, Copper and Chainmail armor durability has been increased
* Increased Iron tools durability by 35%
* Increased shears durability
* Reduced flint and steel durability
* Adjusted Necromium stats
  * Increased % attack speed (-20% -> -15%)
  * Increased % damage (-10% -> -5%)
  * Lowered base attack damage (6 -> 5)
* Shields+
  * Lowered copper shield durability
  * Lowered flint and wooden shield time blocked
* `iguanatweaksreborn:replace_loot` modifier now also keeps nbt tag of the item

**Fixes**
* Missing copper equipment repair
* Tall grass replacing blocks when growing with seasons

### Changes from Insane Survival Extra
**Changes**
* Removed cleansed and enchanted lapis
  * You can now purify items with bottle o' enchanting, which is the same as the old infusing, with increased enchantability and over level enchantments

## 3.0.4
* Added tips to loading screen
* Items from a grave now despawn after 3 minutes instead of 2
* Portable Crates now slow down less (5/20/45/... -> 2.5/10/22.5/...)
* Added repair recipe for iron fishing rod
* Vanilla fishing rods are now replaced with tide's
* Removed tide's fishing boat
* Removed time_stop_no_player_online data pack
  * Now added to InsaneLib

## Alpha 3.0.3
* Baits no longer require seeds
* Lowered cooked fish restored health
* Disabled vanilla shields
* Bottle o' Enchanting now drop 5 levels worth of xp
* Tried to balance mobs/performance by reducing the hostile cap

## Alpha 3.0.2
* Locked stamina no longer slows you down
* Disabled Void fog
* Removed old explosion sound
* Reverted back to Variant Crafting Tables mod

## Alpha 3.0.1
* Mod updates, Tide integration and bug fixes
* Hybrid beta data pack is now optional

## Alpha 3.0.0
This version greatly simplifies the modpack. No more Cleansed lapis, no more forging and no new materials from Insane's Survival Extra. You should be able to update an old world to this version, but the items you have can no longer be obtained and are no longer balanced against new updates.

As for mods, we got new ones like Tide for fishing (which hasn't been configured yet) and Simple Clouds for localized weather.

Hunger is gone again.

Yung's better Strongholds and swamp huts have been replaced with DnT's Strongholds and Swamp Huts.

This is an alpha due to some stuff needs checking (like Tide) and playtest is needed.