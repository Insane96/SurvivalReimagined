# Da controllare alla fine (pagine dei mob)

Tutti i test in gioco e tutti i `?` delle pagine dei mob (ora in Field Guide), da fare insieme a fine lavoro. Ogni fase aggiunge qui i suoi. Dopo la verifica: correggere `pages_<fase>.py` (testi) o `extras.py` (matrice), poi rilanciare `run.sh` e `write_pages.py` con tutti i `pages_*.py` insieme.

## Test generali

- [ ] Le descrizioni compaiono in Field Guide dopo la scansione (fase 1: 42 mob passivi; fase 2: 24 mob ostili; fase 3: 12 mob del Nether e dell'End, più Ender Dragon e Wither nei Bosses). Sono 80 chiavi `fieldguide.minecraft.<mob>.description`, tutti i mob sono nei tag `passive`/`neutral`/`hostile` di Field Guide.
- [ ] I testi condivisi (riproduzione, vecchiaia, equini, zombie, scheletri) sono paragrafi in fondo alla descrizione giusta.
- [ ] Le descrizioni lunghe (Ender Dragon, Wither, Villager, Zombie Villager, Horse) scorrono bene e non vengono tagliate.
- [ ] Nessuna pagina dei mob rimasta in EMI (tolti i 78 file `*_spawn_egg.json` e le chiavi `emi.info.*_spawn_egg*` / `emi.info.survivalreimagined.mob.*`).
- [ ] La descrizione dell'advancement di EMI non parla più delle Spawn Egg (tolta l'ultima frase).

## `?` da verificare in gioco

### Fase 1 (passivi)

- [ ] **Cat**: i villaggi abbandonati non ne generano (pool vuoto); il CatSpawner vanilla li fa comparire vicino ai letti? (omesso dalla pagina)
- [ ] **Iron Golem**: i villager lo evocano? Nei villaggi abbandonati non ci sono villager, ma i villager curati sì (la pagina del Villager dice che chiamano gli Iron Golem quando sono in pericolo).
- [ ] **Mooshroom** (Mooshroom Tweaks `becomeBrownChance` 0.5): metà dei Mooshroom è marrone? (omesso)
- [ ] **Mule**: con ISO `prevent_breeding` nasce davvero da Cavallo e Asino domati che si innamorano da soli? (scritto)
- [ ] **Parrot** (Naturalist `parrot_flight`): i pappagalli sulla spalla danno Slow Falling? (omesso)
- [ ] **Snow Golem** (Quark `Snow Golem Player Heads`): uno Snow Golem con il nome di un giocatore, ucciso da una Witch, droppa la testa del giocatore? (omesso: è un drop)
- [ ] **Zombie Horse** (Vanilla Backport `has_zombie_horses`): spawna di notte con uno Zombie in sella? Si può domare? (omesso)

### Fase 2 (ostili)

- [ ] **Creeper** (MPR `Better creeper lingering`): i Creeper con effetti di pozione lasciano una nuvola esplodendo? (omesso)
- [ ] **Husk** (Vanilla Backport `has_camel_husks`): nei deserti cavalca un Camel Husk con un Parched dietro? (scritto)
- [ ] **Guardian**: "Its attacks ignore armor" va bene come resa del solo danno magico di ISO? (scritto)
- [ ] **Phantom** (Bits and Balance `enableImprovedPhantoms`): le opzioni di trasporto (doppio danno, caduta automatica, caduta se colpito) valgono anche per la presa di Enhanced AI? Enhanced AI blocca lo smontaggio, quindi probabilmente no (omesse)
- [ ] **Skeleton, Bogged, Stray** (Bits and Balance `tippedArrowLingeringClouds.mobsEnabled`): le frecce con effetto dei mob lasciano la nuvola? Va sulla pagina della Tipped Arrow, non sulle uova.

### Fase 3 (Nether, End, boss)

- [x] **Drago e Wither senza uovo**: risolto con Field Guide, le loro descrizioni sono nei Bosses (si sbloccano uccidendoli).
- [ ] **Ender Dragon** (Progressive Bosses): esistono solo le definizioni di livello 0 (base) e 4 (corrupted). Con 1-3 Corrupted End Crystal tra i 4 del respawn il livello è 1-3 e non c'è definizione: il Drago resta vanilla (nel log `Failed to get Dragon Stats`)?
- [ ] **Elder Guardian** (Progressive Bosses): uccidendone uno, gli altri entro 64 blocchi diventano più forti (si sente il verso della maledizione)? Gli Elder dei trial spawner del Monumento vengono potenziati (lo spawn `SPAWNER` è escluso, `TRIAL_SPAWNER` no)?
- [ ] **Shulker** (Enhanced AI): la Levitation VI breve si sente "much stronger and shorter"? Sotto metà vita resta socchiuso mentre spara?
- [ ] **Wither Skeleton** (Enhanced AI MPR `wither_skeleton`): alcuni spawnano con l'arco e tirano frecce di Wither?

