# Da controllare alla fine (pagine dei mob)

Tutti i test in gioco e tutti i `?` delle pagine dei mob (ora in Field Guide), da fare insieme a fine lavoro. Ogni fase aggiunge qui i suoi. Dopo la verifica: correggere `pages_<fase>.py` (testi) o `extras.py` (matrice), poi rilanciare `run.sh` e `write_pages.py` con tutti i `pages_*.py` insieme.

## Test generali

- [ ] Le descrizioni compaiono in Field Guide dopo la scansione (fase 1: 42 mob passivi; fase 2: 24 mob ostili; fase 3: 12 mob del Nether e dell'End, più Ender Dragon e Wither nei Bosses). Sono 80 chiavi `fieldguide.minecraft.<mob>.description`, tutti i mob sono nei tag `passive`/`neutral`/`hostile` di Field Guide. Fase 4: 47 mob di Naturalist (`fieldguide.naturalist.*`), che Field Guide mette in Animals/Monsters dalla `MobCategory`, senza tag. Fase 5: 8 mob di Vanilla Backport (`fieldguide.minecraft.*`: Camel Husk, Copper Golem, Creaking, Happy Ghast, Nautilus, Parched, Sulfur Cube, Zombie Nautilus), 3 di Ecologics e 2 di Supplementaries (Red Merchant, Plunderer). Il Copper Golem è `MISC` ma ha l'uovo, quindi dovrebbe comparire in Animals: controllare.
- [ ] I testi condivisi (riproduzione, vecchiaia, equini, zombie, scheletri) sono paragrafi in fondo alla descrizione giusta.
- [ ] Le descrizioni lunghe (Ender Dragon, Wither, Villager, Zombie Villager, Horse) scorrono bene e non vengono tagliate.
- [ ] Nessuna pagina dei mob rimasta in EMI (tolti i 78 file `*_spawn_egg.json` e le chiavi `emi.info.*_spawn_egg*` / `emi.info.survivalreimagined.mob.*`).
- [ ] La descrizione dell'advancement di EMI non parla più delle Spawn Egg (tolta l'ultima frase).
- [ ] Le descrizioni non elencano i cibi: dicono di cercare `#<mob>_food` in EMI (64 mob; Horse `#minecraft:horse_food`, perché `#horse_food` troverebbe anche lo Zombie Horse; Crab di Naturalist `#naturalist:crab_food`, perché `#crab_food` troverebbe anche il Coconut Crab; Zombie Nautilus `#nautilus_food`, stesso cibo del Nautilus). Ogni ricerca trova il tag giusto (controllato sugli ID). In gioco: la ricerca mostra i cibi e i nomi dei tag ("Deer Food"...) si vedono. I tag `survivalreimagined:<mob>_food` sono solo di riferimento per i mob col cibo fisso nel codice (Deer, Elephant, Mammoth, Hippo, Snail, Whale) o con un tag dal nome diverso (Bear, Black Bear, Butterfly, Lizard, Snake, Tortoise, Zebra, Mooshroom, Donkey, Mule, Trader Llama, Coconut Crab, Penguin; Squirrel ha la Honeycomb fissa nel codice, le Walnut lo attirano soltanto).

## `?` da verificare in gioco

### Fase 1 (passivi)

- [ ] **Cat**: i villaggi abbandonati non ne generano (pool vuoto); il CatSpawner vanilla li fa comparire vicino ai letti? (omesso dalla pagina)
- [ ] **Iron Golem**: i villager lo evocano? Nei villaggi abbandonati non ci sono villager, ma i villager curati sì (la pagina del Villager dice che chiamano gli Iron Golem quando sono in pericolo).
- [ ] **Mooshroom** (Mooshroom Tweaks `becomeBrownChance` 0.5): metà dei Mooshroom è marrone? (omesso)
- [ ] **Mule**: con ISO `prevent_breeding` nasce davvero da Cavallo e Asino domati che si innamorano da soli? (scritto)
- [ ] **Parrot** (Naturalist `parrot_flight`): secondo il changelog di Naturalist 2.0, con un Parrot su ogni spalla e un Bird in testa si vola lentamente. Scritto su Parrot e Bird: verificare.
- [ ] **Snow Golem** (Quark `Snow Golem Player Heads`): uno Snow Golem con il nome di un giocatore, ucciso da una Witch, droppa la testa del giocatore? (omesso: è un drop)
- [ ] **Zombie Horse** (Vanilla Backport `has_zombie_horses`): spawna di notte con uno Zombie in sella? Si può domare? (omesso)

### Fase 2 (ostili)

