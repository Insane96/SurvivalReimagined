# Resoconto strutture aggiunte dalle mod

Analisi di tutti i 114 file `.jar` presenti in `mods/` (elenchi interni via `unzip -l`, ispezione dei file `data/*/worldgen/structure/*.json`, `data/*/worldgen/template_pool/*.json` e `data/*/structure/*.nbt`) più le 3 datapack sciolte in `datapacks/`. Per ogni struttura trovata è stato letto il campo `"step"` (fase di generazione) e il tag `"biomes"` a cui è agganciata, per determinare **dimensione** e **posizione** (superficie / sotterranea / subacquea). Sono stati controllati anche i file in `config/` per capire quali strutture sono **attive o disattivate**.

Legenda stato:
- 🟢 **Attiva** — genera normalmente, nessun blocco nei config.
- 🔴 **Disattivata** — spenta esplicitamente in un file di config.
- ⚪ **Nessun config dedicato** — la mod non espone un'opzione per disattivare la singola struttura (per disattivarla bisognerebbe rimuovere/editare il datapack integrato nel jar, o disabilitare l'intera mod).

Legenda posizione:
- ☀️ **Superficie** — costruzione visibile sopra al terreno (anche se in parte interrata, come piramidi/rovine).
- ⛏️ **Sotterranea** — genera sottoterra/in caverna, non visibile dalla superficie.
- 🌊 **Subacquea** — genera in acqua/oceano.

> Nota tecnica: il campo `"step"` vanilla non è un indicatore 1:1 di "sopra/sotto terra" (es. Bastioni, Monumenti e molte strutture del Nether usano tecnicamente lo step `underground_decoration` pur essendo costruzioni di superficie). La colonna "Posizione" qui sotto riflette il comportamento reale della struttura, non solo il nome dello step.

---

## 🗺️ Explorer Map

**Correzione rispetto alla prima versione di questo resoconto:** avevo controllato male — **Archeological NON ha mappe** (verificato a fondo: nessuna loot table, nessun item "map", nessun compass/locator; il suo sistema di ritrovamento degli Ancient Vault è basato su una **chiave** — `archeological:ancient_key` — non su mappe). È invece **adventuredungeons** ad avere delle vere explorer map:

| Trovate in... | Mappe verso |
|---|---|
| `underground_camp_chest1.json` (Underground Camp) | Trial Rooms, Bygone Dungeon, Cold Lair, Murky Dungeon (le sue 4 dungeon sotterranee, tutte e 4 nella stessa cassa, peso 5 ciascuna) |
| `ruins_default_chest.json` (Ruins Standard) | stesse 4 mappe di cui sopra |
| `ruins_desert_chest.json` (Ruins Desert) | stesse 4 mappe di cui sopra |

