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

**adventuredungeons** ha delle vere explorer map:

| Trovate in... | Mappe verso |
|---|---|
| `underground_camp_chest1.json` (Underground Camp) | Trial Rooms, Bygone Dungeon, Cold Lair, Murky Dungeon (le sue 4 dungeon sotterranee, tutte e 4 nella stessa cassa, peso 5 ciascuna) |
| `ruins_default_chest.json` (Ruins Standard) | stesse 4 mappe di cui sopra |
| `ruins_desert_chest.json` (Ruins Desert) | stesse 4 mappe di cui sopra |

Quindi trovando un Underground Camp o una qualsiasi Ruins "standard"/"desert" di adventuredungeons, hai buone probabilità di ottenere una mappa che porta a una delle sue 4 dungeon (Trial Rooms, Bygone Dungeon, Cold Lair, Murky Dungeon). Le altre mod con strutture (Incendium, Philips' Ruins, formationsnether, immersive_gateways, incubation, abridged, VanillaBackport, sawmill, YungsExtras) **non** hanno mappe proprie; **Supplementaries** ha i Road Sign come indicatori visivi ma non generano mappe.

L'unica altra eccezione è **dentro le mod DnT**, che modificano la loot table vanilla `illager_mansion/map_chest.json` (quella dentro le Magioni Silvestri) per aggiungere mappe verso *altre* strutture — vedi conflitto qui sotto, perché qui è emerso un problema vero.

---

## ⚠️ Conflitti reali trovati (non solo "salt" — anche loot table sovrascritte)

Ho controllato sia i "salt" di generazione (`worldgen/structure_set`) sia le sovrascritture dirette di file (stesso path `data/...` presente in più mod, che in Minecraft non si fondono ma si sovrascrivono a vicenda — vince l'ultimo caricato).

### ✅ Conflitto 1 (RISOLTO) — Loot table `illager_mansion/map_chest.json` (DnT Ancient City Overhaul vs DnT Woodland Mansion Replacement)
Sia `DnT-ancient-city-overhaul-v2` **sia** `DnT-woodland-mansion-replacement-v1.2` includono una copia del file vanilla `data/minecraft/loot_table/chests/illager_mansion/map_chest.json` (loot delle Magioni Silvestri), ma con contenuti diversi:

- **DnT Woodland Mansion Replacement** (versione "pulita", coerente col pack): 2 mappe — verso Pillager Outpost e verso Ancient City.
- **DnT Ancient City Overhaul** (versione "leftover" di una suite DnT più grande): 5 mappe — le stesse 2 di sopra **più** mappe verso `nova_structures:witch_villa`, `nova_structures:badlands_miner_outpost` e `nova_structures:illager_hideout`.

**Ho verificato che queste 3 strutture aggiuntive NON esistono da nessuna parte in questo modpack** (nessun jar le definisce — sono strutture di altre mod DnT della stessa serie, non installate qui; restano solo come stringhe di traduzione inutilizzate nei file `lang`). Solo una delle due versioni del file vince (quella caricata per ultima, non deducibile in modo affidabile dai soli file — va controllato in game o nei log di avvio). **Se vince la versione di Ancient City Overhaul**, una parte del loot delle Magioni genererà mappe "rotte" che puntano a strutture inesistenti.

Lo stesso paio di mod si sovrascriveva a vicenda anche su `secret_room.json` e `library_chest.json` (sempre dentro `illager_mansion/`): qui la differenza era minima ma un potenziale bug — la versione di *Ancient City Overhaul* usa `"options": "nova_structures:illagers_bane"` (un ID di incantesimo singolo), mentre *Woodland Mansion Replacement* usa `"options": "#nova_structures:illagers_bane"` (un tag, col cancelletto, quella corretta).

**Fix applicato:** copiati entrambi i file nella loro versione corretta (con `#`, presa da Woodland Mansion Replacement) come override in `datapacks/survivalreimagined/data/minecraft/loot_table/chests/illager_mansion/`, che vince su entrambe le mod.

**Fix applicato:** creato un override unico in `datapacks/survivalreimagined/data/minecraft/loot_table/chests/illager_mansion/map_chest.json` che vince su entrambe le versioni delle mod (base ripresa dalla versione "pulita" di Woodland Mansion Replacement). La mappa verso `minecraft:pillager_outpost` (struttura disattivata in questo pack, quindi già morta di suo) è stata sostituita con una **mappa del Monumento Oceanico** (`minecraft:monument`, decorazione vanilla `monument`), colmando anche il buco di mappe che in vanilla darebbe solo il Cartografo (assente in questo pack). Resta la mappa verso l'Ancient City.

**Aggiornamento (reinstallazione di Woodland Mansion Replacement con l'overhaul dei villager di ISO):** i tre override erano stati tolti insieme alla mod e sono stati rimessi come **copie esatte** dei file di Woodland Mansion Replacement. Gli avamposti sono di nuovo attivi, quindi la mappa verso `minecraft:pillager_outpost` è tornata valida e quella del Monumento non è stata rimessa (c'è già nei relitti).

### ✅ Conflitto 2 (RISOLTO) — `worldgen/structure_set/nether_complexes.json` (Incendium, ibo e DnT Nether Fortress Overhaul Retro)
Tre pack ridefiniscono lo **stesso** structure_set vanilla `minecraft:nether_complexes` (quello che governa insieme Fortezza del Nether + Bastione). Vince l'ultimo caricato; l'ordine qui sotto è quello della lista `Enabled` nel `level.dat` di un mondo del pack:

| Ordine | Pack | salt | spacing | separation | Note |
|---|---|---|---|---|---|
| 1 | **Incendium** (`mod_data`) | 30084232 | 16 | 8 | con `exclusion_zone` di 8 chunk verso `incendium:greater_structures` |
| 2 | **ibo** (pack integrato nel jar) | 30084232 | 27 | 4 | rimette i valori vanilla, perché senza strutture di Incendium la sua griglia non serve |
| 3 | **DnT Nether Fortress Overhaul Retro** (`datapacks/`, **vince**) | 30084232 | **16** | **8** | valori modificati a mano, l'originale era 27/4 come vanilla |

**Fix applicato:** modificato direttamente il file `data/minecraft/worldgen/structure_set/nether_complexes.json` **dentro** `datapacks/DnT Nether Fortress Overhaul Retro 2.5.zip` (riscritto lo zip mantenendo intatti gli altri 404 file), portando spacing/separation a 16/8, gli stessi valori di Incendium. La `exclusion_zone` di Incendium non è stata riportata: le sue strutture sono disattivate da `ibo`.

**16/8 è una scelta di design, non più un allineamento.** Quando il fix è stato fatto non si sapeva che ibo ripristina i valori vanilla: l'allineamento a Incendium seguiva una griglia pensata per un Nether con le sue 9 strutture, che nel pack non ci sono. Le Fortezze e i Bastioni più comuni vanno bene comunque e i valori restano 16/8: circa **2,8 volte** più complessi che in vanilla ((27/16)², una cella ogni 256 chunk invece di 729), distribuiti in modo più regolare grazie alla separation più alta. Di conseguenza l'`exclusion_zone` di Hellish Trials verso questo set è abbassata da 10 a 5 chunk (vedi la sezione di Hellish Trials).

Se un giorno si volesse tornare a vanilla, basta togliere il file dallo zip DnT (vince ibo con 27/4) e rimettere 10 chunk in Hellish Trials.

### ✅ "Salt" duplicati che invece sono INNOCUI (voluti dal design delle mod)
Controllando tutti gli 83 file `structure_set` del pack, oltre al conflitto sopra ci sono altri 3 casi di salt duplicato, ma sono tutti innocui:

- **`desert_pyramids` / `desert_ruins`** (salt 239021) e **`jungle_temples` / `jungle_ruins`** (salt 239021, identico anche tra deserto e giungla) — è il meccanismo voluto delle mod DnT: la struttura vanilla viene svuotata con uno "start_pool" speciale (`nova_structures:vanilla_structure_remover`) esattamente sulla stessa griglia dove genera la struttura sostitutiva, cosicché la vecchia venga "rimossa" e la nuova prenda il suo posto nello stesso punto. Nessun conflitto reale.
- **`ocean_monuments` / `trident_trial_monument`** (salt 69846574) — stesso meccanismo di sostituzione pulita.
- **`woodland_mansions` / `illager_manor`** (salt 10387319) — i villaggi non c'entrano: quelli dell'overhaul di ISO (5.16.0.0) usano il salt vanilla 10387312 (spacing 80, separation 50).

---

## ✅ Mod che aggiungono o sostituiscono strutture

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

Il datapack cambia il posizionamento (nel jar: anelli `concentric_rings`, `count` 219):
- `worldgen/structure_set/strongholds.json`: `random_spread` spacing 80 / separation 40, salt 1784520396, come le altre strutture.
- `tags/worldgen/biome/has_structure/stronghold.json`: `replace: true` con solo `#minecraft:stronghold_biased_to` (terraferma + Lush/Dripstone Caves e quello che aggiunge Vanilla Backport). Sotto oceani, fiumi, spiagge e Deep Dark non si generano. Il bioma è controllato all'altezza di partenza, non in superficie.
- `worldgen/structure/stronghold.json`: copia di quella del jar con `project_start_to_heightmap` `WORLD_SURFACE_WG` e `start_height` -64 (la camera del portale parte 64 blocchi sotto la superficie, anche sotto le colline, invece che a Y -15 fissa), `dimension_padding.top` 0 invece di 238 (impediva ai pezzi di superare Y ~81) e `terrain_adaptation` `none` invece di `encapsulate` (ricopriva di terreno i pezzi in superficie). Le scale dei corridoi salgono sempre (+6/+12), così a volte esce in superficie. Senza `encapsulate` caverne e acqua possono tagliare i corridoi. Se DnT aggiorna il file, va ricopiato.

Nei mondi esistenti gli occhi di ender trovano solo gli stronghold del nuovo posizionamento (chunk nuovi); quelli vecchi restano ma non vengono più localizzati.

La cella `stronghold_jail_3x3_room5` (1 su 8) contiene 2 villager disoccupati. Era tolta con un override del pool `stronghold_jail_room`, rimosso con l'overhaul dei villager di ISO: pochi villager prigionieri nelle strutture vanno bene, e senza scambi salvati prendono quelli di ISO.

### DnT — Swamp Hut Overhaul — 🟢 attiva, nessun config dedicato
Sostituisce `swamp_hut`. ☀️ **Superficie**, **Overworld** (palude).

### DnT — Woodland Mansion Replacement — 🟢 attiva, nessun config dedicato
Sostituisce `mansion`. ☀️ **Superficie**, **Overworld** (dark forest). Trasforma `minecraft:mansion` in una struttura vuota (`nova_structures:vanilla_structure_remover`) con lo stesso structure set (salt 10387319) dell'Illager Manor, così le mappe della magione puntano al manor.

Fix nel datapack:
- **Villager tenuti**: lo slot mob condiviso `illager_mob` ha 1 villager su 22 elementi, e le stanze `mansion_secret_room3` e `mansion_middle_room_basement8` ne hanno uno incorporato. Sono pochi e disoccupati, senza scambi salvati, quindi nessun override.
- **Loot table mancanti**: tre casse dei giardini usano loot della mod DnT completa (`nova_structures:chests/dungeon_6`, `dungeon_7`, `undead_crypts_grave`), definite nel datapack come la tabella `generic` del manor.
- **Conflitto con Ancient City Overhaul** su `map_chest`, `secret_room` e `library_chest`: vedi Conflitto 1.

### DnT — Nether Fortress Overhaul Retro *(nuova scoperta — è una datapack, non un jar!)*
File: `datapacks/DnT Nether Fortress Overhaul Retro 2.5.zip`. Sostituisce `fortress.json` vanilla. ☀️ **Superficie** (del Nether, sospesa sulla lava come da vanilla), **dimensione Nether**. 🟢 **Attiva** — è dentro `datapacks/`, che in `config/global_packs.toml` è impostato come `required`, quindi sempre caricata in ogni mondo.

### Incendium — 🔴 **strutture disattivate** (biomi attivi)
`Incendium_1.21.x_v5.4.4.jar`. **Dimensione: Nether** (biomi custom `incendium:infernal_dunes`, `incendium:withered_forest`, ecc.).

**Correzione:** avevo detto che tutte e 9 le strutture generano — sbagliato. La mod `ibo-3.2.0-neoforge-1.21.1.jar` ("Incendium Biomes Only") **è attiva** in questo pack e filtra via tutto ciò che è sotto il namespace `incendium` in `worldgen/structure`, `worldgen/structure_set` e `worldgen/template_pool` (oltre a loot table, advancement, ricette e funzioni) — inclusi `incendium:lesser_structures.json` e `incendium:greater_structures.json`, cioè **i due structure_set che piazzano le 9 strutture giganti**. Senza quei structure_set, nessuna delle 9 strutture (Abandoned Tower, Forbidden Castle, Infernal Altar, Nether Reactor, Piglin Village, Pipeline, Quartz Kitchen, Ruined Lab, Sanctum) genera. **Restano solo i biomi Nether custom di Incendium** — che è esattamente lo scopo dichiarato di ibo ("Disables everything but biomes in Incendium").

Il filtro di ibo colpisce solo il namespace `incendium`, quindi i file di Incendium sotto `minecraft` restano:
- **`nether_complexes.json`**: ibo lo sovrascrive con i valori vanilla, ma lo zip DnT carica dopo e vince con 16/8 (vedi Conflitto 2).
- **Tag dei biomi `has_structure/nether_fortress` e `has_structure/bastion_remnant`**: i biomi di Incendium esistono, quindi questi tag decidono quale complesso può nascere in ognuno. Nella cella della griglia la struttura estratta che non è ammessa dal bioma lascia il posto all'altra.

| Bioma di Incendium | Fortezza | Bastione |
|---|---|---|
| `infernal_dunes`, `toxic_heap` | ✅ | ❌ |
| `ash_barrens`, `withered_forest` | ❌ | ✅ |
| `inverted_forest`, `weeping_valley`, `volcanic_deltas` | ✅ | ✅ |

### Philips' Ruins — 🟢 attiva, nessun config dedicato
`Philips-Ruins1.21.1-2.0-NeoForge.jar`. **Dimensione: solo Overworld** (biomi vanilla come forest, jungle, swamp, plains, deep_dark, lush_caves, ecc.).

| Struttura | Posizione |
|---|---|
| Ancient Crypt, Ancient Ruins, Ancient Towers, Field Stone Ruins (+rocks), Level One/Two/Three Ruins (+pool), Pumpkin Ruins, Rare Ruin | ☀️ Superficie |
| Ancient Dungeon, Lost Soul City, Underground Structures | ⛏️ Sotterranea |
| Lost Soul Dungeon | ⛏️ Sotterranea |
| Ocean Fortress, Ocean Ruins | 🌊 Subacquea |

Il jar ha anche i tag `has_structure/start_nether_dungeon_biomes` (biomi del Nether) e `start_nether_ruin_biomes`, ma nessuna struttura li usa: Philips' Ruins non genera niente nel Nether.

### VanillaBackport — 🟢 attiva (via config)
`VanillaBackport-neoforge-1.21.1-1.1.7.10.jar`. Non registra vere strutture jigsaw ma pezzi/feature decorative:
- **Pale Oak** (Pale Garden): ☀️ Superficie, **Overworld** — attivo, `pale_garden = true` in `vanillabackport-common.toml`.
- **Sulfur Springs**: ⛏️ Sotterranea (sopra le Sulfur Caves), **Overworld** — attivo, `has_sulfur_springs = true` in `vanillabackport-common.toml`.

### abridged — 🟢 attiva (via config)
`abridged-2.0.2-neoforge-21.1.jar`. **Bridge**: ☀️ Superficie (attraversa ravine/canyon), **Overworld**. Config `abridged.json`: `"frequency": 0.8` (80% di possibilità quando viene trovata una posizione valida) — non è disattivato.

**Override:** la variante `canyon/pillager_infested` (ponte con pillager) è disattivata svuotando il tag bioma `abridged:has_bridge/pillager_infested` in `datapacks/survivalreimagined/data/abridged/tags/worldgen/biome/has_bridge/pillager_infested.json`.

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

### Ecologics — 🟢 attiva, nessun config di worldgen
`ecologics-1.21.1-2.3.8.jar`. Aggiunge la **Desert Ruin** (`ecologics:desert_ruin`, ☀️ superficie, solo bioma `minecraft:desert`, spacing 20 / separation 8). **Overworld.** La cassa di `chest_house` usa la loot table `minecraft:chests/desert_pyramid`, gli altri pezzi hanno solo vasi. I filoni d'oro del Nether (`add_ore_vein_nether_gold`) sono disattivati da un override in `datapacks/survivalreimagined/data/ecologics/neoforge/biome_modifier/`.

### formationsnether — 🟢 attiva, nessun config dedicato
`formationsnether-1.0.5b-mc1.21+.jar`. **Dimensione: Nether** (bioma `basalt_deltas` e altri).

| Struttura | Posizione |
|---|---|
| Basalt Hut, Ore Shard | ⛏️ Sotterranea |
| Tutte le altre 18 (Blackstone Castle/Remnant, Campsite, Checkerboard Temple, Flaming Pillar, Large House, Large/Small Pedestal, Large Tree, Nether Wart Field, Obsidian Pillar, Parkour Challenge, Quartz Spikes, Respawn Anchor Altar, Rib Cage, Small Fire/Lava Arena, Small Lava Shrine, Sphere Cage) | ☀️ Superficie |

Tre structure_set, nessuna `exclusion_zone`:

| Set | Strutture | spacing/separation |
|---|---|---|
| `formationsnether:common` | le 18 strutture piccole (peso 1 ciascuna) | **5/2**, molto densa |
| `formationsnether:rare` | Blackstone Castle, Checkerboard Temple | 15/10 |
| `formationsnether:ore_shards` | Ore Shard | 4/1 |

### Hellish Trials — 🟢 attiva, nessun config dedicato
`HellishTrials-neoforge-1.0.5.jar`. **Nether Trial** (`hellish_trials:nether_trial`, jigsaw), la versione del Nether delle Trial Chambers con vault ominosi. **Dimensione: Nether** (tag `hellish_trials:has_structure/nether_trial_biomes`).

Structure set `hellish_trials:minor_structures`: spacing 45, separation 25, `exclusion_zone` verso `minecraft:nether_complexes`. **Override** in `datapacks/survivalreimagined/data/hellish_trials/worldgen/structure_set/minor_structures.json`: `chunk_count` da 10 a 5. Con la griglia 16/8 di Fortezze e Bastioni (vedi Conflitto 2), 10 chunk escludevano quasi tutte le posizioni (sopravviveva circa lo 0,4% dei tentativi). Le rune nei suoi vault ominosi sono aggiunte con un modifier `runeenchanting:rune_loot` nel datapack (vedi `CLAUDE.md`).

### Moog's Nether Structures — 🟢 attiva (config in `moogs_structures.json`)
`MoogsNetherStructures-universal-1.21-3.1.1.jar` (libreria `MoogsStructureLib`). **Dimensione: Nether**, 50 strutture jigsaw in 40 structure_set separati, con il placement `moogs_structures:advanced_random_spread`. Nessuna ha una `exclusion_zone` verso `nether_complexes`, quindi possono nascere vicino o sopra a Fortezze e Bastioni.

| Biomi (tag `mns:has_structure/...`) | Strutture | spacing/separation |
|---|---|---|
| Tutto il Nether | Very Small Nether Brick (3 varianti), Very Small Blackstone (4), Circle Nether Brick, Leafy Rubble, Medium Blackstone, Small Nether Brick, Shrine/Smoking Shrine, Soul Fire | 22-25 / 11-20 |
| Tutto il Nether | Large Blackstone Pillars/Walls, Large Nether Brick, Ruined Portal, Lava Pool, Sandy Skull, Medium House (2) | 27-44 / 11-36 |
| Tutto il Nether | Train, Copper Tower, Nether Wart Farm, 6 Bridge, Nether Tower | 65-115 / 25-70 |
| Tutto il Nether | **Mega Fortress** | **116/76** |
| Tutto il Nether | **Mega Arenas**: Small Arena (peso 5), Large Arena (3), Dragon Arena (1) | **150/100** |
| Crimson | Crimson Forge, Crimson Lava Well, Medium Crimson Fungus (2), Medium Crimson Well, Sword | 22-45 / 12-42 |
| Warped | Large House 1, Medium Warped Fungus (2), Medium Warped Well, Warped Dome, Warped House, Warped Pool | 24-42 / 13-38 |
| Nether Wastes | Giant Skull | 54/46 |

Config `config/moogs_structures.json`: `replace_nether_fortress = false`, quindi la **Mega Fortress si aggiunge** alla Fortezza DnT invece di sostituirla (con il preset attivo la Fortezza vanilla sparirebbe e la Mega Fortress passerebbe a 30/12). Moltiplicatori di frequenza tutti a 1.0, nessuna struttura disattivata. Le rune nei suoi vault sono aggiunte via il tag `survivalreimagined:loot/nether_vault` (vedi `CLAUDE.md`).

### Immersive Gateways — 🟢 attiva, nessun config on/off (solo parametri di distanza)
`immersive_gateways-neoforge-0.0.6.jar`. ☀️ Superficie, **solo Overworld** — nonostante il file `immersive_gateways.json` elenchi colori anche per biomi Nether/End (badlands, cherry_grove, desert, ice, jungle, mangrove_swamp, mountain, mushroom, plains, swamp: 10 biomi, tutti Overworld). Config regola solo `minDistance`/`maxDistance` tra i gateway (1024–8096 blocchi), non un enable/disable.

### ✅ FIX APPLICATO — loot troppo forte
L'unica loot table (`immersive_gateways:chests/default`, 4-8 estrazioni) aveva il 34% di possibilità **per estrazione** di un pezzo di equipaggiamento dorato incantato (9 voci su ~25) — ~92% delle casse ne davano almeno uno, in media ~2. Generano con spacing 32/separation 8 (densità da villaggio). Sostituita in `datapacks/survivalreimagined/data/immersive_gateways/loot_table/chests/default.json` con una copia di `philipsruins:chest/level_one_ruins_loot` (già riequilibrata) — niente più oro incantato, oggetti coerenti con una struttura di superficie comune.

### Incubation — 🟢 attiva, pollai disattivati
`incubation-1.21.1-5.0.2.jar`. Pollaio ("chicken coop") aggiunto ai pool dei **villaggi** vanilla (desert/plains/savanna/snowy/taiga). ☀️ Superficie, **Overworld**.

**Disattivati:** il pollaio viene aggiunto (via remolder di Blueprint, `data/incubation/remolders/`) anche ai pool `village/<bioma>/zombie/houses`, gli unici usati dai villaggi abbandonati dell'overhaul di ISO. Porterebbe galline e Hay Nest (rimossi dal pack) in villaggi che non devono avere animali: i 10 remolder sono sovrascritti con `"type": "noop"` in `datapacks/survivalreimagined/data/incubation/remolders/`.

### InsaneSurvivalOverhaul — 🔴 **DISATTIVATA**
`insanesurvivaloverhaul-5.7.1.0.jar`. **Echo Pillar**: ☀️ Superficie (genera a `y=0` proiettata sull'ocean floor), **Overworld**. In `config/insanesurvivaloverhaul/common.toml`:
```
[Death]
"Enable Echo pillar" = false        # <- interruttore master: SPENTO
    [Death."Echo pillar"]
    "Echo pillars" = true            # <- sub-toggle del datapack, ma ignorato perché il master è false
```
**La struttura non genera attualmente nel pack**, nonostante il sotto-toggle del datapack sia `true`.

### Sawmill — 🟢 attivo, casa del falegname disattivata
`sawmill-1.21-1.8.0-neoforge.jar`. Casa del falegname aggiunta ai pool dei **villaggi** vanilla (13 varianti di bioma). ☀️ Superficie, **Overworld**. Config (`sawmill-common.toml`) ha solo `repurposed_structures_compat = true`, nessun on/off per la struttura stessa.

**Disattivata:** la casa del falegname viene aggiunta anche ai pool `zombie/houses` e contiene la Sawmill (job site del Carpenter) e una cassa con loot, mentre i villaggi abbandonati di ISO non hanno job site. `carpenter_house_spawn_rate = 0` in `config/sawmill-common.toml`. Il Carpenter resta ottenibile (villager curati vicino a una Sawmill) e ha scambi in stile ISO (vedi `CLAUDE.md`).

### Supplementaries — 🔴 **ENTRAMBE DISATTIVATE**
`supplementaries-1.21.1-3.8.8-neoforge.jar`.

**adventuredungeons** ha delle vere explorer map:

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

- **Villaggi e Avamposti Pillager: modificati da ISO.** Dalla 5.16.0.0 il pacchetto integrato `villagers_overhaul` sostituisce `disable_long_noses`: villaggi abbandonati (solo zombie villager, spacing 80/separation 50) e avamposti con una guarnigione unica, senza respawn di pillager.
- **Nessun'altra struttura vanilla è disattivata.** Controllato specificamente in `insanesurvivaloverhaul` per buried treasure, ruined portal, trail ruins, trial chambers, nether fossil, bastion, igloo, ocean ruins, pozzo del deserto: nessun toggle, nessuna menzione.
- **Città di Fine (End City): AUMENTATE, non ridotte.** Altro pacchetto integrato di ISO, `increased_end_cities` (`"Increase end cities" = true`, attivo): spacing passa da 20/11 (vanilla) a 11/7 — città di fine molto più dense.
- **Fortezza del Nether e Bastione: più comuni, per scelta.** `nether_complexes` è a 16/8 invece di 27/4 (vedi Conflitto 2).
- **Correzione: `ibo` ("Incendium Biomes Only") È attiva.** Avevo controllato nel posto sbagliato (cartella `resourcepacks/` sul disco e lista `resourcePacks` di `options.txt`) — ma il filtro di ibo agisce sul lato **dati** (strutture/loot/structure_set), non sugli asset, quindi va cercato tra le datapack attive, non tra i resource pack visivi. La mod (di Naomi Roberts, dipendenza obbligatoria su Incendium) si registra ed è sempre attiva finché è installata, senza bisogno di estrarla a mano. Effetto reale: **le 9 strutture giganti di Incendium sono disattivate**, restano solo i suoi biomi Nether — vedi sezione Incendium sopra, corretta di conseguenza.

### ✅ FIX APPLICATO — Relitti (Shipwreck) più rari
`minecraft:shipwrecks` (nessuna mod lo toccava). Override in `datapacks/survivalreimagined/data/minecraft/worldgen/structure_set/shipwrecks.json`:

| | spacing | separation |
|---|---|---|
| Vanilla | 24 | 4 |
| **Ora** | **48** | **8** |

Raddoppiati entrambi (stesso rapporto, stesso salt/strutture vanilla) — relitti circa la metà frequenti. Fammi sapere se vuoi tararli diversamente.

---

## 🗺️ FIX APPLICATO — Explorer map (strutture sotterranee + Monumento/Magione)

Aggiunte mappe per 7 strutture (Ancient City DnT, le 4 sotterranee di Philips' Ruins, più **Monumento Oceanico e Magione/Illager Manor** per colmare il buco lasciato dall'assenza del Cartografo — Stronghold escluso, ha già gli occhi di ender). Meccanismo: **NeoForge Global Loot Modifiers** (`neoforge:add_table`), lo stesso sistema già usato in questo pack da Bits and Balance/Quark/RuneEnchanting — aggiunge le mappe come pool *extra* alle loot table esistenti, senza toccare/sovrascrivere il loro contenuto originale. Fa eccezione la mappa del Monumento, inserita sostituendo la voce morta "Pillager Outpost Map" nel `map_chest.json` della Magione/Ancient City (vedi fix del conflitto qui sopra).

| Mappa verso | Trovabile in | Probabilità |
|---|---|---|
| `minecraft:ancient_city` (DnT) | Buried Treasure vanilla | 60% a tesoro |
| `minecraft:mansion` (Illager Manor, DnT) | Cassa "di valore" dei relitti (`shipwreck_treasure`) | 60% a cassa |
| `minecraft:monument` (Trident Trial Monument, DnT) | Cassa `map_chest` dentro Ancient City/Magione (al posto della morta "Pillager Outpost Map") | 50% (1 tra 2 voci nel pool) |
| Ancient Dungeon, Lost Soul City, Lost Soul Dungeon, Underground Structures (Philips' Ruins) | Casse `ruin_loot`, `ancient_ruins_loot`, `level_one_ruins_loot` di Philips' Ruins | 15% a mappa, per cassa |

File in `datapacks/survivalreimagined/data/neoforge/loot_modifiers/`, `data/survivalreimagined/loot_modifiers/`, `data/survivalreimagined/loot_table/inject/` e `data/minecraft/loot_table/chests/illager_mansion/map_chest.json`. Per Philips' Ruins ho scelto le 3 loot table di superficie più diffuse invece di toccarle tutte singolarmente.

---

## 🗑️ Dungeons and Taverns (mod completa) — installata, analizzata, poi rimossa

`dungeons-and-taverns-v4.4.4 [NeoForge].jar` (96 strutture nuove) e il suo addon `lootintegrations_dnt-2.6.jar` sono stati **rimossi**: aggiungevano incantesimi custom non compatibili con Rune Enchanting (che sostituisce automaticamente solo gli incantesimi vanilla). Poi è stato rimosso anche `DnT-woodland-mansion-replacement-v1.2 [NeoForge].jar`, reinstallato con l'overhaul dei villager di ISO. Restano installati: Ancient City, Desert Temple, Jungle Temple, Ocean Monument, Stronghold, Swamp Hut, Woodland Mansion.

**Ripulito dal datapack** (override esclusivi della mod completa, ormai inutili senza di essa): `villages_birch/jungle/swamp`, `illager_camp`, `taverns`, `swamp_structure` (Witch Villa), `badlands_miner_outpost`, `illager_hideout`, `remnants`, `stray_fort_fortress`, `lone_citadel` (mob+frame).

### 🟢 Magione (Woodland Mansion) — riattivata (vanilla)
Senza nessuna mod di sostituzione, la Magione è tornata 100% vanilla — e la generazione vanilla di vindicator/evoker/witch **non è editabile via datapack**: ho estratto e controllato tutti i 73 pezzi `.nbt` vanilla dal jar di Minecraft, zero mob incorporati nei pezzi (a differenza di DnT). La popolazione mob della Magione vanilla è **scritta direttamente nel codice Java** di Minecraft (una delle poche strutture ancora non completamente data-driven), quindi non c'è alcun file datapack modificabile per toglierli.

Scelta presa: **disattivata del tutto** (`data/minecraft/worldgen/structure_set/woodland_mansions.json` con `"structures": []`), coerente col principio "niente gente dal naso lungo". Ripuliti di conseguenza anche: i pool `illager_mansion` (ormai orfani, nessuna mod li usa più), le loot table `illager_mansion/map_chest.json`/`secret_room.json`/`library_chest.json` (mai più generate), e la mappa della Magione nei relitti (`shipwreck_maps.json`, ora punterebbe a una struttura disattivata) — resta solo la mappa del Monumento Oceanico lì.

**Riattivata con l'overhaul dei villager di ISO** (5.16.0.0): gli illager fanno di nuovo parte del design (fonte finita di smeraldi e totem). `woodland_mansions.json` ora contiene la voce vanilla `minecraft:mansion`. Le loot table e la mappa nei relitti rimosse allora non sono state ripristinate: la Magione usa le loot table vanilla. Resta da valutare una mod che rinnovi le Magioni (report di ISO `report_villagers_modpack.md` §6).

**Sostituita di nuovo da DnT Woodland Mansion Replacement** (Illager Manor): vedi la sezione della mod. L'override di `woodland_mansions.json` è stato tolto, perché identico a quello vanilla e a quello del jar.

---

## Osservazioni per il pack

- **Strutture disattivate nel pack: Echo Pillar** (ISO, `"Enable Echo pillar" = false`), **Galleon** e **Road Sign** (Supplementaries, entrambe spente in `supplementaries-common.toml`). Tutte le altre strutture elencate sopra sono attive.
- **8 strutture vanilla sono sostituite** dalle mod DnT (7 jar + 1 datapack): Città Antica, Piramide del Deserto, Tempio della Giungla, Monumento Oceanico, Fortezza, Capanna della Strega, Magione Silvestre (Illager Manor), **Fortezza del Nether** (quest'ultima dentro `datapacks/`, non nei jar).
- **Concentrazione nel Nether**: ci generano Fortezza DnT e Bastione (16/8, più comuni di vanilla per scelta), formationsnether (set `common` a 5/2), Moog's Nether Structures (50 strutture, da 22/11 a 150/100, più la Mega Fortress) e il Nether Trial di Hellish Trials (45/25). Quasi tutte sono "di superficie" nel Nether, non sepolte. Solo Hellish Trials ha una `exclusion_zone` verso Fortezze e Bastioni: le altre possono sovrapporsi. Incendium **non** è in questa lista: le sue 9 strutture sono disattivate da `ibo`, restano solo i suoi biomi. Amplified Nether cambia solo il terreno, ma questo influisce su dove le strutture di superficie riescono a posizionarsi.
- ~~Overworld sovraffollato di rovine generiche~~ — **ritrattato**: in gioco non hai trovato troppe strutture, e i numeri lo confermano. Guardando gli spacing/separation reali (estratti dai `structure_set`): adventuredungeons ha spacing 30-40, Philips' Ruins varia da 40 a 360 (Rare Ruin, come dice il nome, è molto rara). YungsExtras non usa nemmeno il sistema a griglia (`structure_set`) ma decorazioni via `biome_modifier`, quindi non compete per lo spazio con le altre. La mia frase precedente era una supposizione non verificata sui numeri — la densità reale non sembra eccessiva.
- Nessuna struttura tra quelle elencate genera nell'**End** — nessuna mod del pack tocca quella dimensione.
- **Nessuna struttura del pack ha una propria explorer map** (vedi sezione dedicata sopra).
- **Due conflitti reali di sovrascrittura file** trovati tra mod DnT tra loro e tra Incendium/DnT — **entrambi ora risolti**: vedi sezione "⚠️ Conflitti reali trovati" sopra per i dettagli (loot table della Magione con mappe verso strutture inesistenti → sistemata con un unico override; griglia di generazione di Fortezza/Bastione del Nether ridefinita da Incendium, ibo e DnT con parametri diversi → fissata a 16/8 nello zip di DnT, che vince).
