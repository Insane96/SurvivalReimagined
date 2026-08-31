# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is a **Minecraft 1.21.1 NeoForge modpack instance directory** — not a Java/source code project. The primary author (Insane96) is the developer of two mods used in this pack: **InsaneSurvivalOverhaul** (ISO) and **RuneEnchanting**. The modpack serves as a playtest environment for those mods alongside compatible community mods.

There is no build system. Changes are made by editing config files and datapacks directly. Minecraft must be launched via CurseForge to apply changes.

## Applying config changes

- **Most ISO features**: require a Minecraft restart to take effect. A few (noted in the config) support `/reload`.
- **Data pack changes** (files under `datapacks/`): take effect with `/reload` in-game.
- **Gamerules** (`config/gamerule_manager/default.json`): applied when a new world is created.
- **`.toml.bak` files** are auto-generated backups — do not edit them, they are gitignored via `*.toml.bak`.

## Repository structure

| Path | Purpose |
|------|---------|
| `mods/` | JAR files for all installed mods |
| `config/insanesurvivaloverhaul/` | InsaneSurvivalOverhaul configs, split by feature category |
| `config/runeenchanting/` | RuneEnchanting system (`main.toml`, `runes.toml`) |
| `config/gamerule_manager/` | Default gamerules for new worlds |
| `datapacks/survivalreimagined/` | Custom datapack for this modpack (nether tweaks, etc.) |
| `datapacks/no_emeralds_datapack/` | Converts emerald loot to runes; removes emerald ore generation |
| `defaultconfigs/` | Per-world default configs (e.g. biome settings via Biolith) |

## InsaneSurvivalOverhaul config architecture

ISO uses a two-level config system:

1. **`config/insanesurvivaloverhaul/common.toml`** — master enable/disable switches for each feature module (Combat, Death, Farming, Hunger & Health, Items, Mining, Misc, Mobs, Movement, Sleep, World).
2. **Feature-specific JSON files** in `config/insanesurvivaloverhaul/<Category>/` — fine-grained overrides (e.g. custom terrain slowdown, energy boost items, echo pillar effects, mob equipment drop chances).

Many ISO features have a `"Data pack" = true` option that toggles an integrated data pack bundled inside the mod JAR. These are separate from files in the `datapacks/` directory.

## RuneEnchanting system

Vanilla enchanting is completely replaced by runes. Key points:
- `config/runeenchanting/runes.toml` — enable/disable each rune and tune its numeric values.
- `config/runeenchanting/main.toml` — global settings (hide items from creative, integrated data pack that removes enchanting table recipe).
- The `datapacks/no_emeralds_datapack/` replaces emerald drops with runes (20% chance via `emerald_to_rune.json` loot modifier) and removes emerald ore generation.

## Active gameplay design decisions

Key non-obvious settings currently configured:
- **Nether portal** requires Crying Obsidian in corners (`Portal requires crying obsidian = true`).
- **Experience** is disabled via gamerule (`experienceoverhaul:disable_experience = true`).
- **Stone tools** are removed; copper fills that tier (`"Enable Stone tools gone" = true`).
- **Vanilla enchanting table** recipe is removed; runes replace enchantments.
- **Villages and pillager outposts** do not generate (`"Disable long noses structures" = true`).
- **Spawners** start empowered (burst of 20 mobs, then disable permanently) — the Spawner Reactivator item exists in ISO but is **disabled** in this pack (`"Re-enable with Spawner Reactivator" = false`), so disabled spawners cannot be reactivated.
- **Sleeping** requires tiredness (gained through exhaustion); phantoms spawn from tiredness not insomnia.
- **Nether roof** and 8:1 ratio are kept (the data pack option to disable them is set to `false`).
- **Echo Pillar** (ISO respawn-anchor feature) is **disabled** (`"Enable Echo pillar" = false`).
- **Storage Drawers Controller and Compacting Drawer** are disabled in `config/storagedrawers-common.v2.toml`.
- **Quark's `[oddities]` category** (Totem of Holding, Pipes, Magnets, Crate, Backpack, Tiny Potato, Matrix Enchanting) reads `true` in `config/quark-common.toml`, but none of it actually works: it requires a separate "Quark Oddities" addon jar that is **not installed** — only the base `Quark-*.jar` is present in `mods/`. Don't trust these toggles at face value; verify the feature is reachable in-game (or that its jar exists) before relying on it.
- **Matrix Enchanting** is explicitly set to `false` even though it's a `[tools]`-category (not oddities) Quark feature that *would* otherwise work — disabled on purpose since RuneEnchanting already removes the vanilla enchanting table.

## Legacy content on the `v3` / `v2` branches

Before this pack was updated to 1.21.1, datapack/resourcepack content lived under
`global_packs/required_data/<pack>/data/...` and `global_packs/required_resources/...`
(the CurseForge "global packs" convention), instead of today's `datapacks/survivalreimagined/`.
That structure no longer exists on `1.21.1`, but it's still reachable on `origin/v3`
(and `origin/v2`) via `git show origin/v3:<path>` — it contains custom advancements,
recipes, and other content that was never ported to the current version. When adding
new datapack content (advancements especially), check whether v3 already solved the
same problem before designing from scratch — some of it references mods no longer in
this pack (e.g. `map_atlases`, `easel_does_it`, `heartstone`, `labels`, `betterdungeons`,
`nova_structures`) and should be skipped, but plenty is still directly portable.

## TODO

Current open work is tracked in `TODO.md` and `advancements_to_add.md`.