Quindi trovando un Underground Camp o una qualsiasi Ruins "standard"/"desert" di adventuredungeons, hai buone probabilità di ottenere una mappa che porta a una delle sue 4 dungeon (Trial Rooms, Bygone Dungeon, Cold Lair, Murky Dungeon). Le altre mod con strutture (EternalNether, Incendium, Philips' Ruins, formationsnether, immersive_gateways, incubation, abridged, VanillaBackport, sawmill, YungsExtras) **non** hanno mappe proprie; **Supplementaries** ha i Road Sign come indicatori visivi ma non generano mappe.

L'unica altra eccezione è **dentro le mod DnT**, che modificano la loot table vanilla `illager_mansion/map_chest.json` (quella dentro le Magioni Silvestri) per aggiungere mappe verso *altre* strutture — vedi conflitto qui sotto, perché qui è emerso un problema vero.

---

## ⚠️ Conflitti reali trovati (non solo "salt" — anche loot table sovrascritte)

Ho controllato sia i "salt" di generazione (`worldgen/structure_set`) sia le sovrascritture dirette di file (stesso path `data/...` presente in più mod, che in Minecraft non si fondono ma si sovrascrivono a vicenda — vince l'ultimo caricato).

### 🔴 Conflitto 1 — Loot table `illager_mansion/map_chest.json` (DnT Ancient City Overhaul vs DnT Woodland Mansion Replacement)
Sia `DnT-ancient-city-overhaul-v2` **sia** `DnT-woodland-mansion-replacement-v1.2` includono una copia del file vanilla `data/minecraft/loot_table/chests/illager_mansion/map_chest.json` (loot delle Magioni Silvestri), ma con contenuti diversi:

- **DnT Woodland Mansion Replacement** (versione "pulita", coerente col pack): 2 mappe — verso Pillager Outpost e verso Ancient City.
- **DnT Ancient City Overhaul** (versione "leftover" di una suite DnT più grande): 5 mappe — le stesse 2 di sopra **più** mappe verso `nova_structures:witch_villa`, `nova_structures:badlands_miner_outpost` e `nova_structures:illager_hideout`.

**Ho verificato che queste 3 strutture aggiuntive NON esistono da nessuna parte in questo modpack** (nessun jar le definisce — sono strutture di altre mod DnT della stessa serie, non installate qui; restano solo come stringhe di traduzione inutilizzate nei file `lang`). Solo una delle due versioni del file vince (quella caricata per ultima, non deducibile in modo affidabile dai soli file — va controllato in game o nei log di avvio). **Se vince la versione di Ancient City Overhaul**, una parte del loot delle Magioni genererà mappe "rotte" che puntano a strutture inesistenti.

Lo stesso paio di mod si sovrascrive a vicenda anche su `secret_room.json` e `library_chest.json` (sempre dentro `illager_mansion/`): qui la differenza è minima ma un potenziale bug — la versione di *Ancient City Overhaul* usa `"options": "nova_structures:illagers_bane"` (un ID di incantesimo singolo), mentre *Woodland Mansion Replacement* usa `"options": "#nova_structures:illagers_bane"` (un tag, col cancelletto). Se l'ID senza `#` non corrisponde a un incantesimo reale, quella parte del loot table potrebbe fallire/non generare l'incantamento atteso.

**Consiglio:** non è un problema bloccante (tutti gli altri 9 file loot condivisi tra le due mod sono identici), ma vale la pena verificare in gioco cosa esce dal "map chest" delle Magioni, o segnalarlo agli autori delle mod DnT.

### 🔴 Conflitto 2 — `worldgen/structure_set/nether_complexes.json` (Incendium vs DnT Nether Fortress Overhaul Retro, la datapack)
Entrambe ridefiniscono lo **stesso** structure_set vanilla `minecraft:nether_complexes` (quello che governa insieme Fortezza del Nether + Bastione):

| | salt | spacing | separation | exclusion_zone |
|---|---|---|---|---|
| **Incendium** | 30084232 | 16 | 8 | sì — tiene le strutture di Incendium lontane da fortezze/bastioni (8 chunk) |
| **DnT Nether Fortress Overhaul Retro** (datapack) | 30084232 | 27 | 4 | ❌ assente |

Solo una versione vince. Le datapack sciolte in `datapacks/` (marcate `required` in `config/global_packs.toml`) generalmente hanno **priorità più alta** dei dati dentro i jar delle mod, quindi è probabile che vinca la versione DnT (spacing 27/separation 4, **senza** l'exclusion_zone di Incendium). Se così fosse, si perde la protezione che Incendium usa per evitare che le sue strutture (torri, castelli, villaggi piglin, ecc.) generino a ridosso di Fortezze/Bastioni — possibile "affollamento"/sovrapposizione di strutture nel Nether in certe zone.

**Consiglio:** testare in un mondo nuovo e, se si notano fortezze/bastioni troppo vicini a strutture Incendium, considerare di rimuovere/rinominare uno dei due file per dare priorità esplicita a uno dei due.

### ✅ "Salt" duplicati che invece sono INNOCUI (voluti dal design delle mod)
Controllando tutti gli 83 file `structure_set` del pack, oltre al conflitto sopra ci sono altri 3 casi di salt duplicato, ma sono tutti innocui:

- **`desert_pyramids` / `desert_ruins`** (salt 239021) e **`jungle_temples` / `jungle_ruins`** (salt 239021, identico anche tra deserto e giungla) — è il meccanismo voluto delle mod DnT: la struttura vanilla viene svuotata con uno "start_pool" speciale (`nova_structures:vanilla_structure_remover`) esattamente sulla stessa griglia dove genera la struttura sostitutiva, cosicché la vecchia venga "rimossa" e la nuova prenda il suo posto nello stesso punto. Nessun conflitto reale.
- **`ocean_monuments` / `trident_trial_monument`** (salt 69846574) — stesso meccanismo di sostituzione pulita.
- **`villages` (versione modificata da ISO) / `woodland_mansions` / `illager_manor`** (salt 10387319) — la versione di `villages` inclusa nel pacchetto integrato `disable_long_noses` di InsaneSurvivalOverhaul (per `"Disable long noses structures" = true`, vedi `CLAUDE.md`) ha `"structures": []` (lista vuota): non genera letteralmente nulla, quindi condividere il salt con le Magioni non causa nessuna competizione per lo spazio.

---

## ✅ Mod che aggiungono o sostituiscono strutture

### Archeological — 🟢 attiva, nessun config dedicato
`Archeological-neoforge-1.21.1-1.2.2.jar` — Sistema di siti archeologici da scavare con la spazzola. **Dimensione: solo Overworld** (tag `#minecraft:is_overworld`, `desert`, `#minecraft:is_badlands`, `#minecraft:is_forest`).

| Struttura | Posizione | Bioma |
|---|---|---|
| Ancient Vault (Deep/Underground ruins) | ⛏️ Sotterranea | Overworld generico |
| Ancient Vault (Desert/Frozen/Rock/Wasteland ruins, Ruined Hut) | ☀️ Superficie | deserto / neve / roccia / badlands |
| Deep Ruins (S/M/L) | ⛏️ Sotterranea | Overworld generico |
| Desert Ruins (S/M/L) | ☀️ Superficie | deserto |
| Frozen Ruins (S/M/L) | ☀️ Superficie | biomi innevati |
| Rock Ruins (S/M/L) | ☀️ Superficie | biomi rocciosi |
| Ruined Camp (rosso/verde/blu) | ☀️ Superficie | foresta |
| Underground Ruins (S/M/L) | ⛏️ Sotterranea | Overworld generico |
| Wasteland Ruins (S/M/L) | ☀️ Superficie | badlands |

### DnT — Ancient City Overhaul — 🟢 attiva, nessun config dedicato
Sostituisce `ancient_city` vanilla. ⛏️ **Sotterranea**, **Overworld** (Deep Dark, stesso bioma di sempre).

### DnT — Desert Temple Replacement — 🟢 attiva, nessun config dedicato
Sostituisce `desert_pyramid`. ☀️ **Superficie**, **Overworld** (deserto).

### DnT — Jungle Temple Replacement — 🟢 attiva, nessun config dedicato
Sostituisce `jungle_pyramid`. ☀️ **Superficie**, **Overworld** (giungla).

### DnT — Ocean Monument Replacement — 🟢 attiva, nessun config dedicato
Sostituisce `monument`. 🌊 **Subacquea**, **Overworld** (oceano profondo).

### DnT — Stronghold Overhaul — 🟢 attiva, nessun config dedicato
Sostituisce `stronghold`. ⛏️ **Sotterranea**, **Overworld**.

### DnT — Swamp Hut Overhaul — 🟢 attiva, nessun config dedicato
Sostituisce `swamp_hut`. ☀️ **Superficie**, **Overworld** (palude).

### DnT — Woodland Mansion Replacement — 🟢 attiva, nessun config dedicato
Sostituisce `mansion`. ☀️ **Superficie**, **Overworld** (dark forest).

### DnT — Nether Fortress Overhaul Retro *(nuova scoperta — è una datapack, non un jar!)*
File: `datapacks/DnT Nether Fortress Overhaul Retro 2.5.zip`. Sostituisce `fortress.json` vanilla. ☀️ **Superficie** (del Nether, sospesa sulla lava come da vanilla), **dimensione Nether**. 🟢 **Attiva** — è dentro `datapacks/`, che in `config/global_packs.toml` è impostato come `required`, quindi sempre caricata in ogni mondo.

### EternalNether — 🟢 attiva, nessun config dedicato
`EternalNether-v21.1.3-1.21.1-NeoForge.jar`. **Dimensione: Nether** (biomi `warped_forest` e simili).

| Struttura | Posizione |
|---|---|
| Catacomb | ⛏️ Sotterranea |
| Citadel | ☀️ Superficie |
| Piglin Manor | ☀️ Superficie |

### Incendium — 🟢 attiva, nessun config dedicato
`Incendium_1.21.x_v5.4.4.jar`. **Dimensione: Nether** (biomi custom `incendium:infernal_dunes`, `incendium:withered_forest`, ecc.). Tutte e 9 le strutture tecnicamente usano lo step `underground_decoration`, ma sono edifici di **superficie del Nether** (torri, castelli, villaggi, come i Bastioni vanilla): Abandoned Tower, Forbidden Castle, Infernal Altar, Nether Reactor, Piglin Village, Pipeline, Quartz Kitchen, Ruined Lab, Sanctum. ☀️ Superficie (Nether).

### Philips' Ruins — 🟢 attiva, nessun config dedicato
`Philips-Ruins1.21.1-2.0-NeoForge.jar`. **Dimensione: solo Overworld** (biomi vanilla come forest, jungle, swamp, plains, deep_dark, lush_caves, ecc.).

| Struttura | Posizione |
|---|---|
| Ancient Crypt, Ancient Ruins, Ancient Towers, Field Stone Ruins (+rocks), Level One/Two/Three Ruins (+pool), Pumpkin Ruins, Rare Ruin | ☀️ Superficie |
| Ancient Dungeon, Lost Soul City, Underground Structures | ⛏️ Sotterranea |
| Lost Soul Dungeon | ⛏️ Sotterranea |
| Ocean Fortress, Ocean Ruins | 🌊 Subacquea |

### VanillaBackport — 🟢 attiva (via config)
`VanillaBackport-neoforge-1.21.1-1.1.7.10.jar`. Non registra vere strutture jigsaw ma pezzi/feature decorative:
- **Pale Oak** (Pale Garden): ☀️ Superficie, **Overworld** — attivo, `pale_garden = true` in `vanillabackport-common.toml`.
- **Sulfur Springs**: ⛏️ Sotterranea (sopra le Sulfur Caves), **Overworld** — attivo, `has_sulfur_springs = true` in `vanillabackport-common.toml`.

### abridged — 🟢 attiva (via config)
`abridged-2.0.2-neoforge-21.1.jar`. **Bridge**: ☀️ Superficie (attraversa ravine/canyon), **Overworld**. Config `abridged.json`: `"frequency": 0.8` (80% di possibilità quando viene trovata una posizione valida) — non è disattivato.

### adventuredungeons — 🟢 attiva, nessun config dedicato
`adventuredungeons-neoforge-1.21-1.3.1.jar`. **Dimensione: solo Overworld**.

| Struttura | Posizione | Bioma |
|---|---|---|
| Bygone Dungeon | ⛏️ Sotterranea | — |
| Cold Lair | ⛏️ Sotterranea | biomi innevati |
| Murky Dungeon | ⛏️ Sotterranea | palude |
| Trial Rooms | ⛏️ Sotterranea | montagna/badlands |
| Underground Camp | ⛏️ Sotterranea | dove spawnano avamposti pillager |
| Ruins Desert / Snow / Standard | ☀️ Superficie | deserto / neve / generico |

### clayworks — 🟢 attivo, nessun config di worldgen
`clayworks-1.21.1-4.0.3.jar`. Non è una struttura a sé: aggiunge solo vasi decorativi dentro i **Trial Chambers** vanilla (☀️/⛏️ dipende dal Trial Chamber stesso — sono sotterranei). **Overworld.**

### formationsnether — 🟢 attiva, nessun config dedicato
`formationsnether-1.0.5a-mc1.21+.jar`. **Dimensione: Nether** (bioma `basalt_deltas` e altri).

| Struttura | Posizione |
|---|---|
| Basalt Hut, Ore Shard | ⛏️ Sotterranea |
| Tutte le altre 18 (Blackstone Castle/Remnant, Campsite, Checkerboard Temple, Flaming Pillar, Large House, Large/Small Pedestal, Large Tree, Nether Wart Field, Obsidian Pillar, Parkour Challenge, Quartz Spikes, Respawn Anchor Altar, Rib Cage, Small Fire/Lava Arena, Small Lava Shrine, Sphere Cage) | ☀️ Superficie |

### Immersive Gateways — 🟢 attiva, nessun config on/off (solo parametri di distanza)
`immersive_gateways-neoforge-0.0.6.jar`. ☀️ Superficie, **solo Overworld** — nonostante il file `immersive_gateways.json` elenchi colori anche per biomi Nether/End (badlands, cherry_grove, desert, ice, jungle, mangrove_swamp, mountain, mushroom, plains, swamp: 10 biomi, tutti Overworld). Config regola solo `minDistance`/`maxDistance` tra i gateway (1024–8096 blocchi), non un enable/disable.

### ✅ FIX APPLICATO — loot troppo forte
L'unica loot table (`immersive_gateways:chests/default`, 4-8 estrazioni) aveva il 34% di possibilità **per estrazione** di un pezzo di equipaggiamento dorato incantato (9 voci su ~25) — ~92% delle casse ne davano almeno uno, in media ~2. Generano con spacing 32/separation 8 (densità da villaggio). Sostituita in `datapacks/survivalreimagined/data/immersive_gateways/loot_table/chests/default.json` con una copia di `philipsruins:chest/level_one_ruins_loot` (già riequilibrata) — niente più oro incantato, oggetti coerenti con una struttura di superficie comune.

### Incubation — 🟢 attiva, nessun config dedicato, ma **di fatto morta**
`incubation-1.21.1-5.0.2.jar`. Pollaio ("chicken coop") aggiunto ai pool dei **villaggi** vanilla (desert/plains/savanna/snowy/taiga). ☀️ Superficie, **Overworld**.

⚠️ **Irrilevante in questo pack**, stesso motivo di Sawmill (vedi sopra): `minecraft:villages` è svuotato (`"structures": []`) dal pacchetto integrato `disable_long_noses` di InsaneSurvivalOverhaul, quindi il pollaio non ha villaggi a cui agganciarsi.

### InsaneSurvivalOverhaul — 🔴 **DISATTIVATA**
`insanesurvivaloverhaul-5.7.1.0.jar`. **Echo Pillar**: ☀️ Superficie (genera a `y=0` proiettata sull'ocean floor), **Overworld**. In `config/insanesurvivaloverhaul/common.toml`:
```
[Death]
"Enable Echo pillar" = false        # <- interruttore master: SPENTO
    [Death."Echo pillar"]
    "Echo pillars" = true            # <- sub-toggle del datapack, ma ignorato perché il master è false
```
**La struttura non genera attualmente nel pack**, nonostante il sotto-toggle del datapack sia `true`.

### Sawmill — 🟢 attivo, nessun config di worldgen, ma **di fatto morto**
`sawmill-1.21-1.8.0-neoforge.jar`. Casa del falegname aggiunta ai pool dei **villaggi** vanilla (13 varianti di bioma). ☀️ Superficie, **Overworld**. Config (`sawmill-common.toml`) ha solo `repurposed_structures_compat = true`, nessun on/off per la struttura stessa.

⚠️ **Irrilevante in questo pack:** `minecraft:villages` (e `pillager_outposts`) vengono svuotati con `"structures": []` dal pacchetto integrato `disable_long_noses` di InsaneSurvivalOverhaul (`"Disable long noses structures" = true`, vedi `CLAUDE.md`) — i villaggi non generano mai, quindi la casa del falegname non ha dove agganciarsi. Non vale la pena analizzare/sistemare altro su Sawmill per questo motivo.

### Supplementaries — 🔴 **ENTRAMBE DISATTIVATE**
`supplementaries-1.21.1-3.8.8-neoforge.jar`.

**Correzione rispetto alla prima versione:** avevo sbagliato su entrambe. In `config/supplementaries-common.toml`:

| Struttura | Posizione | Dimensione | Stato |
|---|---|---|---|
| Galleon | 🌊 Subacquea/superficie oceano | Overworld | 🔴 **Disattivato** — `[functional.cannon.plunderer].galleon = false` (riga 263). Avevo scambiato questo flag per un semplice comportamento del cannone dei Plunderer, ma è in realtà l'interruttore della struttura stessa. |
| Road Sign | ☀️ Superficie (lungo sentieri) | Overworld | 🔴 **Disattivato** — `[building.way_sign.road_signs].enabled = false` (riga 431), commento esplicito nel file: *"Entirely disables them from spawning"*. Mi era sfuggito perché la riga non conteneva parole chiave come "road_sign" nel mio primo controllo. |

### YungsExtras — 🟢 attivo, nessun config dedicato
`YungsExtras-1.21.1-NeoForge-5.1.1.jar`. Non registra vere strutture jigsaw ma decorazioni via `biome_modifier`, tutte ☀️ Superficie, **Overworld**: obelischi, pozzi, pozzi dei desideri (deserto), archi di palude, "chillzone" (deserto/palude). Sostituisce anche il pozzo del deserto vanilla (`vanilla_desert_well_removal`).

---

## ⚙️ Librerie/API usate da altre mod (NON aggiungono strutture proprie)

- **YungsApi** — libreria per le mod di YungNickYoung (nessun dato strutturale proprio).
- **formations** (SuperMartijn642) — libreria di processori/piece usata da `formationsnether`.
- **blueprint** (Team Abnormals) — libreria worldgen usata da altre mod Abnormals.
- **lithostitched** — libreria/API di jigsaw generation avanzata; modifica solo alcuni `template_list` vanilla (nether fossil, ruined portal, shipwreck, woodland mansion) per varietà, ma non introduce strutture nuove.
- **Quark** e **amendments** — contengono solo *tag* (`tags/worldgen/structure/...`) che classificano strutture vanilla esistenti (es. per il loot dei forzieri), non strutture nuove.

---

## ➖ Mod che NON aggiungono alcuna struttura

AmbientSounds, BTP, BetterAdvancements, BetterTridents, CreativeCore, CutThrough, Drip Sounds, DyedFlames, EffectDescriptions, Geophilic, HangGlider, ImmediatelyFast, Kiwi, LeavesBeGone, MouseTweaks, NoChatReports, PassableFoliage, PickUpNotifier, Pixelshot, Platform, PuzzlesLib, StrawStatues, StylishEffects, TreeChop, VisualWorkbench, YungsBetterCaves, Zeta, alternate_current, architectury, areaeffectcloud3d, balm, betterdays, biolith, bitsandbalance, blur, boatload, carryon, catalogue, chat_heads, cinchsbetterdeepslate, cloth-config, collective, configured, coroutil, defaultoptions, e4mc, emi, enhancedai, experiencetweaks, explosionoverhaul, extendedbonemeal, ferritecore, fwa, globalpacks, ibo, inventorytotem, jamlib, lambdynamiclights, lithium, midnightlib, mobspropertiesrandomness, modelfix, modernfix, moonlight, mooshroomtweaks, netherportalfix, nohunger, nyfsspiders, packetfixer, particlerain, pathtodirt, personality, quickstack, runeenchanting, screenshot_viewer, server_i18n_api, shieldsplus, snowundertrees, sodium, spark, underlay, wits, worldplaytime, wscommands, yet_another_config_lib_v3, insanelib, PuzzlesLib.

Anche le datapack `survivalreimagined` e `no_emeralds_datapack` (in `datapacks/`) sono state controllate: **non aggiungono strutture**.

*(Nota: `YungsBetterCaves` genera solo terreno di caverne, non "strutture" in senso stretto.)*

---

## 💰 Philips' Ruins — modifiche applicate

Trovato bottino da endgame (spada di diamante, mele dorate...) su strutture "basse" come Field Stone Ruins e Pumpkin Ruins, più nomi di debug lasciati nelle casse. Fix applicati via override in `datapacks/survivalreimagined/`:

- **Loot riequilibrato**: 22 pezzi di Field Stone Ruins/Pumpkin Ruins (+1 di Ancient Ruins) spostati da `level_three_ruins_loot` a loot table di fascia bassa coerente.
- **Nomi di debug rimossi**: 287 `CustomName` (es. "Level Three Ruins loot") tolti da 107 file `.nbt` — le casse ora mostrano il titolo normale.
- **`level_one_ruins_loot`**: rimossi elmo/vanga di ferro e forbici.

Non toccate: le 6 loot table mancanti (casse vuote in Bone/Sculk Dungeon, Nether Dungeon/Ruin, End Ruins, Badlands) e lo squilibrio Ocean Ruins/Ocean Fortress.

---

## 🧭 Strutture vanilla — cosa è disattivato/modificato, e fix applicato

Controllato ogni `structure_set` vanilla ridefinito da una mod (non solo quelli che c'entrano con le mod strutturali già elencate sopra), cercando in particolare `"structures": []` (liste vuote = struttura disattivata).

- **Villaggi e Avamposti Pillager: disattivati.** Il pacchetto integrato `disable_long_noses` di InsaneSurvivalOverhaul (`"Disable long noses structures" = true`) svuota `minecraft:villages` e `minecraft:pillager_outposts` con `"structures": []` — non generano mai (già documentato sopra per Sawmill/Incubation).
- **Nessun'altra struttura vanilla è disattivata.** Controllato specificamente in `insanesurvivaloverhaul` per buried treasure, ruined portal, trail ruins, trial chambers, nether fossil, bastion, igloo, ocean ruins, pozzo del deserto: nessun toggle, nessuna menzione.
- **Città di Fine (End City): AUMENTATE, non ridotte.** Altro pacchetto integrato di ISO, `increased_end_cities` (`"Increase end cities" = true`, attivo): spacing passa da 20/11 (vanilla) a 11/7 — città di fine molto più dense.
- **Scoperta bonus, mod non attiva:** `ibo-3.1.0-neoforge-1.21.jar` = **"Incendium Biomes Only"**, una mod a parte (di Naomi Roberts) che dichiara esplicitamente "Disables everything but biomes in Incendium" — un resourcepack imbustato nel jar che filtra via *tutte* le strutture/loot table/structure_set di Incendium, lasciando solo i suoi biomi. **Non risulta attivo**: non è estratto in `resourcepacks/`, non compare tra i pack abilitati in `global_packs.toml`. Se in futuro volete disattivare le 9 strutture giganti di Incendium tenendo i suoi biomi, questa mod è già pronta — basta capire come attivarla (probabilmente dal menu resource pack in game) — e risolverebbe anche di striscio il conflitto `nether_complexes` con la Fortezza del Nether DnT segnalato sopra.

### ✅ FIX APPLICATO — Relitti (Shipwreck) più rari
`minecraft:shipwrecks` (nessuna mod lo toccava). Override in `datapacks/survivalreimagined/data/minecraft/worldgen/structure_set/shipwrecks.json`:

| | spacing | separation |
|---|---|---|
| Vanilla | 24 | 4 |
| **Ora** | **48** | **8** |

Raddoppiati entrambi (stesso rapporto, stesso salt/strutture vanilla) — relitti circa la metà frequenti. Fammi sapere se vuoi tararli diversamente.

---

## Osservazioni per il pack

- **Strutture disattivate nel pack: Echo Pillar** (ISO, `"Enable Echo pillar" = false`), **Galleon** e **Road Sign** (Supplementaries, entrambe spente in `supplementaries-common.toml`). Tutte le altre strutture elencate sopra sono attive.
- **8 strutture vanilla sono sostituite** dalle mod DnT (7 jar + 1 datapack): Città Antica, Piramide del Deserto, Tempio della Giungla, Monumento Oceanico, Fortezza, Capanna della Strega, Magione Silvestre, **Fortezza del Nether** (quest'ultima trovata solo ora, dentro `datapacks/`, non nei jar — nessun conflitto con le altre.
- **Concentrazione nel Nether**: Incendium, EternalNether, formationsnether e la Nether Fortress DnT generano tutte lì (quasi tutte "di superficie" nel Nether, non sepolte). *(Correzione: nella versione precedente collegavo questo a "Portal requires crying obsidian" e al tetto del Nether attivo — non c'entrano nulla con la densità di generazione, era un'aggiunta senza senso da parte mia. L'unico modo per giudicare se la densità nel Nether è davvero eccessiva è guardare spacing/separation reali di ogni mod, vedi sotto, oppure verificarlo in gioco.)*
- ~~Overworld sovraffollato di rovine generiche~~ — **ritrattato**: in gioco non hai trovato troppe strutture, e i numeri lo confermano. Guardando gli spacing/separation reali (estratti dai `structure_set`): Archeological usa ~30 structure_set separati con spacing 150-200 ciascuno (rovine "grandi" fino a 1 ogni 200 chunk), adventuredungeons ha spacing 30-40, Philips' Ruins varia da 40 a 360 (Rare Ruin, come dice il nome, è molto rara). YungsExtras non usa nemmeno il sistema a griglia (`structure_set`) ma decorazioni via `biome_modifier`, quindi non compete per lo spazio con le altre. La mia frase precedente era una supposizione non verificata sui numeri — la densità reale non sembra eccessiva.
- Nessuna struttura tra quelle elencate genera nell'**End** — nessuna mod del pack tocca quella dimensione.
- **Nessuna struttura del pack ha una propria explorer map** (vedi sezione dedicata sopra).
- **Due conflitti reali di sovrascrittura file** trovati tra mod DnT tra loro e tra Incendium/DnT: vedi sezione "⚠️ Conflitti reali trovati" sopra per i dettagli (loot table della Magione con mappe verso strutture inesistenti, e griglia di generazione di Fortezza/Bastione del Nether ridefinita due volte con parametri diversi).
