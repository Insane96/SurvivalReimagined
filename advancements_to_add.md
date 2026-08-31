# Advancement da aggiungere

Lista di lavoro per nuovi advancement nel datapack `survivalreimagined`
(schema: tab adventure, frame "task", `minecraft:inventory_changed` dove possibile,
vedi `storage_drawers.json` / `framing_table.json` come riferimento).

## Storage Drawers
- [x] Prima drawer (`adventure/storage_drawers.json`)
- [x] Framing table (`adventure/framing_table.json`)
- ~~Controller~~ / ~~Compacting Drawer~~ — disattivati in config, non servono

## RuneEnchanting
- [x] Fatto direttamente nel repo sorgente della mod (non nel modpack)

## Da portare dal branch v3 (esistevano già, mai migrati su 1.21.1)
Trovati in `global_packs/required_data/survivalreimagineddatapack/data/.../advancements/`
sul branch `origin/v3` — non ancora presenti su `1.21.1`.

- [x] **Hang Glider** — implementato in `adventure/hang_glider.json`,
      parent `minecraft:story/smelt_iron`
- ~~Quark — Get all Corundum~~ — **non serve più**: il vecchio override in v3
  esisteva perché nella versione 1.20.1 l'advancement spedito da Quark era rotto.
  Nel jar attuale (`Quark-4.1-482`) è già presente e funzionante di suo
  (`data/quark/advancement/content/get_all_corundum.json`, parent
  `minecraft:story/smelt_iron`, condition `zeta:flag`/`corundum` che lo disattiva
  da sola se il modulo Corundum è spento) — niente da portare
- [x] **Straw Statue** — implementato in `adventure/straw_statue.json`, riagganciato a
      `minecraft:story/smelt_iron` (l'originale `iguanatweaksreborn:story/furnace` non
      esiste più in ISO)
- ~~atlas.json~~ / ~~easel.json~~ / ~~heartstone.json~~ / ~~storage_labels.json~~ —
  mod (`map_atlases`, `easel_does_it`, `heartstone`, `labels`) non più nel pack, scartati
- ~~betterdungeons/root.json~~ / ~~nova_structures/*~~ — mod non più nel pack, scartati

## InsaneSurvivalOverhaul (ISO)
- [x] ~~Catena "Età del rame"~~ — **già coperta**, nessun codice da scrivere. Esiste
      già una catena equivalente come JSON statici dentro `integrated_packs/` nel repo
      ISO (root `minecraft:story/mine_stone` → `two_flints`/`charcoal`/`campfire` →
      `copper_tools`/`smelt_iron`), non nel provider Java. Dettagli e un bug minore
      trovato per strada (copy-paste tra `two_flints.json` e `charcoal.json`) salvati
      in memoria di progetto (`iso_copper_age_advancement_resolved`)
- ~~Echo pillar~~ — disattivato
- ~~Spawner Reactivator~~ — disattivato

## Quark
- [x] Ender Watcher, Compressed Blocks, Slime in a Bucket — confermati attivi, candidati
- [ ] Get all Corundum — vedi sopra (da v3)
- ~~Ancient Tomes~~ — disattivato (master switch)
- ~~Totem of Holding~~ / ~~Pipes~~ / ~~Magnets~~ / ~~Crate~~ / ~~Backpack~~ / ~~Tiny Potato~~ —
  categoria `[oddities]`, ma manca il jar "Quark Oddities" separato: non funzionanti
  nonostante il config dica `true`
- ~~Crystals Craft Runes~~ — non è un vero obiettivo, era solo un sotto-toggle del
  Corundum; l'advancement vero è "Get all Corundum" sopra

## Altre mod
- [ ] **CarryOn** — **bloccato, verificato non fattibile con solo JSON**: CarryOn
      (`tschipp.carryon`) implementa il "carry" via mixin su `Entity` + una data
      attachment interna (`CarryOnData`), non uno stack in inventario né un'entità
      passeggero — non esiste nessun trigger vanilla che possa intercettarlo, e la mod
      stessa espone solo un `AdvancementCondition` per *leggere* condizioni da
      advancement (per lo scripting di pickup), non un trigger da *scatenare*.
      Serve codice mod-side (un criterion trigger custom) per renderlo possibile —
      altrimenti va scartato
- ~~Gravestone~~ — scartato: in hardcore chi muore non potrà mai ottenerlo
- ~~TreeChop~~ — scartato: è letteralmente la prima azione in un mondo nuovo, banale
- ~~Archeological~~ — ha già 8 advancement propri completi, non serve aggiungere altro
- ~~BetterTridents~~ / ~~Strutture overhaul (DnT/Yung's/Philip's Ruins)~~ — scartati:
  sono le stesse strutture/oggetti vanilla solo migliorati, non serve un advancement dedicato
