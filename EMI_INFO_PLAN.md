# Piano: pagine EMI info per tutti gli oggetti non decorativi

Obiettivo: ogni blocco o oggetto con una funzione (vanilla e mod) ha una pagina `emi:info`. Restano fuori quelli puramente decorativi e quelli la cui funzione è già evidente da ricette e tooltip. Le pagine devono dare un'infarinatura anche a chi conosce poco Minecraft, senza dover cercare su internet: le meccaniche vanilla che un veterano conosce (redstone, pozioni, End, Trial Chambers) hanno comunque una pagina.

## Stato di partenza (2026-11-24)

- **Pack** (`resourcepacks/survivalreimagined_lang`): 162 pagine. Supplementaries 79, Vanilla Backport 19, Naturalist 16, Amendments 14, Ecologics 10, Storage Drawers 5, Quark 3 (Crate, Magnet, Pipe), Vanilla 3 (Sculk, Sculk Sensor, Calibrated Sculk Sensor), più singole pagine per Bits and Balance, Boatload, Clayworks, Hang Glider, Heartstone, Labels, Map Atlases, Sawmill, Shields+ e Straw Statues.
- **ISO** (pagine nel suo plugin EMI, testi in `emi.info.insanesurvivaloverhaul.*`): 37 pagine sui suoi oggetti e sui vanilla che cambia. Tra queste: Daggers, Shortbow, Beacon, Beds, Hoes, Wooden equipment, Conduit, Fishing Rod, Sweet Berry Bush, Cake, Sponge, Campfire, Spawner, Bone Meal, Rich Farmland, Totem of Undying, Zombie Villager cure, Name Tags, seeds, Powered Rails, angoli del portale, falling blocks, Explosive Barrel, Mining Charge ed Echo Lantern.
- **Quark**: ha i suoi suggerimenti (`quark.jei.hint.*`, `"Enable Jei Hints" = true`), registrati come info di JEI. JEI è installato insieme a EMI: da verificare se EMI li mostra.
- **Senza nessuna pagina**: Quark Oddities (Totem of Holding, Backpack disattivato), Incubation, Stamina, Better Tridents, Progressive Bosses, Hellish Trials, RuneEnchanting e circa il 98% degli oggetti vanilla.

## Regole (valgono per tutte le fasi)