### Fasi successive (già nella matrice)

- [ ] **Camel Husk** (Vanilla Backport): spawna nei deserti di notte con Husk e Parched in sella (dal codice, non nei JSON dei biomi)?
- [ ] **Parched** (Vanilla Backport `has_parched_skeletons`): spawna nei deserti (dal codice)?
- [ ] **Caterpillar** (Naturalist): nasce dalle Butterfly (uova/crisalide)?
- [ ] **Coconut Crab** (Ecologics): esce dal Cocco che cade dalle palme?
- [ ] **Red Merchant** (Supplementaries): arriva con il Wandering Trader?

## Field Guide (le pagine dei mob si spostano lì)

- [x] A capo e testi lunghi (Zombie) si vedono bene, le nostre chiavi battono le descrizioni del mod.
- [x] Griglia dei drop: legge solo le loot table, non i global loot modifier (Zombie mostra la Rotten Flesh invece della Cloth di ISO). Spenta (`disableLootDisplay: true`): i drop utili vanno nei testi.
- [x] Griglia dei biomi: richiede Immersive Overlays (tolta). Spenta (`disableBiomeDisplay: true`): i biomi restano nei testi.
- [ ] Guardian non scansionabile nel test (probabilmente TeamViewer): riprovare.
- [ ] Drago e Wither compaiono bloccati nei Bosses (`kill_to_unlock`).
- [ ] Mob delle mod (Naturalist, Ecologics, Vanilla Backport) renderizzati bene.
- [ ] Blocchi e item: si reintegrano in Field Guide dopo i mob. Per ora la categoria Plants è nascosta (`datapacks/survivalreimagined/data/fieldguide/fieldguide/categories/plants.json`, `"hidden": true`) e `mushroom_collector` è disattivato (`neoforge:false`): da riattivare insieme. Il nome resta Field Guide.
- [ ] Spawn egg nascoste in EMI (`assets/emi/index/stacks/survivalreimagined_spawn_eggs.json`, filtro `/_spawn_egg$/`): controllare che spariscano tutte (anche quelle delle mod) e nient'altro.
- [ ] Vita e armatura nella pagina restano per ora.
- [x] Tolte le pagine `emi:info` dei mob; `write_pages.py` scrive le chiavi `fieldguide.*` (testi e testi condivisi in un'unica chiave, un paragrafo ciascuno). Tolte anche le voci di prova di Creeper e Zombie.
- [x] Descrizione dell'advancement di EMI: tolta la frase sulle Spawn Egg.
- [ ] Item: Field Guide supporta anche voci per item (`obtain`/`eat`, strategie `items`/`food`/`mod_items`), per ora restano in EMI. `disableObtainUnlocks` resta `false`.
- [ ] Condivisione: niente sblocco per tutto il server per ora (`entryScanCommands` con `fieldguide grant @a` era l'alternativa, i team non sono supportati).

### Advancement di Field Guide

- [ ] `fieldguide:root` (si ottiene con il Spyglass nell'inventario): descrizione riscritta in `en_us.json` ("Get a Spyglass and look at mobs through it to add them to your Field Guide, opened with B"). Controllare in gioco; se si aggiungono blocchi, citarli.
- [ ] Field Guide sposta il vanilla `minecraft:adventure/spyglass_at_parrot` sotto `fieldguide:root`: va bene o lo rimettiamo in Adventure?
- [x] `mushroom_collector` (4 funghi giganti): disattivato finché Plants è nascosta.
- [ ] `animal_expert` / `monster_hunter` (completare la categoria): fattibili solo se non ci sono mob irraggiungibili (disattivati, senza spawn, es. Quark Crab, Illusioner, Giant, mob di sole strutture rimosse). Controllare le liste e metterli in `fieldguide:blacklisted`.
- [ ] Gli altri (`first_discovery`, `enderman_scan`, `invisible_scan`, `gem_alert`, `let_him_cook`, `quick_review`) vanno bene così? Controllare che il tono dei testi vada bene col pack.

## Frasi al limite dello stile (numeri/statistiche)

Lasciate per ora, da rivedere con l'utente:

- [ ] Rabbit: "It takes less fall damage"
- [ ] Zombie Horse: "Tougher but slower than a Horse"
- [ ] Llama, Trader Llama: "Some carry more than others"
- [ ] Horse: "steps up two blocks without jumping"
- [ ] Spider, Cave Spider: "barely takes fall damage"
- [ ] Vindicator: "It hits less hard"
- [ ] Vex: "It's bigger but dies quickly"
- [ ] Guardian: "smaller and much weaker"
- [ ] Drowned: "Its Trident hits less hard"
- [ ] Elder Guardian: "tougher, quicker to attack"
- [ ] Shulker: "It's armored even while open", "Levitation is much stronger and shorter"
- [ ] Ender Dragon: "Hitting it in flight hurts it more than when it's perched, and explosions hurt it less"
- [ ] Wither: "the Ultimate does all of this and hits harder"
