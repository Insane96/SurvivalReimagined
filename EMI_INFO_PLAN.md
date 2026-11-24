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
3. **Blocchi funzionali**: Beacon (se ISO non basta), Conduit, Respawn Anchor, Lectern, Jukebox, Composter, Cauldron, Brewing Stand, Smithing Table e Trim Templates, Loom, Stonecutter, Bell, Scaffolding, Bee Nest / Beehive e Honey, Ender Chest, Shulker Box. **Fatto (2026-11-24)**. Lectern, Jukebox, Cauldron e Bell hanno una riga vanilla nelle pagine di Amendments. Netherite Upgrade e Trim Template hanno una pagina ciascuno con le fonti, prese dalle loot table effettive (DnT, Incendium, Moog's, Adventure Dungeons, Hellish Trials, Bits and Balance). Non servono: Beacon (ISO), Shulker Box (il tooltip di Quark ne mostra il contenuto), Loom, Stonecutter, Scaffolding e Composter (ovvi nell'inventario). Il Blast Armor Trim di Supplementaries si trova solo nei Galleon, spenti nel pack (`galleon = false`): oggi non si ottiene.
4. **Materiali e drop non ovvi**: Echo Shard, Disc Fragment, Heart of the Sea, Nautilus Shell, Sniffer Egg, Armadillo Scute, Breeze Rod, Heavy Core, Trial Key / Ominous Trial Key, Ominous Bottle, Dragon Breath, Shulker Shell, Phantom Membrane.
5. **Equipaggiamento**: Elytra, Trident, Mace, Wind Charge, Turtle Helmet, Shield, Crossbow, Firework Rocket / Star.
6. **Piante e agricoltura**: crescita e Bone Meal (dove ISO non arriva), Sugar Cane, Cactus, Bamboo, Kelp, Chorus, Nether Wart, Sea Pickle, Glow Berries, Pitcher, Torchflower, Moss / Azalea.

## Fase 3 — Mod senza copertura (2-3 sessioni)

- **Quark e Quark Oddities**: dipende dalla Fase 0. In ogni caso serve il Totem of Holding, una pagina chiave per la morte nel pack.
- **Incubation** (Egg Crates, cibi), **Better Tridents** (Trident Fragment), **Hellish Trials** (Ominous Vault e loot).
- **RuneEnchanting**, **Stamina**, **Progressive Bosses**: sono mod di Insane96, quindi le loro pagine vanno in [Da implementare nelle mod](#da-implementare-nelle-mod).
- **Buchi nelle mod già coperte**: per esempio Bits and Balance (2 pagine), Clayworks, Boatload, Sawmill, Ecologics, Vanilla Backport. Si controllano gli oggetti non decorativi rimasti senza pagina.

## Fase 4 — Revisione (1 sessione)

- Rileggere le 162 pagine esistenti alla luce di quelle nuove: doppioni con ISO o Quark, testi diventati sbagliati per cambi di config.
- Controllo in gioco a campione (EMI → tasto info) dei lotti più grandi.
## Da implementare nelle mod

Pagine per comportamenti delle mod di Insane96, raccolte durante le fasi. Formato: `oggetti` — cosa spiegare (origine).

### InsaneSurvivalOverhaul

- Oggetti di "Energy boost" (lista in `config/insanesurvivaloverhaul/Tiredness/`): riducono la stanchezza (`Tiredness`, `EnergyBoostItem`).
- `#minecraft:beds`: una riga in più nella pagina `beds`, attiva solo con phantoms from tiredness: essere molto stanchi attira i Phantom (`Tiredness`).
- Penalità alla morte (`DeathInventoryPenalty`, gamerule `death_keep_equipment`): armatura, offhand e oggetti con durabilità nella hotbar restano perdendo durabilità, il resto cade. Non ha un oggetto, quindi va fuori da EMI: una riga nella schermata di morte, del tipo "Your equipment was kept but lost durability". Nella stessa schermata, un'altra riga con il numero di morti, così non serve aprire le statistiche o usare lo scoreboard (ISO ha già `ClientboundDeathStatsPacket`, da vedere se si può estendere).
- Non è una pagina: Turtle Scute e Armadillo Scute (`Scutes`, `Scute drops as block`) dovrebbero avere un tooltip "Placeable" tramite InsaneLib, come fa Supplementaries con Stick e Blaze Rod.
- Non è una pagina, è da sistemare: `Portal requires crying obsidian` (`Nether.onPortalTryToActivate`) non controlla gli angoli, ma conta la Crying Obsidian in tutto il rettangolo della cornice e ne vuole almeno 4. Quindi 4 blocchi messi in qualsiasi punto della cornice accendono il portale.
- Non è una pagina: la ricetta di riciclo in EMI (`Recycling`) dovrebbe dire che la resa cala con la durabilità consumata.

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