- Un file per pagina in `assets/emi/recipe/additions/<modid>_<nome>.json`. I testi vanno come chiavi `emi.info.<modid>.<nome>[.n]` in `assets/survivalreimagined/lang/en_us.json`.
- Le varianti si raggruppano in un'unica pagina con più `stacks` o con un tag `#item:` (es. tutti i letti, tutte le asce).
- Stile: niente numeri esatti, salvo quando servono per usare la meccanica. Niente "dove trovarlo" per gli oggetti comuni in superficie; sì per quelli sotterranei, legati a una struttura o a un mob. Sì anche per tutti gli oggetti che si ottengono da una loot table (chest, drop dei mob, pesca, archeologia), perché EMI non le mostra.
- **Descrivere il comportamento in questo pack, non quello vanilla.** Prima di scrivere una pagina si controllano config di ISO (`common.toml`, `server.toml`), datapack, `item_components`, gamerule in `WSCommands.toml` e le altre mod che toccano lo stesso oggetto (Amendments, Supplementaries, Quark, Bits and Balance).
- **Dove va la pagina**:
  - comportamento dovuto a ISO (o a un'altra mod di Insane96: Enhanced AI, Progressive Bosses, RuneEnchanting, Stamina, No Hunger, ...) → non va scritta nel pack. Si aggiunge alla sezione [Da implementare nelle mod](#da-implementare-nelle-mod) con oggetto, comportamento da spiegare e da dove viene (opzione di config o classe). Le implementa Insane96 nei plugin EMI delle mod;
  - comportamento dovuto alla combinazione del pack (datapack, config, più mod insieme) → nel resource pack.
  - Se ISO ha già una pagina per l'oggetto, si aggiunge una seconda pagina nel pack solo per quello che ISO non dice, senza ripetere.
- **Niente pagina se il giocatore lo scopre già da solo**: da una ricetta in EMI, da un advancement, da un tooltip o al primo utilizzo. Una regola che riguarda come funziona una ricetta va nella visualizzazione della ricetta, non in una pagina.
- Una pagina per gli oggetti rimossi (`insanelib:creative_removal`) non serve.
- Un commit per lotto, con una voce nel `changelog.md` sotto `# Upcoming` (es. "Added EMI info pages for vanilla redstone components").

## Fase 0 — Verifiche e inventario (1 sessione)

**Fatta (2026-11-24).**

- I suggerimenti di Quark compaiono in EMI per le funzioni attive (provati Bottled Cloud ed Emerald Block). Per Quark servono quindi solo i buchi. Le pagine del pack su Crate, Magnet e Pipe ripetono in parte i suggerimenti di Quark: vanno ridotte a quello che Quark non dice (Fase 4).
- Inventario: `inventory.py` nello scratchpad della sessione produce `inventario.csv` (`id; mod; nome; coperto da; decisione proposta`). Su 3725 oggetti: 706 coperti, 153 rimossi, 201 tecnici, 1371 decorativi, 832 in 86 gruppi, 462 da valutare (Minecraft 280, Quark 42, Supplementaries 42, ISO 22, Naturalist 18, altre circa 58). Tra i 42 di Quark ci sono ancora oggetti di moduli spenti, che Quark nasconde da solo: Crab (categoria mobs spenta), Matrix Enchanter, Monster Box, Hammer.

1. **In gioco**:
   - i suggerimenti di Quark compaiono in EMI? Se sì, per Quark servono solo i buchi e le correzioni. Se no, bisogna scegliere se riportarli nel pack o lasciar perdere;
   - i suggerimenti di Quark che descrivono funzioni disattivate o cambiate nel pack vanno nascosti o corretti.
2. **Inventario**: uno script (nello scratchpad) legge dai jar le chiavi lang `item.*` e `block.*` e gli ID registrati, e produce un CSV con `id, mod, coperto da (pack / ISO / Quark / nessuno), categoria proposta, decisione`. La decisione è una tra *pagina*, *gruppo X*, *decorativo*, *ovvio* o *rimosso*.
3. **Revisione tua** del CSV: decidi cosa è "ovvio" e cosa merita una pagina. È il passo che fissa quanto è grande tutto il resto.

## Fase 1 — Vanilla cambiato dal pack o da ISO, non ancora coperto (1-2 sessioni)

**Fatta (2026-11-24).** Quasi tutti i candidati vengono da ISO o No Hunger e sono finiti in [Da implementare nelle mod](#da-implementare-nelle-mod). Nel pack:

- `supplementaries_ash` (Ash e Burnt Log): il fuoco trasforma quasi tutti i log in Burnt Log, e la Ash si ottiene rompendoli (loot table del datapack). La ricetta "log che bruciano → Ash" mostrata in EMI da Supplementaries è quindi fuorviante;
- `minecraft_wet_sponge`: dove trovarla, con più spugne dagli Elder Guardian più forti (loot table di Progressive Bosses sovrascritte dal pack).

Già a posto: Crying Obsidian (`portal_corners` di ISO) e Spawner (ISO mostra la riga "reactivate" solo se il Reactivator è attivo). Fletching Table e Recycling hanno già le loro categorie o ricette in EMI.

Il Totem of Holding non ha un oggetto: è solo un'entità, il modello in `models/item/extra` è usato per il rendering. Non può avere una pagina EMI, quindi la spiegazione della morte va appoggiata ad altro (vedi la voce della penalità alla morte).

## Fase 2 — Vanilla con meccaniche poco evidenti (3-4 sessioni)

Un lotto (e un commit) per categoria:

1. **Navigazione e strumenti**: Compass, Recovery Compass, Lodestone, Clock, Spyglass, Map / Cartography Table, Bundle, Brush e blocchi sospetti, Goat Horn. **Fatto (2026-11-24)**, più Obsidian. La pagina del Clock è quella di Supplementaries, allargata. Brush e blocchi sospetti non servono.
2. **Redstone**: Observer, Comparator, Repeater, Target, Daylight Detector, Note Block, Sculk Shrieker, Crafter, Lightning Rod, Tripwire, Piston e blocchi non spostabili, Hopper, Dropper / Dispenser (comportamenti speciali), Rail speciali. **Fatto (2026-11-24)**. Tripwire Hook e Lightning Rod hanno una riga vanilla nelle pagine di Amendments e Vanilla Backport. Slime e Honey Block sono spiegati nella pagina del Piston, Rail e Powered Rail non servono (ovvio e ISO).
3. **Blocchi funzionali**: Beacon (se ISO non basta), Conduit, Respawn Anchor, Lectern, Jukebox, Composter, Cauldron, Brewing Stand, Smithing Table e Trim Templates, Loom, Stonecutter, Bell, Scaffolding, Bee Nest / Beehive e Honey, Ender Chest, Shulker Box. **Fatto (2026-11-24)**. Lectern, Jukebox, Cauldron e Bell hanno una riga vanilla nelle pagine di Amendments. Netherite Upgrade e Trim Template hanno una pagina ciascuno con le fonti, prese dalle loot table effettive (DnT, Incendium, Moog's, Adventure Dungeons, Hellish Trials, Bits and Balance). Non servono: Beacon (ISO), Shulker Box (il tooltip di Quark ne mostra il contenuto), Loom, Stonecutter, Scaffolding e Composter (ovvi nell'inventario). Il Blast Armor Trim di Supplementaries si trovava solo nei Galleon, spenti nel pack (`galleon = false`): ora si pesca come tesoro, e la sua pagina lo dice.
4. **Materiali e drop non ovvi**: Echo Shard, Disc Fragment, Heart of the Sea, Nautilus Shell, Sniffer Egg, Armadillo Scute, Breeze Rod, Heavy Core, Trial Key / Ominous Trial Key, Ominous Bottle, Dragon Breath, Shulker Shell, Phantom Membrane. **Fatto (2026-11-24)**, più Trial Spawner, Vault, Nether Star, Wither Rose, Ancient Debris, Eye of Ender ed End Portal Frame, End Crystal, ametista e una pagina per tutti i dischi vanilla. Fonti prese dalle loot table effettive. Non vanno nel pack perché li cambia ISO: Heart of the Sea (Divine Fragment), Shulker Shell, Ender Pearl, Armadillo e Turtle Scute (vedi sotto). Netherite Scrap non serve: la fusione è in EMI.
5. **Equipaggiamento**: Elytra, Trident, Mace, Wind Charge, Turtle Helmet, Shield, Crossbow, Firework Rocket / Star. **Fatto (2026-11-24)**. Il Trident Fragment di Better Tridents sta nella pagina del Trident (Drowned dal datapack, Elder Guardian). Le Elytra vengono solo dalle End City: Incendium nel pack ha solo i biomi. Non servono: Crossbow, Firework e Shield (ovvi, lo scudo ha già la pagina di Shields+). Turtle Helmet: l'Oxygen Bonus di ISO si vede nel tooltip. Le modifiche di ISO a Elytra e Crossbow sono sotto.
6. **Piante e agricoltura**: crescita e Bone Meal (dove ISO non arriva), Sugar Cane, Cactus, Bamboo, Kelp, Chorus, Nether Wart, Sea Pickle, Glow Berries, Pitcher, Torchflower, Moss / Azalea. **Fatto (2026-11-24)**. Nel pack: Bone Meal (i blocchi aggiunti da Universal Bone Meal, oltre alla pagina di ISO), Nether Wart, Chorus, semi dello Sniffer (Torchflower e Pitcher), Frogspawn e Froglight, Carrot e Warped Fungus on a Stick. Non servono (ovvi nel CSV): Sugar Cane, Cactus, Bamboo, Kelp, Sea Pickle, Glow Berries, Moss e Azalea. Il raccolto col tasto destro di Quark (`Simple Harvest`) è spento. Golden Carrot e Glistering Melon nemmeno: la distillazione è in EMI.

## Fase 3 — Mod senza copertura (2-3 sessioni)

- **Quark e Quark Oddities**: dipende dalla Fase 0. In ogni caso serve il Totem of Holding, una pagina chiave per la morte nel pack.
- **Incubation** (Egg Crates, cibi), **Better Tridents** (Trident Fragment), **Hellish Trials** (Ominous Vault e loot).
- **RuneEnchanting**, **Stamina**, **Progressive Bosses**: sono mod di Insane96, quindi le loro pagine vanno in [Da implementare nelle mod](#da-implementare-nelle-mod).
- **Buchi nelle mod già coperte**: per esempio Bits and Balance (2 pagine), Clayworks, Boatload, Sawmill, Ecologics, Vanilla Backport. Si controllano gli oggetti non decorativi rimasti senza pagina.

**Fatta (2026-11-24)**, partendo dagli oggetti "dubbio" del CSV:

- Pagine nuove: Cartographer's Quill (Supplementaries con Quark: sostituisce le mappe del tesoro e degli esploratori nelle chest), Spider Head (Creeper carico, e la stessa riga sulla pagina della Enderman Head), Fat, Tooth, Morsel e Lizard Tail di Naturalist (da quali mob), Golden Dandelion di Tiny Takeover Backport (blocca la crescita dei cuccioli), uova e Bird Cage di Vibrant Parrots.
- Aggiunti a pagine esistenti: Hanging Coconut (Coconut), Bamboo Raft with Cannon (Cannon Boat), Tinted Jar (Jar), Gold Gate (Gold Door e Iron Gate).
- Già a posto: Soap, Soap Block e Bubble Blower (pagine ripristinate con la Ash), Trident Fragment (pagina del Trident), Ominous Vault di Hellish Trials (pagina del Vault). Quark: bastano i suoi suggerimenti; il Totem of Holding non ha un oggetto (vedi Fase 1). Incubation: i suoi 4 oggetti sono "ovvio".
- Non servono: Ashen Basalt (dà Basalt, citato nella pagina della Ash), Barnacles, Checker Block, Flax Bale, Gold Bars, Seashell (decorativi), Tater in a Jar, Speedometer (senza ricetta, mostra la velocità al primo uso), Snail Eggs (non si raccolgono).
- Fat e Tooth: le pagine dicono da dove vengono. Gli usi (Candle con la Fat al posto della Honeycomb, 2 Bone Meal da un Tooth) sono ricette del datapack, che EMI mostra già.

## Fase 4 — Revisione (1 sessione)

- Rileggere le 162 pagine esistenti alla luce di quelle nuove: doppioni con ISO o Quark, testi diventati sbagliati per cambi di config.
- Controllo in gioco a campione (EMI → tasto info) dei lotti più grandi.

**Rilettura fatta (2026-11-24)**, il controllo in gioco resta da fare. Corretto:

- Crate, Magnet e Pipe ridotte a quello che i suggerimenti di Quark non dicono;
- trim Sentry e Vex: "Woodland Mansion" diventa "Illager Manor", come nella pagina del Goat Horn.

Nessun doppione con le pagine di ISO: Conduit, Bone Meal e Obsidian dicono cose diverse da ISO e restano coerenti con la config. Spostate in [Da implementare nelle mod](#da-implementare-nelle-mod):

- `minecraft_sculk`, perché la Rune droppata dallo Sculk viene dall'integrated pack di RuneEnchanting (`enchantment_changes`);
- `shieldsplus_shields`, perché Shields+ è una mod di Insane96.

Parrot Eggs: spente quelle di Quark (`Parrot Eggs` = false), che vogliono i Beetroot Seeds, difficili da trovare. Restano quelle di Vibrant Parrots, che usano `#minecraft:parrot_food`: il datapack lo riduce a Melon e Pumpkin Seeds, che servono anche per addomesticarli.

## Da implementare nelle mod

Pagine per comportamenti delle mod di Insane96, raccolte durante le fasi. Formato: `oggetti` — cosa spiegare (origine).

### InsaneSurvivalOverhaul

- Oggetti di "Energy boost" (lista in `config/insanesurvivaloverhaul/Tiredness/`): riducono la stanchezza (`Tiredness`, `EnergyBoostItem`).
- `#minecraft:beds`: una riga in più nella pagina `beds`, attiva solo con phantoms from tiredness: essere molto stanchi attira i Phantom (`Tiredness`).
- Penalità alla morte (`DeathInventoryPenalty`, gamerule `death_keep_equipment`): armatura, offhand e oggetti con durabilità nella hotbar restano perdendo durabilità, il resto cade. Non ha un oggetto, quindi va fuori da EMI: una riga nella schermata di morte, del tipo "Your equipment was kept but lost durability". Nella stessa schermata, un'altra riga con il numero di morti, così non serve aprire le statistiche o usare lo scoreboard (ISO ha già `ClientboundDeathStatsPacket`, da vedere se si può estendere).
- Non è una pagina: Turtle Scute e Armadillo Scute (`Scutes`, `Scute drops as block`) dovrebbero avere un tooltip "Placeable" tramite InsaneLib, come fa Supplementaries con Stick e Blaze Rod.
- Non è una pagina, è da sistemare: `Portal requires crying obsidian` (`Nether.onPortalTryToActivate`) non controlla gli angoli, ma conta la Crying Obsidian in tutto il rettangolo della cornice e ne vuole almeno 4. Quindi 4 blocchi messi in qualsiasi punto della cornice accendono il portale.
- `minecraft:heart_of_the_sea` (Divine Fragment): a cosa serve (ridà la vita massima persa morendo) e da dove viene: Elder Guardian, Spawner, Ominous Vault, Buried Treasure, Piglin Brute (`Death max health penalty`, `divine_fragment_rp`, `mob_loot_changes`).
- `minecraft:shulker_shell`: gli Shulker lasciano Shulker Box invece dei gusci (`Early game shulker boxes`); i gusci vengono solo dalla runa di RuneEnchanting che stacca le parti (`part_breaking/shulker`).
- `minecraft:ender_pearl`: gli Enderman la lasciano solo con Looting (`Loot changes`, `entities/enderman`), quindi serve dire dove trovarle (baratto con i Piglin, chest degli Stronghold e delle Trial Chamber).
- `minecraft:netherite_scrap`: una riga sui Piglin Brute, che la lasciano spesso (`Loot changes`, `entities/piglin_brute`).
- `minecraft:elytra`: una riga in più rispetto alla pagina del pack: fuori dall'End si plana peggio e il boost dei razzi è più lento, ma si decolla anche con un razzo dopo un salto, senza dover già planare (`Elytra`, `Air resistance`, `Firework boost off ground`).
- `minecraft:crossbow`: le frecce passano attraverso i mob (`Piercing crossbow`), ma partono più lente e meno precise (`Crossbow velocity`, `Crossbow inaccuracy`). Forse basta un tooltip.
- Non è una pagina: la ricetta di riciclo in EMI (`Recycling`) dovrebbe dire che la resa cala con la durabilità consumata.
- `crystal_heart`: va nella stessa pagina del Divine Fragment (`Death max health penalty`): la ricetta si vede, ma non a cosa serve.
- `wild_wheat`, `wild_carrots`, `wild_potatoes`, `wild_beetroots`: la pagina `crops` dice solo "Can be found in the wild". Si possono aggiungere agli stack di quella pagina, con dove crescono e cosa lasciano (`Crops`).
- `sweet_berry_seeds`: da dove vengono, cioè dai cespugli di bacche (pack `berries`) e dai Farmer. Basta aggiungerli alla pagina `sweet_berry_bush` (`Berries`).
- `copper_ore_rock`, `iron_ore_rock`, `gold_ore_rock`: in superficie segnalano una grande vena del minerale sottoterra (`Big ore veins`).
- `cloth`: la lasciano gli Zombie al posto della Rotten Flesh (`Cloth`). Gli usi si vedono dalle ricette, la fonte no.
- `pumpkin_pulp`: si ottiene usando le Shears su una Pumpkin (`gameplay/pumpkin_shear`, `Foods & Drinks`).
- `solanum_neorossii`: la lasciano le patate selvatiche nel deserto (`Crops`). Va detto da dove viene, e si può mettere in un vaso.
- `glow_block`: si vede attraverso i muri anche da lontano. Guardandolo, l'HUD dice su quali assi sei allineato con il blocco, o "Not aligned", per esempio per scavare un tunnel verso un punto (`GlowBlockFeature`). La descrizione della feature dice ancora "for testing" e andrebbe aggiornata.

### Progressive Bosses

- `corrupted_soul_sand`: il tooltip dice dove metterla e il livello di corruzione, ma non cosa cambia (Wither più forte a ogni livello, fino all'Ultimate Wither) né da dove viene.
- `corrupted_end_crystal`: cos'è e come si usa per evocare il Corrupted Ender Dragon.

### RuneEnchanting

- `minecraft:sculk`: senza Silk Touch lascia molto raramente una Rune a caso, che può essere una Curse (`enchantment_changes`, `blocks/sculk`). Testo che era nel pack: "Only drops itself when mined with Silk Touch. Otherwise, very rarely, it drops a random Rune, which may be a Curse."
- `rune`, `encased_rune`, `runic_table`: l'incantamento è sostituito dalle rune, quindi è una delle pagine più importanti per chi inizia. Da spiegare dove si trovano le Rune (loot e Librarian), a cosa serve l'Encased Rune e come si usa il Runic Table.

### Shields+

- Tutti gli scudi (`wooden_shield` ... `netherite_shield`). Testo che era nel pack:
  - "Shields block a fixed amount of damage per hit, shown in their tooltip, and the rest goes through. They only block attacks from the front, and Axes disable them for a moment."
  - "A shield can stay lifted only for a limited time, then it goes on cooldown, longer the more it was lifted. Raising it right before being hit is a parry, which blocks more damage."
  - "With a shield in the off hand, crouch to block. You can attack while crouch blocking, but each attack puts the shield on cooldown for a moment."

### Stamina

- Non ha oggetti. Se serve una spiegazione, va fuori da EMI (tooltip o HUD).

### Altre mod

_(vuoto)_

## Stima

| Fase | Pagine nuove | Sessioni |
|------|-------------:|---------:|
| 0 — Verifiche e inventario | — | 1 |
| 1 — Vanilla cambiato | 15-30 | 1-2 |
| 2 — Vanilla poco evidente | 70-100 | 3-4 |
| 3 — Mod | 40-80 | 2-3 |
| 4 — Revisione | — | 1 |
| **Totale** | **125-210** | **8-11** |

I numeri si restringono dopo la Fase 0: dipendono da quanto è largo il criterio "ovvio" e da cosa mostra già Quark.