- [ ] **Creeper** (MPR `Better creeper lingering`): i Creeper con effetti di pozione lasciano una nuvola esplodendo? (omesso)
- [ ] **Husk** (Vanilla Backport `has_camel_husks`): nei deserti cavalca un Camel Husk con un Parched dietro? (scritto; dal codice: il 10% degli Husk spawnati naturalmente, se c'è spazio)
- [ ] **Guardian**: "Its attacks ignore armor" va bene come resa del solo danno magico di ISO? (scritto)
- [ ] **Phantom** (Bits and Balance `enableImprovedPhantoms`): le opzioni di trasporto (doppio danno, caduta automatica, caduta se colpito) valgono anche per la presa di Enhanced AI? Enhanced AI blocca lo smontaggio, quindi probabilmente no (omesse)
- [ ] **Skeleton, Bogged, Stray** (Bits and Balance `tippedArrowLingeringClouds.mobsEnabled`): le frecce con effetto dei mob lasciano la nuvola? Va sulla pagina della Tipped Arrow, non sulle uova.

### Fase 3 (Nether, End, boss)

- [x] **Drago e Wither senza uovo**: risolto con Field Guide, le loro descrizioni sono nei Bosses (si sbloccano uccidendoli).
- [ ] **Ender Dragon** (Progressive Bosses): esistono solo le definizioni di livello 0 (base) e 4 (corrupted). Con 1-3 Corrupted End Crystal tra i 4 del respawn il livello è 1-3 e non c'è definizione: il Drago resta vanilla (nel log `Failed to get Dragon Stats`)?
- [ ] **Elder Guardian** (Progressive Bosses): uccidendone uno, gli altri entro 64 blocchi diventano più forti (si sente il verso della maledizione)? Gli Elder dei trial spawner del Monumento vengono potenziati (lo spawn `SPAWNER` è escluso, `TRIAL_SPAWNER` no)?
- [ ] **Shulker** (Enhanced AI): la Levitation VI breve si sente "much stronger and shorter"? Sotto metà vita resta socchiuso mentre spara?
- [ ] **Wither Skeleton** (Enhanced AI MPR `wither_skeleton`): alcuni spawnano con l'arco e tirano frecce di Wither?

### Fase 4 (Naturalist)

Fonti: changelog di Naturalist 2.x e wiki di minecraft-guides.com (2026-10), controllati nel jar dove non coincidono.

- [ ] **Capybara**: per Naturalist si riproducono solo quelli domati. Con ISO `prevent_breeding` quelli selvatici si innamorano da soli e fanno figli? (scritto solo il testo condiviso)
- [ ] **Butterfly**: con ISO si innamorano da sole e lasciano un Caterpillar?
- [ ] **Whale**: aggiunta ai tag di riproduzione di ISO (`breedable_animals`, `prevent_breeding`), si innamora da sola. Nessun tag di vecchiaia. Il cibo è fisso nel codice: Cod, Salmon e Crab Meat, crudi o cotti (`survivalreimagined:whale_food`). Controllare che così diventi 'well fed'.
- [ ] **Mole, Lizard, Rhino**: nel codice non hanno `BreedGoal` (il changelog dice che il Mole si riproduce con gli Spider Eye): scritto "can't be bred".
- [ ] **Deer**: mangia le Apple (dalla wiki, nessun tag nella matrice)?
- [ ] **Firefly**: alla luce del sole sparisce (codice: `isSunBurnTick` -> `discard`), non brucia come diceva la wiki (1.x).
- [ ] **Dragonfly**: nutrita con Chorus Fruit sputa una nuvola di Instant Damage (codice, `mobInteract`).
- [ ] **Hippo**: attacca le barche (`HippoAttackBoatsGoal`) e segue i giocatori a terra (2.0.7).
- [ ] **Clam**: si prende il tesoro con click destro mentre è aperta (wiki)?
- [ ] **Ant**: lo Sugar le cura; le formiche di un formicaio piantato con la Queen Ant ti difendono.
- [ ] **Vulture**: attacca chi ha poca vita e tiene qualcosa in mano (codice: vita sotto i 3 cuori, mano principale non vuota), a meno che non porti già Rotten Flesh.
- [ ] **Black Bear**: stesso testo del Bear (per il changelog è un clone).
- [ ] Le entità tecniche `naturalist:carried_food`, `dirt_trail`, `lizard_tail` non compaiono in Field Guide (MISC senza uovo); altrimenti metterle in `fieldguide:blacklisted`.
- [ ] Varianti (Bird, Snake, Tiger, Crab...) mostrate bene da Field Guide (Naturalist ha un suo provider di varianti).

### Fase 5 (Vanilla Backport, Ecologics, Supplementaries)

Fonti: i jar decompilati (Vanilla Backport 1.2.2, Ecologics 2.3.12, Supplementaries 4.1.4) e i loro config.

- [x] **Caterpillar** (Naturalist): nasce dalle Butterfly innamorate (wiki), poi diventa Chrysalis su un tronco. Scritto, vedi fase 4.
- [ ] **Camel Husk**: arriva con il 10% degli Husk spawnati naturalmente, con un Parched dietro (`HuskMixin`, non dipende da `has_camel_husks`). Senza cavalieri si sella e si cavalca, non si riproduce; sparisce come un mostro finché non ci interagisci. Il Rabbit's Foot lo cura?
- [ ] **Parched**: spawna nei biomi con la Desert Pyramid (`has_parched_skeletons`), non brucia al sole (`isSunBurnTick` false, quindi neanche il `Burn in sky light` di ISO) e le sue frecce danno Weakness.
- [ ] **Creaking**: sparisce all'alba (`do_creaking_hearts_work_on_day` false), come in vanilla?
- [ ] **Copper Golem**: con la mano vuota ti dà l'oggetto che trasporta; il fulmine gli toglie uno stadio di ossidazione. Gli Iron Golem gli regalano un Poppy (`OfferCopperGolemFlowerGoal`, omesso).
- [ ] **Happy Ghast**: si cura più in fretta sotto la pioggia o tra le nuvole; sta fermo con un giocatore sopra; al massimo 4 passeggeri.
- [ ] **Nautilus**: caccia i Pufferfish (`nautilus_hostiles`), carica chi lo colpisce, immune al veleno; si doma con il Pufferfish (1 su 3). Con ISO si innamora da solo (`breeds_alone`).
- [ ] **Zombie Nautilus**: brucia al sole se non ha l'armatura (che si consuma al posto suo); senza Drowned in sella si doma e si cavalca come il Nautilus? Non si riproduce.
- [ ] **Sulfur Cube**: non attacca; con un blocco dentro smette di girare, si spinge, si lega al guinzaglio e non sparisce; con il TNT esplode con Flint and Steel, fuoco o redstone; da ucciso si divide in due piccoli; le Slime Ball fanno crescere i piccoli.
- [ ] **Coconut Crab**: esce dal 20% dei Cocchi che si rompono cadendo dalle palme (spiagge). Con il Cocco addosso prende metà danno e reagisce; sotto metà vita il guscio si rompe (2 Coconut Slice) e scappa dai giocatori; un Cocco dato in mano glielo rimette.
- [ ] **Penguin**: resta incinta e partorisce dopo (`spawnChildFromBreeding` sovrascritto, niente `BabyEntitySpawnEvent`): con ISO si innamora da sola, ma niente fallimenti né gemelli (testo `breeds_alone.no_twins`). Più di 4 Penguin vicini danno Regeneration ai giocatori.
- [ ] **Alligator, Ostrich, Snail, Tortoise** (Naturalist): fanno le uova con `EggLayingBreedGoal`, che non lancia `BabyEntitySpawnEvent`, quindi niente fallimenti né gemelli di ISO: passati a `breeds_alone.no_twins` (prima dicevano "can fail and sometimes gives twins"). La Turtle vanilla ha un mixin apposta in ISO, questi no.
- [ ] **Squirrel**: solo nelle Plains (biome modifier di Ecologics). Le Walnut lo fanno fidare (1 su 3), poi raccoglie e pianta gli Alberelli; la Honeycomb è il cibo per la riproduzione.
- [ ] **Red Merchant**: arriva quando non arriva il Wandering Trader, più spesso con difficoltà locale alta e dopo il Drago (`RedMerchantSpawnerMixin`). Gli Evoker trasformano i Wandering Trader vicini in Red Merchant (sempre attivo, serve `mobGriefing`). Lancia Bombe a Zombie, raider e Zoglin.
- [ ] **Plunderer**: solo nei raid dal mare (Galleon spenti). Spada d'oro, usa i Cannoni vicini, a volte ha un Parrot in spalla.
- [ ] Le pagine EMI di Harness, Dried Ghast, Nautilus Armor, Creaking Heart, Copper Chest, Copper Golem Statue e del Sulfur Cube Bucket restano: ripetono in parte le pagine dei mob, decidere se accorciarle.

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
- [ ] Giant Isopod, Snail, Tortoise: "taking less damage" (Tortoise anche "barely knocked back")
- [ ] Lizard, Tortoise: "Tamed ... get tougher"
- [ ] Jungle Scorpion: "Bigger than the Desert Scorpion"
