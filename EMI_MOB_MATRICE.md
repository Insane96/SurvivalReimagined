# Matrice mob × mod — SurvivalReimagined4

Generata da `tools/emi_mobs/run.sh` (dati del pack: tag, biomi, strutture, config) più le note manuali in `tools/emi_mobs/extras.py`: non modificare questo file a mano, modifica `extras.py` e rigenera. `?` = da verificare. **OFF** = il mob è nel tag ma la feature è spenta o azzerata da config.

## Comportamenti generici (non ripetuti per ogni mob)

Questi valgono per quasi tutti i mob e nella matrice sono solo una sigla accanto al nome:

- **T** (Enhanced AI Targeting): ti sentono attraverso i muri a corto raggio, ti seguono da più lontano, avvisano i vicini.
- **X** (Enhanced AI): scappano da Creeper innescati e TNT, vanno nel panico se in fiamme, rompono barche e minecart per scappare.
- **S** (MPR di Enhanced AI `speed_bonus`/`outside_nerf`): più veloci (meno all'aperto di giorno senza luna piena), nuotano più veloci, all'aperto ti seguono da meno lontano.
- **D** (MPR di Enhanced AI `deepness_buff`): nelle grotte dell'Overworld hanno più vita e ti sentono da più lontano, crescendo con la profondità.
- **A** (Enhanced AI animali): a volte reagiscono o sono ostili, a volte scappano dai giocatori, il branco scappa se uno viene colpito, metà non segue il cibo.
- ISO (tutti i mostri): equipaggiamento droppato il 50% delle volte e mai integro; spawn possibile anche vicino allo spawn del mondo; niente spawn vicino a una Echo Lantern; gli spawner ignorano la luce e partono con una raffica (vedi CLAUDE.md); i non-morti bruciano alla luce del sole anche sotto un blocco (`Burn in sky light`).
- Enhanced AI: i mostri spariscono solo più lontano; mob cramming ridotto (ISO).

## Decisioni (2026-11-26)

- Pagine EMI sulle uova, una per mob, nel pack (`resourcepacks/survivalreimagined_lang`), anche per il comportamento delle mod di Insane96. Niente drop; sempre dove si trova.
- I comportamenti generici qui sopra **non** si scrivono nelle pagine: solo quelli distintivi del mob.
- Le meccaniche degli oggetti (Cage, Jar, Flute, guinzaglio, frecce con effetto) vanno sulle pagine degli oggetti, non ripetute sulle uova.
- Le voci `?` che non si chiariscono dal codice le controlla l'utente in gioco.

## Vanilla

### Allay (`minecraft:allay`)  · D S T X
- **Dove (biomi)**: —
- **Strutture**: Adventure Dungeons (piazzato); Pillager Outpost (piazzato); Woodland Mansion (DnT Illager Manor) (piazzato)
- **Altre fonti**: nelle gabbie delle Pillager Outpost e nella Woodland Mansion (DnT)
- Supplementaries Cage: catturabile in gabbia
- Supplementaries Jar: catturabile in un barattolo

### Armadillo (`minecraft:armadillo`)  · A D S
- **Dove (biomi)**: Overworld: Badlands, Eroded Badlands
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- ISO `Disable armadillo brushing`: non si spazzolano: le scaglie si raccolgono quando le perde
- ISO `Scutes`: le scaglie cadono come blocco impilabile
- Supplementaries Cage: catturabile in gabbia
- **Cibo (tag)**: `minecraft:armadillo_food` = spider_eye (ultimo: minecraft)

### Axolotl (`minecraft:axolotl`)  · D S T X
- **Dove (biomi)**: Overworld: Lush Caves
- **Strutture**: Woodland Mansion (DnT Illager Manor) (piazzato)
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `minecraft:axolotl_food` = tropical_fish_bucket, naturalist:anglerfish_bucket, naturalist:bass_bucket, naturalist:blobfish_bucket, naturalist:catfish_bucket, naturalist:piranha_bucket (ultimo: naturalist)

### Bat (`minecraft:bat`)
- **Dove (biomi)**: quasi tutto l'Overworld (56/57; manca: Deep Dark)
- **Strutture**: Adventure Dungeons (piazzato)
- Supplementaries Cage: catturabile in gabbia
- Supplementaries Urn: può uscire dalle Urne rotte nelle grotte

### Bee (`minecraft:bee`)  · D S T X
- **Dove (biomi)**: —
- **Altre fonti**: dai Bee Nest sugli alberi (foreste di betulle, pianure, prati, ciliegi) e dagli alveari
- ISO Aging: vita molto breve
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- Enhanced AI `Bee hive navigation`: si allontanano meno dall'alveare
- Supplementaries Cage: catturabile in gabbia
- Supplementaries Jar: catturabile in un barattolo
- **Cibo (tag)**: `minecraft:bee_food` = ecologics:azalea_flower, insanesurvivaloverhaul:cyan_flower, allium, azure_bluet, blue_orchid, cactus_flower, cherry_leaves, chorus_flower, closed_eyeblossom, cornflower ... (ultimo: minecraft)

### Blaze (`minecraft:blaze`)  · D S T X
- **Dove (biomi)**: Nether: Infernal Dunes, Volcanic Deltas
- **Strutture**: Fortezza del Nether (DnT) (piazzato, spawn naturale, spawner, trial spawner); Hellish Trials (trial spawner); Incendium (piazzato, spawner); Moog's Nether Structures (piazzato, spawn naturale)
- EAI Blaze attack: raffiche di palle di fuoco più lunghe

### Bogged (`minecraft:bogged`)  · D S T X
- **Dove (biomi)**: Overworld: Mangrove Swamp
- **Strutture**: Adventure Dungeons (trial spawner); Jungle Temple (DnT) (piazzato, spawn naturale); Trial Chambers (trial spawner)
- EAI Climbing: sale le scale a pioli
- EAI Leaders: alcuni sono leader e chiamano rinforzi
- EAI Lunge at target: si ferma un attimo e poi si lancia contro il bersaglio
- EAI MPR `overworld_skeletons`: armatura (più spesso con la luna piena e in profondità), meno preciso
- EAI MPR `scale/skeletons`: più piccoli a caso
- EAI Riding: a volte cavalca altri mob
- EAI Skeleton flee target: si allontana se ti avvicini
- EAI Skeleton shoot: tira più lontano, più spesso e si sposta di lato
- Bits and Balance `tippedArrowLingeringClouds.mobsEnabled`: le sue frecce con effetto lasciano una nuvola dell'effetto dove atterrano (vale per tutte le frecce con effetto, anche dei giocatori: va sulla pagina della Tipped Arrow, qui solo un accenno)
- **OFF**: Shielding (`Chance to equip` 0); Parkour (feature spenta)

### Breeze (`minecraft:breeze`)  · D S X
- **Dove (biomi)**: —
- **Strutture**: Hellish Trials (trial spawner); Trial Chambers (trial spawner)
- **Altre fonti**: solo dai trial spawner (Trial Chambers, Hellish Trials)

### Camel (`minecraft:camel`)  · A D S T X
- **Dove (biomi)**: Overworld: Desert
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- Ecologics `camelChestsEnabled`: gli si può mettere una Chest
- Supplementaries Flute: richiamabile con il Flauto
- Vanilla Backport `camel_spawns` + Ecologics `spawn_camel`: spawna nei deserti
- **Cibo (tag)**: `minecraft:camel_food` = ecologics:prickly_pear, cactus (ultimo: Ecologics)

### Cat (`minecraft:cat`)  · D S X
- **Dove (biomi)**: —
- **Strutture**: Swamp Hut (DnT) (spawn naturale)
- **Altre fonti**: Swamp Hut (DnT) e addomesticando un Ocelot; ?i villaggi abbandonati non ne generano (pool vuoto), da verificare se il CatSpawner vanilla li fa comparire vicino ai letti
- ISO Aging: non invecchia: non è in nessun tag `*_lifespan`
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- ISO Misc mobs `Passive regen chance`: si cura lentamente da solo
- ISO `Ocelot to cat`: si ottiene anche addomesticando un Ocelot; villaggi senza gatti; c'è quello della Swamp Hut
- EAI MPR `small_animals`: attacco più debole
- Amendments `pets_follow_teleports`: gli animali che ti seguono si teletrasportano con te (anche portali)
- Bits and Balance `friendlyFireFriendlies`: non puoi colpire per sbaglio i tuoi animali
- Supplementaries Cage: catturabile in gabbia
- **Cibo (tag)**: `minecraft:cat_food` = cod, salmon, naturalist:anglerfish, naturalist:bass, naturalist:blobfish, naturalist:catfish, naturalist:piranha (ultimo: naturalist)

### Cave Spider (`minecraft:cave_spider`)  · D S T X
- **Dove (biomi)**: Overworld: Sulfur Caves
- **Strutture**: Hellish Trials (trial spawner); Incendium (piazzato); Jungle Temple (DnT) (piazzato); Philips' Ruins (piazzato, spawner); Stronghold (DnT) (piazzato, spawner); Trial Chambers (trial spawner)
- **Altre fonti**: spawner nelle Mineshaft
- EAI MPR `spiders`: quasi niente danno da caduta, un po' più lento
- EAI Riding: a volte cavalca altri mob
- EAI Web thrower: a volte lancia ragnatele che rallentano; le ragnatele avvelenano
- Bits and Balance `enableCaveSpidersInCaves` (0.15): parte dei Ragni nelle grotte viene sostituita da Cave Spider
- Enhanced AI `Stuck fix`: non restano più bloccati sui muri
- **OFF**: Parkour (feature spenta)

### Chicken (`minecraft:chicken`)  · A D S T X
- **Dove (biomi)**: Overworld: Bamboo Jungle, Birch Forest, Dappled Forest, Dark Forest, Flower Forest, Forest, Grove, Jungle, Old Growth Birch Forest, Old Growth Pine Taiga, Old Growth Spruce Taiga, Plains, Snowy Taiga, Sparse Jungle, Sunflower Plains, Taiga, Windswept Forest, Windswept Gravelly Hills, Windswept Hills
- **Strutture**: Incendium (piazzato); Woodland Mansion (DnT Illager Manor) (piazzato)
- ISO Aging: vita breve
- ISO Animal products: uova più lente; da un uovo lanciato esce un pulcino 1 volta su 8
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Crops (`chicken_food_items`): si nutrono solo con Semi di Melone, Zucca e Torchflower; gli altri semi (grano, barbabietola, lino, carota) le attirano soltanto
- EAI MPR `small_animals`: attacco più debole
- Naturalist `remove_farm_animals_savanna/swamp`: niente in savane e paludi
- Quark `Grab Chickens`: si prende in testa e rallenta la caduta (Slowness)
- Supplementaries Cage: catturabile in gabbia
- Supplementaries Fodder: mangia il Fodder
- Vanilla Backport `farm_animal_variants` = false: spento: nessuna variante
- **Cibo (tag)**: `insanesurvivaloverhaul:chicken_food_items` = melon_seeds, pumpkin_seeds, torchflower_seeds (ultimo: insanesurvivaloverhaul) · `minecraft:chicken_food` = beetroot_seeds, melon_seeds, pitcher_pod, pumpkin_seeds, torchflower_seeds, wheat_seeds, supplementaries:flax_seeds (ultimo: supplementaries)

### Cod (`minecraft:cod`)  · D S T X
- **Dove (biomi)**: Overworld: Cold Ocean, Deep Cold Ocean, Deep Lukewarm Ocean, Deep Ocean, Lukewarm Ocean, Ocean
- EAI MPR `scale/sea_creatures`: dimensioni casuali

### Cow (`minecraft:cow`)  · A D S T X
- **Dove (biomi)**: Overworld: Bamboo Jungle, Birch Forest, Dappled Forest, Dark Forest, Flower Forest, Forest, Grove, Jungle, Old Growth Birch Forest, Old Growth Pine Taiga, Old Growth Spruce Taiga, Plains, Snowy Taiga, Sparse Jungle, Sunflower Plains, Taiga, Windswept Forest, Windswept Gravelly Hills, Windswept Hills
- **Strutture**: Woodland Mansion (DnT Illager Manor) (piazzato)
- ISO Aging: vita lunga
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- ISO `Fluid cooldown`: si mungono una volta ogni tanto (anche lo stufato del Mooshroom)
- Naturalist `remove_farm_animals_savanna/swamp`: niente in savane e paludi
- Supplementaries Cage: catturabile in gabbia da cucciolo
- Supplementaries Fodder: mangia il Fodder
- Vanilla Backport `farm_animal_variants` = false: spento: nessuna variante
- **Cibo (tag)**: `minecraft:cow_food` = wheat, supplementaries:flax (ultimo: supplementaries)

### Creeper (`minecraft:creeper`)  · D S T X
- **Dove (biomi)**: quasi tutto l'Overworld (55/57; manca: Deep Dark, Mushroom Fields)
- **Strutture**: Desert Temple (DnT) (piazzato); Hellish Trials (piazzato); Jungle Temple (DnT) (spawn naturale); Philips' Ruins (spawner); Stronghold (DnT) (piazzato, spawn naturale)
- EAI Creeper launch: a volte si lancia contro il giocatore
- EAI Creeper swell: esplode anche attraverso i muri, a volte cammina innescato, sfonda muri (breach), raramente 'angry' più potente
- EAI Disable falling swelling: non si innesca cadendo
- EAI Jump: salta sul posto se sei poco più in alto
- EAI Riding: a volte cavalca altri mob
- EAI Sprint: a volte corre vicino al bersaglio
- EAI Tnt like creepers: a volte si innesca se colpito da un'esplosione
- Enhanced AI Creeper swell `Insane survival overhaul integration`: probabilmente senza effetto: scrive le chiavi `iguanatweaksreborn:explosion_*`, che Explosion Overhaul non legge (legge `knockback_multiplier`/`damage_multiplier`)
- Explosion Overhaul: esplosione dal centro del corpo, danno ridotto (x0.85), i blocchi distrutti droppano
- MPR `Better creeper lingering`: ?i Creeper con effetti di pozione lasciano una nuvola 3D esplodendo
- **OFF**: Parkour (feature spenta)

### Dolphin (`minecraft:dolphin`)  · D S T X
- **Dove (biomi)**: Overworld: Deep Lukewarm Ocean, Deep Ocean, Lukewarm Ocean, Ocean, Warm Ocean

### Donkey (`minecraft:donkey`)  · A D T X
- **Dove (biomi)**: Overworld: Meadow, Plains, Savanna, Savanna Plateau, Sunflower Plains, Windswept Savanna
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- ISO `Equine attributes`: statistiche fisse per specie (niente genetica), da `equine_attributes.json`
- EAI Stay near dismount: non si allontana da dove scendi
- Quark `Horses Swim`: nuotano con il giocatore in groppa
- Supplementaries Flute: richiamabile con il Flauto
- Supplementaries Sugar Cube: mangiato dà Speed
- **Cibo (tag)**: `survivalreimagined:donkey_food` = apple, enchanted_golden_apple, golden_apple, hay_block, sugar, wheat, supplementaries:flax, supplementaries:flax_block, supplementaries:sugar_cube (ultimo: datapack)

### Drowned (`minecraft:drowned`)  · D S T X
- **Dove (biomi)**: Overworld: Cold Ocean, Deep Cold Ocean, Deep Frozen Ocean, Deep Lukewarm Ocean, Deep Ocean, Dripstone Caves, Frozen Ocean, Frozen River, Lukewarm Ocean, Ocean, River, Warm Ocean
- **Strutture**: Jungle Temple (DnT) (spawn naturale); Ocean Monument (DnT) (trial spawner); Philips' Ruins (spawn naturale, spawner); Stronghold (DnT) (piazzato, spawn naturale)
- ISO `Zombie siege`: assedio di zombie anche lontano dai villaggi
- EAI Air steal: ruba aria colpendo
- EAI Better drowned swim up: salta fuori dall'acqua
- EAI Biting mobs: morde se colpito senza un'arma
- EAI Climbing: sale le scale a pioli
- EAI Drowned attack during day: attacca anche di giorno
- EAI Drowning targets: afferra i bersagli e li porta sott'acqua
- EAI Fisher mobs: a volte ha una canna da pesca e ti tira a sé
- EAI Jump: salta sul posto se sei poco più in alto
- EAI Leaders: alcuni sono leader e chiamano rinforzi
- EAI Lunge at target: si ferma un attimo e poi si lancia contro il bersaglio
- EAI MPR `overworld_zombies_equipment`: armatura (anche rame) e armi/attrezzi, più spesso con la luna piena, alla luce del cielo e in profondità
- EAI MPR `zombies`, `scale/zombies`: più piccoli a caso; nelle grotte dell'Overworld alcuni sono minatori (più in profondità, più spesso)
- EAI Pearler mobs: a volte ha Ender Pearl e le lancia per raggiungerti
- EAI Pick up and throw: a volte raccoglie altri mob e te li lancia
- EAI Riding: a volte cavalca altri mob
- EAI Sprint: a volte corre vicino al bersaglio
- EAI Sun resistant drowned: brucia al sole solo dopo un po'
- EAI Swimmers: nuoto più veloce
- Enhanced AI (MPR `drowned_trident_nerf`): il Tridente lanciato dai Drowned fa metà danno
- Enhanced AI (MPR `fuck_baby_zombies`): niente Zombie bambini: tutti spawnano adulti (vale per tutto `#minecraft:zombies`)
- Vanilla Backport `zombie_nautilus_spawn_chance` 0.5: metà dei Drowned negli oceani spawna in groppa a uno Zombie Nautilus
- **OFF**: Shielding (`Chance to equip` 0); Miner mobs da config (`Miner chance` 0); per gli zombie lo attiva MPR (vedi sotto); Parkour (feature spenta)

### Elder Guardian (`minecraft:elder_guardian`)  · D S T X
- **Dove (biomi)**: —
- **Strutture**: Ocean Monument (DnT) (piazzato, trial spawner)
- **Altre fonti**: nell'Ocean Monument (DnT Trident Trial Monument), piazzati e da trial spawner
- Progressive Bosses Elder Guardian: 3 livelli (0-2): ogni Elder ucciso alza di 1 il livello degli altri Elder entro 64 blocchi (più vita e assorbimento, attacco più rapido, più resistenza, minion più frequenti); assorbimento e cura a ogni colpo già dal livello 0; evoca Elder Minion (Guardian con metà vita e nuoto più veloce) se ci sono meno di 6 Guardian vicini. Gli Elder da `SPAWNER` (non trial) restano vanilla
- Progressive Bosses `Adventure` = false: non impedisce di rompere blocchi e la Mining Fatigue resta vanilla (il codice agisce solo con `Adventure` = true)

### Ender Dragon (`minecraft:ender_dragon`)
- **Dove (biomi)**: —
- **Altre fonti**: nell'End, si può far rinascere con 4 End Crystal sul portale
- Progressive Bosses Dragon: 2 definizioni: base (livello 0) e corrupted (livello 4 = respawn con 4 Corrupted End Crystal, ricetta End Crystal + Dragon Egg). Si rigenera da sola e dai cristalli (di più dai corrotti); distruggere un cristallo che la cura la ferisce; più danno in volo, meno da appollaiata e dalle esplosioni; si arrabbia col danno (più veloce, più attacchi); acid ball con nube, blast attack che respinge lontano, carica, minion Shulker; sotto metà vita può far rinascere cristalli (con Phantom); gabbie sulle torri, alcune con cristalli corrotti; cristalli immuni alle altre esplosioni; gabbie con ossidiana agli angoli. ?con 1-3 cristalli corrotti non c'è definizione: Drago vanilla?

### Enderman (`minecraft:enderman`)  · D X
- **Dove (biomi)**: quasi tutto l'Overworld (55/57; manca: Deep Dark, Mushroom Fields); Nether: Inverted Forest, Nether Wastes, Soul Sand Valley, Warped Forest, Weeping Valley; End: End Barrens, End Highlands, End Midlands, Small End Islands, The End
- **Strutture**: Jungle Temple (DnT) (spawn naturale); Stronghold (DnT) (piazzato, spawn naturale)
- EAI Climbing: sale le scale a pioli
- EAI Jump: salta sul posto se sei poco più in alto
- EAI Teleport anti-cheese: se lo bersagli da posti irraggiungibili si teletrasporta
- EAI Teleport to target: teletrasporta altri mob vicino al bersaglio
- Enhanced AI `Look anger cone`: si arrabbia guardandolo da un angolo più ampio
- Supplementaries `enderman_head`: la testa droppa e fa da componente redstone quando la guardi (pagina item già esistente?)
- **OFF**: Item disruption (feature spenta); Parkour (feature spenta)

### Endermite (`minecraft:endermite`)  · D S T X
- **Dove (biomi)**: —
- **Strutture**: Formations Nether (spawner); Philips' Ruins (spawner); Stronghold (DnT) (spawn naturale)
- **Altre fonti**: a volte da una Ender Pearl lanciata; spawner in Formations Nether e Philips' Ruins
- Supplementaries Cage: catturabile in gabbia

### Evoker (`minecraft:evoker`)  · D S T X
- **Dove (biomi)**: —
- **Strutture**: Incendium (piazzato); Philips' Ruins (piazzato); Woodland Mansion (DnT Illager Manor) (piazzato)
- **Altre fonti**: Woodland Mansion (DnT Illager Manor) e raid
- ISO Misc mobs `Passive regen chance`: si cura lentamente da solo
- EAI Climbing: sale le scale a pioli
- EAI Jump: salta sul posto se sei poco più in alto
- EAI Open doors: apre le porte
- EAI Sprint: a volte corre vicino al bersaglio
- Quark `Vexes Die With Their Masters` / Bits and Balance `despawnVexWithEvoker`: i Vex muoiono con il loro Evoker
- **OFF**: Parkour (feature spenta)

### Fox (`minecraft:fox`)  · A D S T X
- **Dove (biomi)**: Overworld: Dappled Forest, Grove, Old Growth Pine Taiga, Old Growth Spruce Taiga, Snowy Taiga, Taiga
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- ISO Misc mobs `Passive regen chance`: si cura lentamente da solo
- EAI MPR `small_animals`: attacco più debole
- Ecologics `foxesAttackSquirrels`: cacciano gli Squirrel
- Naturalist forest foxes/rabbits: spawn extra nelle foreste
- Supplementaries Cage: catturabile in gabbia
- Supplementaries Flute: richiamabile con il Flauto
- **Cibo (tag)**: `minecraft:fox_food` = glow_berries, sweet_berries (ultimo: minecraft)

### Frog (`minecraft:frog`)  · D S T X
- **Dove (biomi)**: Overworld: Mangrove Swamp, Swamp
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- Supplementaries Cage: catturabile in gabbia
- Supplementaries Jar: catturabile in un barattolo
- **Cibo (tag)**: `minecraft:frog_food` = slime_ball (ultimo: minecraft)

### Ghast (`minecraft:ghast`)  · D S T X
- **Dove (biomi)**: Nether: Ash Barrens, Basalt Deltas, Nether Wastes, Quartz Flats, Soul Sand Valley, Volcanic Deltas, Weeping Valley
- **Strutture**: Incendium (piazzato); Philips' Ruins (spawner)
- EAI Ghast shooting: più palle di fuoco, a volte anche senza vederti
- Vanilla Backport `dried_ghasts`: Dried Ghast (fossili del Nether, baratto coi Piglin) -> Ghastling -> Happy Ghast

### Glow Squid (`minecraft:glow_squid`)  · D S T X
- **Dove (biomi)**: quasi tutto l'Overworld (55/57; manca: Deep Dark, Sulfur Caves)
- EAI MPR `scale/sea_creatures`: dimensioni casuali

### Goat (`minecraft:goat`)  · A D S T X
- **Dove (biomi)**: Overworld: Frozen Peaks, Jagged Peaks, Snowy Slopes
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- ISO `Fluid cooldown`: si mungono una volta ogni tanto (anche lo stufato del Mooshroom)
- Supplementaries Cage: catturabile in gabbia da cucciolo
- Supplementaries Fodder: mangia il Fodder
- **Cibo (tag)**: `minecraft:goat_food` = wheat, supplementaries:flax (ultimo: supplementaries)

### Guardian (`minecraft:guardian`)  · D S T X
- **Dove (biomi)**: Overworld: Deep Cold Ocean, Deep Frozen Ocean, Deep Lukewarm Ocean, Deep Ocean
- **Strutture**: Ocean Monument (DnT) (trial spawner); Philips' Ruins (spawn naturale, spawner)
- ISO `Guardian magic damage only`: solo danno magico (ignora l'armatura)
- ISO `Guardians in deep oceans`: spawnano anche negli oceani profondi, sotto Y 32: più piccoli e con molta meno vita di quelli del Monumento

### Hoglin (`minecraft:hoglin`)  · D S T X
- **Dove (biomi)**: Nether: Crimson Forest
- **Strutture**: Bastion Remnant (piazzato); Hellish Trials (piazzato); Incendium (piazzato)
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `minecraft:hoglin_food` = crimson_fungus (ultimo: minecraft)

### Horse (`minecraft:horse`)  · A D T X
- **Dove (biomi)**: Overworld: Plains, Savanna, Savanna Plateau, Sunflower Plains, Windswept Savanna
- ISO Aging: vita molto lunga; invecchiano e muoiono di vecchiaia (`Die of old age` = true; una Poisonous Potato li ferma, vale per tutti i mob con un tag lifespan)
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- ISO `Equine attributes`: statistiche fisse per specie (niente genetica), da `equine_attributes.json`
- EAI Stay near dismount: non si allontana da dove scendi
- Bits and Balance `dualRiders`: due giocatori sullo stesso cavallo
- Quark `Horses Swim`: nuotano con il giocatore in groppa
- Supplementaries Flute: richiamabile con il Flauto
- Supplementaries Sugar Cube: mangiato dà Speed
- **Cibo (tag)**: `minecraft:horse_food` = apple, enchanted_golden_apple, golden_apple, hay_block, sugar, wheat, supplementaries:flax, supplementaries:flax_block, supplementaries:sugar_cube (ultimo: supplementaries) · `minecraft:horse_tempt_items` = apple, carrot, enchanted_golden_apple, golden_apple, supplementaries:sugar_cube (ultimo: supplementaries)

### Husk (`minecraft:husk`)  · D S T X
- **Dove (biomi)**: Overworld: Desert
- **Strutture**: Desert Temple (DnT) (piazzato); Jungle Temple (DnT) (piazzato); Philips' Ruins (piazzato, spawner); Trial Chambers (trial spawner)
- ISO `Zombie siege`: assedio di zombie anche lontano dai villaggi
- EAI Biting mobs: morde se colpito senza un'arma
- EAI Climbing: sale le scale a pioli
- EAI Fisher mobs: a volte ha una canna da pesca e ti tira a sé
- EAI Jump: salta sul posto se sei poco più in alto
- EAI Leaders: alcuni sono leader e chiamano rinforzi
- EAI Lunge at target: si ferma un attimo e poi si lancia contro il bersaglio
- EAI MPR `overworld_zombies_equipment`: armatura (anche rame) e armi/attrezzi, più spesso con la luna piena, alla luce del cielo e in profondità
- EAI MPR `zombies`, `scale/zombies`: più piccoli a caso; nelle grotte dell'Overworld alcuni sono minatori (più in profondità, più spesso)
- EAI Pearler mobs: a volte ha Ender Pearl e le lancia per raggiungerti
- EAI Pick up and throw: a volte raccoglie altri mob e te li lancia
- EAI Riding: a volte cavalca altri mob
- EAI Sprint: a volte corre vicino al bersaglio
- Enhanced AI (MPR `fuck_baby_zombies`): niente Zombie bambini: tutti spawnano adulti (vale per tutto `#minecraft:zombies`)
- Vanilla Backport `has_camel_husks`: ?nei deserti può cavalcare un Camel Husk (con un Parched dietro)
- **OFF**: Shielding (`Chance to equip` 0); Miner mobs da config (`Miner chance` 0); per gli zombie lo attiva MPR (vedi sotto); Parkour (feature spenta)

### Iron Golem (`minecraft:iron_golem`)  · D S T X
- **Dove (biomi)**: —
- **Strutture**: Pillager Outpost (piazzato); Stronghold (DnT) (piazzato); Woodland Mansion (DnT Illager Manor) (piazzato)
- **Altre fonti**: si costruisce (4 blocchi di ferro + Carved Pumpkin); ?i villager lo evocano (nei villaggi abbandonati non ci sono villager); piazzato in Pillager Outpost (gabbia), Woodland Mansion, Stronghold (DnT)
- ISO `Fixed iron golem damage`: danno fisso invece che casuale
- EAI MPR `iron_golems`: subisce molto meno danno e quasi non viene spinto
- EAI Patrol: torna dove è spawnato
- EAI Villager golem repair: riparato dai fabbri, va da loro se ferito
- Bits and Balance `ironGolemsKillCreepers` = false: spento
- Enhanced AI `Custom targeting`: metà dei mostri in `#enhancedai:config/can_attack_iron_golem` lo attacca
- **OFF**: Falling shockwave (feature spenta)

### Llama (`minecraft:llama`)  · D T X
- **Dove (biomi)**: Overworld: Savanna Plateau, Windswept Forest, Windswept Gravelly Hills, Windswept Hills
- ISO Aging: vita molto lunga
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- ISO `Equine attributes`: statistiche fisse per specie (niente genetica), da `equine_attributes.json`
- EAI Stay near dismount: non si allontana da dove scendi
- Supplementaries Flute: richiamabile con il Flauto
- **Cibo (tag)**: `minecraft:llama_food` = hay_block, wheat, supplementaries:flax (ultimo: supplementaries) · `minecraft:llama_tempt_items` = hay_block (ultimo: minecraft)

### Magma Cube (`minecraft:magma_cube`)  · D S T X
- **Dove (biomi)**: Nether: Ash Barrens, Basalt Deltas, Infernal Dunes, Nether Wastes, Toxic Heap, Volcanic Deltas, Weeping Valley, Withered Forest
- **Strutture**: Bastion Remnant (spawner); Fortezza del Nether (DnT) (spawn naturale, trial spawner); Hellish Trials (trial spawner); Incendium (piazzato, spawner); Moog's Nether Structures (spawn naturale); Philips' Ruins (piazzato, spawner)
- EAI Magma cube surf speed: veloce nella lava
- EAI Slime jump delay: salta più spesso
- EAI Slime size: può spawnare più grande
- Enhanced AI `Slime attack fix`: fanno danno al salto e all'atterraggio, non a ogni tick di contatto
- Supplementaries Cage: catturabile in gabbia
- Supplementaries Jar: catturabile in un barattolo

### Mooshroom (`minecraft:mooshroom`)  · A D S T X
- **Dove (biomi)**: Overworld: Mushroom Fields
- ISO Aging: vita lunga
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- ISO `Fluid cooldown`: si mungono una volta ogni tanto (anche lo stufato del Mooshroom)
- Mooshroom Tweaks `becomeBrownChance` 0.5: ?metà dei Mooshroom è marrone
- Supplementaries Fodder: mangia il Fodder
- **Cibo (tag)**: `survivalreimagined:mooshroom_food` = wheat, supplementaries:flax (ultimo: datapack)

### Mule (`minecraft:mule`)  · A D T X
- **Dove (biomi)**: —
- **Altre fonti**: da Cavallo + Asino; con ISO `prevent_breeding` ?solo se si innamorano da soli
- ISO `Equine attributes`: statistiche fisse per specie (niente genetica), da `equine_attributes.json`
- EAI Stay near dismount: non si allontana da dove scendi
- Quark `Horses Swim`: nuotano con il giocatore in groppa
- Supplementaries Flute: richiamabile con il Flauto
- Supplementaries Sugar Cube: mangiato dà Speed
- **Cibo (tag)**: `survivalreimagined:mule_food` = apple, enchanted_golden_apple, golden_apple, hay_block, sugar, wheat, supplementaries:flax, supplementaries:flax_block, supplementaries:sugar_cube (ultimo: datapack)

### Ocelot (`minecraft:ocelot`)  · D S T X
- **Dove (biomi)**: Overworld: Bamboo Jungle, Jungle
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Misc mobs `Passive regen chance`: si cura lentamente da solo
- ISO `Ocelot to cat`: addomesticato diventa un Gatto
- Supplementaries Cage: catturabile in gabbia
- **Cibo (tag)**: `minecraft:ocelot_food` = cod, salmon, naturalist:anglerfish, naturalist:bass, naturalist:blobfish, naturalist:catfish, naturalist:piranha (ultimo: naturalist)

### Panda (`minecraft:panda`)  · D S T X
- **Dove (biomi)**: Overworld: Bamboo Jungle, Jungle
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `minecraft:panda_food` = bamboo (ultimo: minecraft)

### Parrot (`minecraft:parrot`)  · D S T X
- **Dove (biomi)**: Overworld: Bamboo Jungle, Jungle
- ISO Aging: vita molto lunga; invecchiano e muoiono di vecchiaia (`Die of old age` = true; una Poisonous Potato li ferma, vale per tutti i mob con un tag lifespan)
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- ISO Livestock: addomesticati e fatti innamorare solo con Semi di Melone e Zucca
- ISO Misc mobs `Passive regen chance`: si cura lentamente da solo
- ISO `Shoulder dismount fall distance` 4: cadono dalla spalla solo dopo una caduta di qualche blocco
- Amendments `pets_follow_teleports`: gli animali che ti seguono si teletrasportano con te (anche portali)
- Bits and Balance `friendlyFireFriendlies`: non puoi colpire per sbaglio i tuoi animali
- Naturalist `parrot_flight`: ?con un Parrot per spalla e un Bird in testa si vola lentamente (changelog 2.0)
- Supplementaries Cage: catturabile in gabbia
- Vibrant Parrots: colori diversi; innamorati depongono un uovo del loro colore; restano sulla spalla in volo/caduta; si tolgono accovacciandosi; Bird Cage
- **Cibo (tag)**: `minecraft:parrot_food` = melon_seeds, pumpkin_seeds, supplementaries:flax_seeds (ultimo: supplementaries)

### Phantom (`minecraft:phantom`)  · D S T X
- **Dove (biomi)**: Nether: Toxic Heap, Withered Forest
- ISO `Tired tied phantoms`: spawnano in base alla stanchezza (Tired II+), non all'insonnia
- EAI Grabbing phantoms: afferra e porta in aria finché non lo colpisci
- Bits and Balance `enableImprovedPhantoms`: i colpi danno Slowness che si accumula; Pickup è spento, le altre opzioni (doppio danno, caduta) ?valgono solo per il suo Pickup o anche per la presa di Enhanced AI
- Enhanced AI (MPR `scale/phantoms`): dimensioni casuali, fino a molto più grandi

### Pig (`minecraft:pig`)  · A D S T X
- **Dove (biomi)**: Overworld: Bamboo Jungle, Cherry Grove, Jungle, Old Growth Pine Taiga, Old Growth Spruce Taiga, Plains, Snowy Taiga, Sparse Jungle, Sunflower Plains, Taiga, Windswept Forest, Windswept Gravelly Hills, Windswept Hills
- **Strutture**: Woodland Mansion (DnT Illager Manor) (piazzato)
- ISO Aging: vita media
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- Naturalist `remove_farm_animals_savanna/swamp`: niente in savane e paludi
- Naturalist `remove_forest_pigs`: niente maiali nelle foreste
- Supplementaries Cage: catturabile in gabbia da cucciolo
- Supplementaries Fodder: mangia il Fodder
- Vanilla Backport `farm_animal_variants` = false: spento: nessuna variante
- **Cibo (tag)**: `minecraft:pig_food` = beetroot, carrot, potato (ultimo: minecraft)

### Piglin (`minecraft:piglin`)  · D S T X
- **Dove (biomi)**: Nether: Ash Barrens, Crimson Forest, Nether Wastes
- **Strutture**: Bastion Remnant (piazzato); Fortezza del Nether (DnT) (piazzato); Incendium (piazzato); Moog's Nether Structures (spawn naturale)
- EAI Climbing: sale le scale a pioli
- EAI Lunge at target: si ferma un attimo e poi si lancia contro il bersaglio
- EAI Sprint: a volte corre vicino al bersaglio
- **OFF**: Shielding (`Chance to equip` 0); Parkour (feature spenta)
- **Cibo (tag)**: `minecraft:piglin_food` = cooked_porkchop, porkchop, naturalist:bushmeat, naturalist:cooked_bushmeat (ultimo: naturalist)

### Piglin Brute (`minecraft:piglin_brute`)  · D S T X
- **Dove (biomi)**: —
- **Strutture**: Bastion Remnant (piazzato); Formations Nether (spawner); Incendium (piazzato)
- **Altre fonti**: Bastion Remnant; spawner in Formations Nether; Incendium
- EAI Climbing: sale le scale a pioli
- EAI Jump: salta sul posto se sei poco più in alto
- EAI Lunge at target: si ferma un attimo e poi si lancia contro il bersaglio
- EAI Sprint: a volte corre vicino al bersaglio
- **OFF**: Shielding (`Chance to equip` 0); Parkour (feature spenta)

### Pillager (`minecraft:pillager`)  · D T X
- **Dove (biomi)**: —
- **Strutture**: Incendium (piazzato); Philips' Ruins (piazzato); Pillager Outpost (spawn naturale); Woodland Mansion (DnT Illager Manor) (piazzato)
- **Altre fonti**: Pillager Outpost, pattuglie nell'Overworld, raid; Woodland Mansion (DnT)
- ISO Misc mobs `Passive regen chance`: si cura lentamente da solo
- ISO villagers overhaul: fonte di Smeraldi; pattuglie e raid attivi (`WSCommands.toml`)
- EAI Climbing: sale le scale a pioli
- EAI Flee target: a volte si tiene a distanza
- EAI Open doors: apre le porte
- EAI Pillager shoot: tira più lontano e più preciso
- EAI Sprint: a volte corre vicino al bersaglio
- **OFF**: Shielding (`Chance to equip` 0); Parkour (feature spenta)

### Polar Bear (`minecraft:polar_bear`)  · D S T X
- **Dove (biomi)**: Overworld: Deep Frozen Ocean, Frozen Ocean, Ice Spikes, Snowy Plains

### Pufferfish (`minecraft:pufferfish`)  · D S T X
- **Dove (biomi)**: Overworld: Deep Lukewarm Ocean, Lukewarm Ocean, Warm Ocean
- EAI MPR `scale/sea_creatures`: dimensioni casuali

### Rabbit (`minecraft:rabbit`)  · A D S T X
- **Dove (biomi)**: Overworld: Cherry Grove, Dappled Forest, Desert, Flower Forest, Grove, Ice Spikes, Meadow, Old Growth Pine Taiga, Old Growth Spruce Taiga, Snowy Plains, Snowy Slopes, Snowy Taiga, Taiga
- ISO Aging: vita breve
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- EAI MPR `small_animals`: attacco più debole
- Naturalist forest foxes/rabbits: spawn extra nelle foreste
- Quark `Safer Creatures`: meno danno da caduta
- Supplementaries Cage: catturabile in gabbia
- Supplementaries Jar: catturabile in un barattolo da cucciolo
- **Cibo (tag)**: `minecraft:rabbit_food` = carrot, dandelion, golden_carrot (ultimo: minecraft)

### Ravager (`minecraft:ravager`)  · D S T X
- **Dove (biomi)**: —
- **Strutture**: Incendium (piazzato); Woodland Mansion (DnT Illager Manor) (piazzato)
- **Altre fonti**: raid; Woodland Mansion (DnT)
- ISO Misc mobs `Passive regen chance`: si cura lentamente da solo

### Salmon (`minecraft:salmon`)  · D S T X
- **Dove (biomi)**: Overworld: Cold Ocean, Deep Cold Ocean, Deep Frozen Ocean, Frozen Ocean, Frozen River, River
- EAI MPR `scale/sea_creatures`: dimensioni casuali

### Sheep (`minecraft:sheep`)  · A D S T X
- **Dove (biomi)**: Overworld: Bamboo Jungle, Birch Forest, Cherry Grove, Dappled Forest, Dark Forest, Flower Forest, Forest, Grove, Jungle, Meadow, Old Growth Birch Forest, Old Growth Pine Taiga, Old Growth Spruce Taiga, Plains, Snowy Taiga, Sparse Jungle, Sunflower Plains, Taiga, Windswept Forest, Windswept Gravelly Hills, Windswept Hills
- **Strutture**: Woodland Mansion (DnT Illager Manor) (piazzato)
- ISO Aging: vita lunga; adulti e anziani danno più lana
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- Name Tag Upgrade: il nome si toglie con le cesoie (prima la lana)
- Naturalist `remove_farm_animals_savanna/swamp`: niente in savane e paludi
- Supplementaries Cage: catturabile in gabbia da cucciolo
- Supplementaries Fodder: mangia il Fodder
- **Cibo (tag)**: `minecraft:sheep_food` = wheat, supplementaries:flax (ultimo: supplementaries)

### Shulker (`minecraft:shulker`)  · D S T X
- **Dove (biomi)**: —
- **Strutture**: Philips' Ruins (piazzato)
- **Altre fonti**: End City; Philips' Ruins (End Gate Fortress)
- EAI Shulker armor: armatura anche da aperto e da socchiuso
- Bits and Balance `despawnBulletsWithShulker`: i proiettili spariscono con lo Shulker
- Enhanced AI `Shulker armor`/`bullets`/`attack`: armatura anche da aperto e da socchiuso (chiuso poco più del vanilla); sotto metà vita si apre solo a metà mentre spara; spara meno spesso; Levitation VI ma più breve (5 s, 8 s su Hard, contro 10 s di Levitation I)

### Silverfish (`minecraft:silverfish`)  · T X
- **Dove (biomi)**: —
- **Strutture**: Adventure Dungeons (trial spawner); Philips' Ruins (piazzato, spawner); Stronghold (DnT) (spawner); Trial Chambers (trial spawner)
- **Altre fonti**: dai blocchi infestati (Stronghold, montagne); spawner nello Stronghold (DnT)
- Enhanced AI `Silverfish merge with stone` / `wake up friends`
- Supplementaries Urn: può uscire dalle Urne rotte nelle grotte

### Skeleton (`minecraft:skeleton`)  · D S T X
- **Dove (biomi)**: quasi tutto l'Overworld (55/57; manca: Deep Dark, Mushroom Fields); Nether: Quartz Flats, Soul Sand Valley, Weeping Valley
- **Strutture**: Adventure Dungeons (spawner); Desert Temple (DnT) (piazzato); Fortezza del Nether (DnT) (spawn naturale, trial spawner); Hellish Trials (trial spawner); Immersive Gateways (spawner); Incendium (piazzato); Jungle Temple (DnT) (spawn naturale); Moog's Nether Structures (piazzato, spawn naturale); Philips' Ruins (piazzato, spawn naturale, spawner); Stronghold (DnT) (piazzato, spawn naturale); Trial Chambers (trial spawner)
- **Altre fonti**: spawner nei Dungeon
- ISO `Remove skeletons from fortresses`: non spawna più nelle Fortezze del Nether (anche se lo `spawn_overrides` di DnT lo elenca)
- EAI Climbing: sale le scale a pioli
- EAI Leaders: alcuni sono leader e chiamano rinforzi
- EAI Lunge at target: si ferma un attimo e poi si lancia contro il bersaglio
- EAI MPR `overworld_skeletons`: armatura (più spesso con la luna piena e in profondità), meno preciso
- EAI MPR `scale/skeletons`: più piccoli a caso
- EAI Riding: a volte cavalca altri mob
- EAI Skeleton flee target: si allontana se ti avvicini
- EAI Skeleton shoot: tira più lontano, più spesso e si sposta di lato
- Bits and Balance `tippedArrowLingeringClouds.mobsEnabled`: ?solo se ha frecce con effetto (es. Faretra di Supplementaries)
- Supplementaries `quiver_skeleton_spawn_chance`: raramente spawna con una Faretra (dipende dalla difficoltà locale)
- **OFF**: Shielding (`Chance to equip` 0); Parkour (feature spenta)

### Skeleton Horse (`minecraft:skeleton_horse`)  · A D T X
- **Dove (biomi)**: —
- **Altre fonti**: trappola: un fulmine durante un temporale crea 4 cavalieri scheletro
- ISO `Equine attributes`: statistiche fisse per specie (niente genetica), da `equine_attributes.json`
- EAI Stay near dismount: non si allontana da dove scendi
- Quark `Horses Swim`: nuotano con il giocatore in groppa
- Supplementaries Flute: richiamabile con il Flauto

### Slime (`minecraft:slime`)  · D S T X
- **Dove (biomi)**: quasi tutto l'Overworld (55/57; manca: Deep Dark, Mushroom Fields)
- **Strutture**: Adventure Dungeons (trial spawner); Incendium (piazzato); Jungle Temple (DnT) (spawn naturale); Stronghold (DnT) (piazzato, spawn naturale); Trial Chambers (trial spawner)
- EAI Slime jump delay: salta più spesso
- EAI Slime size: può spawnare più grande
- Enhanced AI `Slime attack fix`: fanno danno al salto e all'atterraggio, non a ogni tick di contatto
- Quark `Safer Creatures`: niente danno da caduta
- Quark `Slime In A Bucket`: gli Slime piccoli si raccolgono con un secchio (fanno saltellare nei chunk slime)
- Quark `Slimes To Magma Cubes`: uno Slime ucciso da un Magma Block (danno `hotFloor`) si divide in Magma Cube
- Supplementaries Cage: catturabile in gabbia
- Supplementaries Jar: catturabile in un barattolo
- Supplementaries Urn: può uscire dalle Urne rotte nelle grotte

### Sniffer (`minecraft:sniffer`)  · A D S T X
- **Dove (biomi)**: —
- **Altre fonti**: solo da Sniffer Egg (archeologia nelle Warm Ocean Ruins)
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `minecraft:sniffer_food` = torchflower_seeds (ultimo: minecraft)

### Snow Golem (`minecraft:snow_golem`)  · D S T X
- **Dove (biomi)**: —
- **Altre fonti**: si costruisce (2 blocchi di neve + Carved Pumpkin)
- EAI Climbing: sale le scale a pioli
- EAI Healed by snowballs: curato dalle palle di neve
- EAI MPR `snow_golems`: ha un po' di armatura
- EAI Snow golems: le palle di neve fanno danno; e congelano
- Quark `Snow Golem Player Heads`: ?uno Snow Golem con nome di un giocatore ucciso da una Witch droppa la testa del giocatore

### Spider (`minecraft:spider`)  · D S T X
- **Dove (biomi)**: quasi tutto l'Overworld (54/57; manca: Deep Dark, Mushroom Fields, Sulfur Caves)
- **Strutture**: Adventure Dungeons (trial spawner); Jungle Temple (DnT) (spawn naturale); Stronghold (DnT) (spawn naturale); Trial Chambers (trial spawner); Woodland Mansion (DnT Illager Manor) (spawner)
- **Altre fonti**: spawner nei Dungeon
- EAI MPR `spiders`: quasi niente danno da caduta, un po' più lento
- EAI Riding: altri mob possono cavalcarlo
- EAI Web thrower: a volte lancia ragnatele che rallentano
- Enhanced AI (MPR `scale/spider`): più piccolo dei Ragni vanilla
- Enhanced AI `Stuck fix`: non restano più bloccati sui muri
- **OFF**: Parkour (feature spenta)

### Squid (`minecraft:squid`)  · D S T X
- **Dove (biomi)**: Overworld: Cold Ocean, Deep Cold Ocean, Deep Frozen Ocean, Deep Lukewarm Ocean, Deep Ocean, Frozen Ocean, Frozen River, Lukewarm Ocean, Ocean, River, Warm Ocean
- EAI MPR `scale/sea_creatures`: dimensioni casuali

### Stray (`minecraft:stray`)  · D S T X
- **Dove (biomi)**: Overworld: Ice Spikes, Snowy Plains
- **Strutture**: Adventure Dungeons (trial spawner); Philips' Ruins (spawner); Trial Chambers (trial spawner)
- EAI Climbing: sale le scale a pioli
- EAI Leaders: alcuni sono leader e chiamano rinforzi
- EAI Lunge at target: si ferma un attimo e poi si lancia contro il bersaglio
- EAI MPR `overworld_skeletons`: armatura (più spesso con la luna piena e in profondità), meno preciso
- EAI MPR `scale/skeletons`: più piccoli a caso
- EAI Riding: a volte cavalca altri mob
- EAI Skeleton flee target: si allontana se ti avvicini
- EAI Skeleton shoot: tira più lontano, più spesso e si sposta di lato
- Bits and Balance `tippedArrowLingeringClouds.mobsEnabled`: le sue frecce con effetto lasciano una nuvola dell'effetto dove atterrano (vale per tutte le frecce con effetto, anche dei giocatori: va sulla pagina della Tipped Arrow, qui solo un accenno)
- **OFF**: Shielding (`Chance to equip` 0); Parkour (feature spenta)

### Strider (`minecraft:strider`)  · D S T X
- **Dove (biomi)**: Nether: Ash Barrens, Basalt Deltas, Crimson Forest, Infernal Dunes, Inverted Forest, Nether Wastes, Quartz Flats, Soul Sand Valley, Toxic Heap, Volcanic Deltas, Warped Forest, Weeping Valley
- **Strutture**: Incendium (piazzato)
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `minecraft:strider_food` = warped_fungus (ultimo: minecraft) · `minecraft:strider_tempt_items` = warped_fungus, warped_fungus_on_a_stick (ultimo: minecraft)

### Tadpole (`minecraft:tadpole`)  · D S T X
- **Dove (biomi)**: —
- **Altre fonti**: dalla Frogspawn che le Rane depongono

### Trader Llama (`minecraft:trader_llama`)  · D T X
- **Dove (biomi)**: —
- **Altre fonti**: con il Wandering Trader
- ISO Aging: vita molto lunga
- ISO `Equine attributes`: statistiche fisse per specie (niente genetica), da `equine_attributes.json`
- EAI Stay near dismount: non si allontana da dove scendi
- **Cibo (tag)**: `survivalreimagined:trader_llama_food` = hay_block, wheat, supplementaries:flax (ultimo: datapack)

### Tropical Fish (`minecraft:tropical_fish`)  · D S T X
- **Dove (biomi)**: Overworld: Deep Lukewarm Ocean, Lukewarm Ocean, Lush Caves, Mangrove Swamp, Warm Ocean
- **Strutture**: Woodland Mansion (DnT Illager Manor) (piazzato)
- EAI MPR `scale/sea_creatures`: dimensioni casuali

### Turtle (`minecraft:turtle`)  · D S T X
- **Dove (biomi)**: Overworld: Beach
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- ISO `Scutes`: le scaglie cadono come blocco impilabile
- **Cibo (tag)**: `minecraft:turtle_food` = seagrass (ultimo: minecraft)

### Vex (`minecraft:vex`)  · D S T X
- **Dove (biomi)**: —
- **Strutture**: Incendium (spawner)
- **Altre fonti**: evocati dagli Evoker; spawner in Incendium (Sanctum)
- Enhanced AI (MPR `fuck_vexes`, `scale/vexes`): molta meno vita, più grande
- Quark `Vexes Die With Their Masters` / Bits and Balance `despawnVexWithEvoker`: i Vex muoiono con il loro Evoker
- Supplementaries Cage: catturabile in gabbia

### Villager (`minecraft:villager`)  · D S T X
- **Dove (biomi)**: —
- **Strutture**: Igloo (piazzato); Moog's Structure Lib (piazzato); Stronghold (DnT) (piazzato); Woodland Mansion (DnT Illager Manor) (piazzato)
- **Altre fonti**: solo curando Zombie Villager (ISO); pochi nelle strutture: cella dello Stronghold (DnT), Woodland Mansion (DnT), Igloo
- ISO Misc mobs `Passive regen chance`: si cura lentamente da solo
- ISO Villagers: solo curando Zombie Villager; niente riproduzione; commerciano solo vendendo per 1 Smeraldo; prezzi che salgono e non scendono; 1 restock al giorno; mantengono i trade se perdono il job site
- EAI Villager alert protectors: se in pericolo avvisa gli Iron Golem
- EAI Villager attacking: si difende
- EAI Villager eat to heal: mangia per curarsi
- EAI Villager golem repair: i fabbri riparano gli Iron Golem
- Enhanced AI `Custom targeting`: metà dei mostri in `#enhancedai:config/can_attack_villagers` li attacca
- Enhanced AI `Villager attacking`: reagiscono solo ai giocatori con reputazione sotto -100 (come gli Iron Golem); `Villagers fight back enemies` = false, quindi non attaccano i mostri
- Quark `Villagers Follow Emeralds`: ti seguono se tieni uno Smeraldo

### Vindicator (`minecraft:vindicator`)  · D S T X
- **Dove (biomi)**: —
- **Strutture**: Incendium (piazzato); Woodland Mansion (DnT Illager Manor) (piazzato)
- **Altre fonti**: Woodland Mansion (DnT Illager Manor), raid
- ISO Misc mobs `Passive regen chance`: si cura lentamente da solo
- EAI Climbing: sale le scale a pioli
- EAI Jump: salta sul posto se sei poco più in alto
- EAI Lunge at target: si ferma un attimo e poi si lancia contro il bersaglio
- EAI Open doors: apre le porte
- EAI Sprint: a volte corre vicino al bersaglio
- Enhanced AI (MPR `fuck_vindicators`): molto meno danno
- **OFF**: Shielding (`Chance to equip` 0); Parkour (feature spenta)

### Wandering Trader (`minecraft:wandering_trader`)  · D S T X
- **Dove (biomi)**: —
- **Altre fonti**: compare vicino ai giocatori ogni tanto (attivo in `WSCommands.toml`)
- ISO villagers overhaul: trade propri (ISO), attivo via `WSCommands.toml`
- EAI Climbing: sale le scale a pioli
- EAI Jump: salta sul posto se sei poco più in alto
- **OFF**: Parkour (feature spenta)

### Warden (`minecraft:warden`)  · D S
- **Dove (biomi)**: —
- **Altre fonti**: evocato dagli Sculk Shrieker nel Deep Dark (Ancient City)
- ISO `Warden`: si evoca più facilmente: bastano 2 avvisi degli Sculk Shrieker, e gli avvisi calano più lentamente
- Enhanced AI (MPR `warden`): sale i blocchi interi senza saltare
- Enhanced AI `Warden darkness/listen/sonic boom range`: Darkness e Sonic Boom da molto più lontano, sente le vibrazioni più lontano

### Witch (`minecraft:witch`)  · D T X
- **Dove (biomi)**: quasi tutto l'Overworld (55/57; manca: Deep Dark, Mushroom Fields)
- **Strutture**: Jungle Temple (DnT) (spawn naturale); Philips' Ruins (spawner); Stronghold (DnT) (spawn naturale); Swamp Hut (DnT) (piazzato, spawn naturale); Woodland Mansion (DnT Illager Manor) (piazzato)
- **Altre fonti**: raid
- ISO Misc mobs `Passive regen chance`: si cura lentamente da solo
- EAI Allied monsters: lancia pozioni buone ai mostri vicini
- EAI Climbing: sale le scale a pioli
- EAI Flee target: a volte si tiene a distanza
- EAI Thirsty witches: beve più pozioni
- EAI Witch potion throwing: lancia più lontano, più veloce e più tipi di pozione
- Enhanced AI `Dark art` = false: spento: non evocano villager
- **OFF**: Dark art (feature spenta)

### Wither (`minecraft:wither`)
- **Dove (biomi)**: —
- **Altre fonti**: si costruisce (4 Soul Sand + 3 teschi di Wither Skeleton)
- Explosion Overhaul: nessun knockback dalle esplosioni
- Progressive Bosses Wither: 4 varianti: base (evocazione normale) e, con Corrupted Soul Sand al centro (1/2/3 Nether Star), armored, summoner, ultimate (solo nel Nether). Tutte: si rigenera, si cura con le uccisioni dei teschi, raffiche di teschi quando colpito, cariche sotto metà vita e se non ti vede, esplode alla morte, ogni uccisione lascia una Wither Rose. Armored: armatura alta; summoner: Wither Minion (alcuni con arco) e cura alta; ultimate: tutto. Dalla armored in su le esplosioni ignorano i blocchi wither-proof

### Wither Skeleton (`minecraft:wither_skeleton`)  · D S T X
- **Dove (biomi)**: Nether: Withered Forest
- **Strutture**: Formations Nether (spawner); Fortezza del Nether (DnT) (piazzato, spawn naturale, trial spawner); Hellish Trials (trial spawner); Incendium (piazzato); Moog's Nether Structures (piazzato, spawn naturale); Philips' Ruins (piazzato, spawn naturale, spawner)
- EAI Climbing: sale le scale a pioli
- EAI Jump: salta sul posto se sei poco più in alto
- EAI Lunge at target: si ferma un attimo e poi si lancia contro il bersaglio
- EAI MPR `scale/skeletons`: più piccoli a caso
- EAI Skeleton flee target: si allontana se ti avvicini
- EAI Skeleton shoot: tira più lontano, più spesso e si sposta di lato
- EAI Sprint: a volte corre vicino al bersaglio
- Enhanced AI (MPR `wither_skeleton`): a volte spawna con un arco (a volte incantato)
- Enhanced AI `Wither instead of fire`: con l'arco tira frecce di Wither invece che infuocate
- Progressive Bosses `no_wither_rose`: se ucciso dal Wither non lascia la Wither Rose
- **OFF**: Shielding (`Chance to equip` 0); Parkour (feature spenta)

### Wolf (`minecraft:wolf`)  · D T X
- **Dove (biomi)**: Overworld: Forest, Grove, Old Growth Pine Taiga, Old Growth Spruce Taiga, Snowy Taiga, Taiga
- ISO Aging: vita molto lunga; invecchiano e muoiono di vecchiaia (`Die of old age` = true; una Poisonous Potato li ferma, vale per tutti i mob con un tag lifespan)
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- ISO Misc mobs `Passive regen chance`: si cura lentamente da solo
- EAI MPR `slow_passive_healing`: si cura lentamente da solo
- EAI MPR `wolves`: più veloce
- Amendments `pets_follow_teleports`: gli animali che ti seguono si teletrasportano con te (anche portali)
- Bits and Balance `friendlyFireFriendlies`: non puoi colpire per sbaglio i tuoi animali
- Bits and Balance `speedyWolves`: i lupi addomesticati accelerano per raggiungerti
- Let Sleeping Dogs Lie: seduti a lungo si sdraiano
- Quark `Pat The Dogs`: si accarezzano (tasto destro a mano vuota da accovacciato)
- Vanilla Backport `wolf_sound_variants`: varianti di verso
- **Cibo (tag)**: `minecraft:wolf_food` = ecologics:crab_meat, beef, chicken, cooked_beef, cooked_chicken, cooked_mutton, cooked_porkchop, cooked_rabbit, mutton, porkchop ... (ultimo: minecraft)

### Zoglin (`minecraft:zoglin`)  · D S T X
- **Dove (biomi)**: —
- **Strutture**: Philips' Ruins (spawner)
- **Altre fonti**: Hoglin portato nell'Overworld; spawner in Philips' Ruins

### Zombie (`minecraft:zombie`)  · D S T X
- **Dove (biomi)**: quasi tutto l'Overworld (55/57; manca: Deep Dark, Mushroom Fields)
- **Strutture**: Adventure Dungeons (spawner, trial spawner); Immersive Gateways (spawner); Jungle Temple (DnT) (piazzato, spawn naturale); Philips' Ruins (piazzato, spawn naturale, spawner); Stronghold (DnT) (piazzato, spawn naturale); Trial Chambers (trial spawner)
- **Altre fonti**: spawner nei Dungeon
- ISO `Always convert zombie`: i villager uccisi dagli zombie diventano sempre Zombie Villager
- ISO `Zombie siege`: assedio di zombie anche lontano dai villaggi
- EAI Biting mobs: morde se colpito senza un'arma
- EAI Climbing: sale le scale a pioli
- EAI Fisher mobs: a volte ha una canna da pesca e ti tira a sé
- EAI Jump: salta sul posto se sei poco più in alto
- EAI Leaders: alcuni sono leader e chiamano rinforzi
- EAI Lunge at target: si ferma un attimo e poi si lancia contro il bersaglio
- EAI MPR `overworld_zombies_equipment`: armatura (anche rame) e armi/attrezzi, più spesso con la luna piena, alla luce del cielo e in profondità
- EAI MPR `zombies`, `scale/zombies`: più piccoli a caso; nelle grotte dell'Overworld alcuni sono minatori (più in profondità, più spesso)
- EAI Pearler mobs: a volte ha Ender Pearl e le lancia per raggiungerti
- EAI Pick up and throw: a volte raccoglie altri mob e te li lancia
- EAI Riding: a volte cavalca altri mob
- EAI Sprint: a volte corre vicino al bersaglio
- Enhanced AI (MPR `fuck_baby_zombies`): niente Zombie bambini: tutti spawnano adulti (vale per tutto `#minecraft:zombies`)
- **OFF**: Shielding (`Chance to equip` 0); Miner mobs da config (`Miner chance` 0); per gli zombie lo attiva MPR (vedi sotto); Parkour (feature spenta)

### Zombie Horse (`minecraft:zombie_horse`)
- **Dove (biomi)**: —
- **Altre fonti**: Vanilla Backport: di notte in Plains, Snowy Plains e savane (`spawns_zombie_horses`)
- ISO `Equine attributes`: statistiche fisse per specie (niente genetica), da `equine_attributes.json`
- EAI Stay near dismount: non si allontana da dove scendi
- Quark `Horses Swim`: nuotano con il giocatore in groppa
- Supplementaries Flute: richiamabile con il Flauto
- Vanilla Backport `has_zombie_horses`: spawna di notte in pianure e savane ?con uno Zombie in sella
- **Cibo (tag)**: `minecraft:zombie_horse_food` = red_mushroom (ultimo: VanillaBackport)

### Zombie Villager (`minecraft:zombie_villager`)  · D S T X
- **Dove (biomi)**: quasi tutto l'Overworld (55/57; manca: Deep Dark, Mushroom Fields)
- **Strutture**: Igloo (piazzato); Jungle Temple (DnT) (spawn naturale); Philips' Ruins (piazzato); Stronghold (DnT) (piazzato, spawn naturale); Villaggi abbandonati (ISO) (piazzato)
- ISO Villagers: unica fonte di villager: si cura con Weakness + Golden Carrot (tag `#insanesurvivaloverhaul:zombie_villager_cure_items`, la durata della cura è quella vanilla), poi convalescenza di un giorno (non commercia, rallentato)
- ISO `Fire resistant structure zombie villagers`: quelli piazzati dalle strutture hanno Fire Resistance infinita, così non bruciano prima di essere trovati
- ISO `No nitwits`: i nitwit curati diventano disoccupati e possono prendere un lavoro
- ISO `Zombie siege`: assedio di zombie anche lontano dai villaggi
- EAI Biting mobs: morde se colpito senza un'arma
- EAI Climbing: sale le scale a pioli
- EAI Fisher mobs: a volte ha una canna da pesca e ti tira a sé
- EAI Jump: salta sul posto se sei poco più in alto
- EAI Leaders: alcuni sono leader e chiamano rinforzi
- EAI Lunge at target: si ferma un attimo e poi si lancia contro il bersaglio
- EAI MPR `overworld_zombies_equipment`: armatura (anche rame) e armi/attrezzi, più spesso con la luna piena, alla luce del cielo e in profondità
- EAI MPR `zombies`, `scale/zombies`: più piccoli a caso; nelle grotte dell'Overworld alcuni sono minatori (più in profondità, più spesso)
- EAI Pearler mobs: a volte ha Ender Pearl e le lancia per raggiungerti
- EAI Pick up and throw: a volte raccoglie altri mob e te li lancia
- EAI Riding: a volte cavalca altri mob
- EAI Sprint: a volte corre vicino al bersaglio
- Enhanced AI (MPR `fuck_baby_zombies`): niente Zombie bambini: tutti spawnano adulti (vale per tutto `#minecraft:zombies`)
- **OFF**: Shielding (`Chance to equip` 0); Miner mobs da config (`Miner chance` 0); per gli zombie lo attiva MPR (vedi sotto); Parkour (feature spenta)

### Zombified Piglin (`minecraft:zombified_piglin`)  · D S T X
- **Dove (biomi)**: Nether: Crimson Forest, Nether Wastes
- **Strutture**: Fortezza del Nether (DnT) (piazzato, spawn naturale); Incendium (piazzato); Moog's Nether Structures (piazzato, spawn naturale)
- EAI Biting mobs: morde se colpito senza un'arma
- EAI Climbing: sale le scale a pioli
- EAI Jump: salta sul posto se sei poco più in alto
- EAI Lunge at target: si ferma un attimo e poi si lancia contro il bersaglio
- EAI MPR `zombies`, `scale/zombies`: più piccoli a caso; nelle grotte dell'Overworld alcuni sono minatori (più in profondità, più spesso)
- EAI Pick up and throw: a volte raccoglie altri mob e te li lancia
- EAI Riding: a volte cavalca altri mob
- EAI Sprint: a volte corre vicino al bersaglio
- Enhanced AI (MPR `fuck_baby_zombies`): niente Zombie bambini: tutti spawnano adulti (vale per tutto `#minecraft:zombies`)
- Enhanced AI `Break anger`: OFF: da disattivare (decisione 2026-11-26; il config usava `#forge:ores/quartz`, inesistente): non va nella pagina
- **OFF**: Shielding (`Chance to equip` 0); Miner mobs da config (`Miner chance` 0); per gli zombie lo attiva MPR (vedi sotto); Parkour (feature spenta)

## Vanilla Backport

### Camel Husk (`minecraft:camel_husk`)
- **Dove (biomi)**: —
- **Altre fonti**: ?Vanilla Backport: deserti (codice)
- Vanilla Backport `has_camel_husks`: ?deserti di notte con Husk e Parched in sella
- **Cibo (tag)**: `minecraft:camel_husk_food` = rabbit_foot (ultimo: VanillaBackport)

### Copper Golem (`minecraft:copper_golem`)
- **Dove (biomi)**: —
- **Altre fonti**: si costruisce
- Vanilla Backport `has_copper_golems`: si costruisce con Blocco di Rame + Carved Pumpkin; sposta oggetti dalle Copper Chest; si ossida nel tempo

### Creaking (`minecraft:creaking`)
- **Dove (biomi)**: —
- **Altre fonti**: dai Creaking Heart nel Pale Garden, di notte
- Vanilla Backport `creaking`: nasce di notte dal Creaking Heart nel Pale Garden; non si ferma il giorno (`do_creaking_hearts_work_on_day` = false)

### Happy Ghast (`minecraft:happy_ghast`)
- **Dove (biomi)**: —
- **Altre fonti**: da un Dried Ghast (fossili del Nether, baratto) messo in acqua -> Ghastling
- Vanilla Backport + Bits and Balance `speedyHappyGhasts`: cavalcabile con Harness; risente di Speed/Slowness
- **Cibo (tag)**: `minecraft:happy_ghast_food` = snowball (ultimo: VanillaBackport) · `minecraft:happy_ghast_tempt_items` = black_harness, blue_harness, brown_harness, cyan_harness, gray_harness, green_harness, light_blue_harness, light_gray_harness, lime_harness, magenta_harness ... (ultimo: VanillaBackport)

### Nautilus (`minecraft:nautilus`)
- **Dove (biomi)**: —
- **Altre fonti**: oceani: raro in quelli freddi e ghiacciati, più frequente in quelli normali, tiepidi e caldi (`spawns_nautilus*`)
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- Vanilla Backport `has_nautilus`: cavalcabile sott'acqua, armatura da Nautilus nei loot
- **Cibo (tag)**: `minecraft:nautilus_food` = cod, cod_bucket, cooked_cod, cooked_salmon, pufferfish, pufferfish_bucket, salmon, salmon_bucket, tropical_fish, tropical_fish_bucket ... (ultimo: VanillaBackport)

### Parched (`minecraft:parched`)  · D S T X
- **Dove (biomi)**: —
- **Altre fonti**: ?Vanilla Backport: deserti (codice)
- EAI Climbing: sale le scale a pioli
- EAI Leaders: alcuni sono leader e chiamano rinforzi
- EAI MPR `overworld_skeletons`: armatura (più spesso con la luna piena e in profondità), meno preciso
- EAI MPR `scale/skeletons`: più piccoli a caso
- EAI Riding: a volte cavalca altri mob
- EAI Skeleton flee target: si allontana se ti avvicini
- EAI Skeleton shoot: tira più lontano, più spesso e si sposta di lato
- Bits and Balance `tippedArrowLingeringClouds.mobsEnabled`: le sue frecce con effetto lasciano una nuvola dell'effetto dove atterrano (vale per tutte le frecce con effetto, anche dei giocatori: va sulla pagina della Tipped Arrow, qui solo un accenno)
- Vanilla Backport `has_parched_skeletons`: ?spawna nei deserti (codice, non nei JSON dei biomi)
- **OFF**: Shielding (`Chance to equip` 0); Parkour (feature spenta)

### Sulfur Cube (`minecraft:sulfur_cube`)
- **Dove (biomi)**: —
- **Altre fonti**: Sulfur Caves (Vanilla Backport)
- Vanilla Backport `has_sulfur_cubes`: spawna nelle Sulfur Caves; archetipi esplosivi e dannosi attivi; si mette nel secchio
- **Cibo (tag)**: `minecraft:sulfur_cube_food` = slime_ball (ultimo: VanillaBackport)

### Zombie Nautilus (`minecraft:zombie_nautilus`)
- **Dove (biomi)**: —
- **Altre fonti**: con i Drowned negli oceani (metà dei Drowned ne cavalca uno); variante corallo negli Warm Ocean
- Vanilla Backport `has_nautilus`: cavalcabile sott'acqua, armatura da Nautilus nei loot

## Naturalist

Il comportamento proprio di Naturalist (cosa mangiano, chi cacciano, abitudini) lo ricavo dal codice della mod in fase di scrittura. Modifiche del pack: esclusi da `enhancedai:speed_bonus` (quindi niente sigla S), carne ridotta (drop esclusi dalle pagine), cibi crudi in `raw_foods`.

### Alligator (`naturalist:alligator`)  · D
- **Dove (biomi)**: Overworld: Mangrove Swamp, River, Swamp
- ISO Aging: vita lunga
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `naturalist:alligator_food_items` = beef, chicken, porkchop, rabbit (ultimo: naturalist)

### Anglerfish (`naturalist:anglerfish`)  · D
- **Dove (biomi)**: Overworld: Cold Ocean, Deep Cold Ocean, Deep Lukewarm Ocean, Deep Ocean, Lukewarm Ocean, Ocean, Warm Ocean
- EAI MPR `scale/sea_creatures`: dimensioni casuali

### Ant (`naturalist:ant`)  · D
- **Dove (biomi)**: —
- **Altre fonti**: dagli Ant Hill (`add_ant_hills`)

### Bass (`naturalist:bass`)  · D
- **Dove (biomi)**: Overworld: Frozen River, Mangrove Swamp, River, Swamp
- EAI MPR `scale/sea_creatures`: dimensioni casuali

### Bear (`naturalist:bear`)  · D
- **Dove (biomi)**: Overworld: Birch Forest, Dappled Forest, Dark Forest, Flower Forest, Forest, Grove, Old Growth Birch Forest, Old Growth Pine Taiga, Old Growth Spruce Taiga, Pale Garden, Snowy Taiga, Taiga
- ISO Aging: vita lunga
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `naturalist:bear_tempt_items` = alexsmobs:cooked_moose_ribs, alexsmobs:raw_moose_ribs, cooked_salmon, honeycomb, salmon, sweet_berries, naturalist:venison (ultimo: naturalist) · `survivalreimagined:bear_food` = alexsmobs:cooked_moose_ribs, alexsmobs:raw_moose_ribs, cooked_salmon, honeycomb, salmon, sweet_berries, naturalist:venison (ultimo: datapack)

### Bird (`naturalist:bird`)  · D
- **Dove (biomi)**: Overworld: Badlands, Beach, Birch Forest, Cherry Grove, Dappled Forest, Dark Forest, Desert, Eroded Badlands, Flower Forest, Forest, Frozen Peaks, Grove, Ice Spikes, Jagged Peaks, Mangrove Swamp, Meadow, Old Growth Birch Forest, Old Growth Pine Taiga, Old Growth Spruce Taiga, Pale Garden, Plains, Savanna, Savanna Plateau, Snowy Beach, Snowy Plains, Snowy Slopes, Snowy Taiga, Stony Peaks, Sunflower Plains, Swamp, Taiga, Windswept Forest, Windswept Gravelly Hills, Windswept Hills, Windswept Savanna, Wooded Badlands
- **Cibo (tag)**: `naturalist:bird_food_items` = beetroot_seeds, melon_seeds, pumpkin_seeds, wheat_seeds (ultimo: naturalist)

### Black Bear (`naturalist:black_bear`)  · D
- **Dove (biomi)**: Overworld: Birch Forest, Dappled Forest, Dark Forest, Flower Forest, Forest, Grove, Old Growth Birch Forest, Old Growth Pine Taiga, Old Growth Spruce Taiga, Pale Garden, Snowy Taiga, Taiga
- ISO Aging: vita lunga
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `survivalreimagined:black_bear_food` = alexsmobs:cooked_moose_ribs, alexsmobs:raw_moose_ribs, cooked_salmon, honeycomb, salmon, sweet_berries, naturalist:venison (ultimo: datapack)

### Blobfish (`naturalist:blobfish`)  · D
- **Dove (biomi)**: Overworld: Cold Ocean, Deep Cold Ocean, Deep Lukewarm Ocean, Deep Ocean, Lukewarm Ocean, Ocean, Warm Ocean
- EAI MPR `scale/sea_creatures`: dimensioni casuali

### Boar (`naturalist:boar`)  · D
- **Dove (biomi)**: Overworld: Birch Forest, Dappled Forest, Dark Forest, Flower Forest, Forest, Grove, Old Growth Birch Forest, Pale Garden, Savanna, Savanna Plateau, Windswept Savanna
- ISO Aging: vita media
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `naturalist:boar_food_items` = beetroot, carrot, potato (ultimo: naturalist)

### Butterfly (`naturalist:butterfly`)  · D
- **Dove (biomi)**: Overworld: Birch Forest, Dappled Forest, Dark Forest, Flower Forest, Forest, Mangrove Swamp, Old Growth Birch Forest, Pale Garden, Plains, Sunflower Plains, Swamp
- ISO Aging: vita molto breve
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- Supplementaries Cage: catturabile in gabbia
- Supplementaries Jar: catturabile in un barattolo
- **Cibo (tag)**: `survivalreimagined:butterfly_food` = ecologics:azalea_flower, insanesurvivaloverhaul:cyan_flower, allium, azure_bluet, blue_orchid, cactus_flower, cherry_leaves, chorus_flower, closed_eyeblossom, cornflower ... (ultimo: datapack)

### Capybara (`naturalist:capybara`)  · A D
- **Dove (biomi)**: Overworld: Bamboo Jungle, Jungle, Mangrove Swamp, Sparse Jungle, Swamp
- ISO Aging: vita media
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `naturalist:capybara_food_items` = melon_slice (ultimo: naturalist)

### Caterpillar (`naturalist:caterpillar`)  · D
- **Dove (biomi)**: —
- **Altre fonti**: dalle Butterfly innamorate, poi diventa Chrysalis su un tronco
- Supplementaries Cage: catturabile in gabbia
- Supplementaries Jar: catturabile in un barattolo

### Catfish (`naturalist:catfish`)  · D
- **Dove (biomi)**: Overworld: Mangrove Swamp, Swamp
- EAI MPR `scale/sea_creatures`: dimensioni casuali

### Clam (`naturalist:clam`)  · D
- **Dove (biomi)**: Overworld: Cold Ocean, Deep Cold Ocean, Deep Lukewarm Ocean, Deep Ocean, Lukewarm Ocean, Ocean, Warm Ocean

### Crab (`naturalist:crab`)  · D
- **Dove (biomi)**: Overworld: Beach, Stony Shore
- ISO Aging: vita breve
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `naturalist:crab_food` = tropical_fish (ultimo: naturalist) · `quark:crab_tempt_items` = chicken, cod, cooked_cod, cooked_salmon, pufferfish, salmon, tropical_fish, wheat, naturalist:anglerfish, naturalist:bass ... (ultimo: Quark)

### Deer (`naturalist:deer`)  · A D
- **Dove (biomi)**: Overworld: Birch Forest, Cherry Grove, Dappled Forest, Dark Forest, Flower Forest, Forest, Grove, Old Growth Birch Forest, Pale Garden
- ISO Aging: vita media
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `survivalreimagined:deer_food` = apple (ultimo: datapack)

### Desert Scorpion (`naturalist:desert_scorpion`)  · D
- **Dove (biomi)**: Overworld: Badlands, Desert, Eroded Badlands, Wooded Badlands

### Dragonfly (`naturalist:dragonfly`)  · D
- **Dove (biomi)**: Overworld: Mangrove Swamp, Swamp

### Duck (`naturalist:duck`)  · A D
- **Dove (biomi)**: Overworld: Frozen River, Mangrove Swamp, River, Swamp
- ISO Aging: vita breve
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- EAI MPR `small_animals`: attacco più debole
- **Cibo (tag)**: `naturalist:duck_food_items` = cod, pufferfish, salmon, tropical_fish, naturalist:anglerfish, naturalist:bass, naturalist:blobfish, naturalist:catfish, naturalist:piranha (ultimo: naturalist)

### Elephant (`naturalist:elephant`)  · D
- **Dove (biomi)**: Overworld: Savanna, Savanna Plateau, Windswept Savanna
- ISO Aging: vita molto lunga
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `survivalreimagined:elephant_food` = melon_slice (ultimo: datapack)

### Firefly (`naturalist:firefly`)  · D
- **Dove (biomi)**: Overworld: Birch Forest, Dappled Forest, Dark Forest, Flower Forest, Forest, Glimmering Weald, Mangrove Swamp, Mushroom Fields, Old Growth Birch Forest, Pale Garden, Plains, Sunflower Plains, Swamp
- Supplementaries Cage: catturabile in gabbia
- Supplementaries Jar: catturabile in un barattolo

### Giant Isopod (`naturalist:giant_isopod`)  · A D
- **Dove (biomi)**: Overworld: Cold Ocean, Deep Cold Ocean, Deep Lukewarm Ocean, Deep Ocean, Lukewarm Ocean, Ocean, Warm Ocean
- ISO Aging: vita breve
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `naturalist:giant_isopod_food` = cod, cooked_cod, cooked_salmon, salmon, tropical_fish, naturalist:bass, naturalist:catfish, naturalist:cooked_bass, naturalist:cooked_catfish (ultimo: naturalist)

### Giraffe (`naturalist:giraffe`)  · A D
- **Dove (biomi)**: Overworld: Savanna, Savanna Plateau, Windswept Savanna
- ISO Aging: vita lunga
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `naturalist:giraffe_food_items` = apple, golden_apple, hay_block (ultimo: naturalist)

### Great White Shark (`naturalist:great_white_shark`)  · D
- **Dove (biomi)**: Overworld: Deep Lukewarm Ocean, Lukewarm Ocean, Warm Ocean
- **Cibo (tag)**: `naturalist:great_white_shark_food_items` = cod, cooked_cod, cooked_salmon, salmon, tropical_fish, naturalist:bass, naturalist:catfish, naturalist:cooked_bass, naturalist:cooked_catfish (ultimo: naturalist)

### Hedgehog (`naturalist:hedgehog`)  · D
- **Dove (biomi)**: Overworld: Flower Forest, Forest, Meadow, Plains, Sunflower Plains, Taiga
- ISO Aging: vita breve
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `naturalist:hedgehog_food_items` = glow_berries, sweet_berries (ultimo: naturalist)

### Hippo (`naturalist:hippo`)  · D
- **Dove (biomi)**: Overworld: Bamboo Jungle, Jungle, Savanna, Savanna Plateau, Sparse Jungle, Windswept Savanna
- ISO Aging: vita lunga
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `survivalreimagined:hippo_food` = melon (ultimo: datapack)

### Jellyfish (`naturalist:jellyfish`)  · D
- **Dove (biomi)**: Overworld: Cold Ocean, Deep Cold Ocean, Deep Lukewarm Ocean, Deep Ocean, Lukewarm Ocean, Ocean, Warm Ocean
- EAI MPR `scale/sea_creatures`: dimensioni casuali

### Jungle Scorpion (`naturalist:jungle_scorpion`)  · D
- **Dove (biomi)**: Overworld: Bamboo Jungle, Jungle, Sparse Jungle

### Komodo Dragon (`naturalist:komodo_dragon`)  · D
- **Dove (biomi)**: Overworld: Badlands, Desert, Eroded Badlands, Jungle, Savanna, Savanna Plateau, Sparse Jungle, Windswept Savanna, Wooded Badlands
- ISO Aging: vita lunga
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `naturalist:komodo_dragon_food_items` = ecologics:crab_meat, beef, chicken, cooked_beef, cooked_chicken, cooked_mutton, cooked_porkchop, cooked_rabbit, mutton, porkchop ... (ultimo: naturalist)

### Lion (`naturalist:lion`)  · D
- **Dove (biomi)**: Overworld: Savanna, Savanna Plateau, Windswept Savanna
- ISO Aging: vita lunga
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `naturalist:lion_food_items` = ecologics:crab_meat, beef, chicken, cooked_beef, cooked_chicken, cooked_mutton, cooked_porkchop, cooked_rabbit, mutton, porkchop ... (ultimo: naturalist)

### Lizard (`naturalist:lizard`)  · D
- **Dove (biomi)**: Overworld: Bamboo Jungle, Birch Forest, Dappled Forest, Dark Forest, Desert, Flower Forest, Forest, Jungle, Mangrove Swamp, Old Growth Birch Forest, Pale Garden, Savanna, Savanna Plateau, Sparse Jungle, Swamp, Windswept Savanna
- **Cibo (tag)**: `naturalist:lizard_tempt_items` = spider_eye (ultimo: naturalist) · `survivalreimagined:lizard_food` = spider_eye (ultimo: datapack)

### Mammoth (`naturalist:mammoth`)  · D
- **Dove (biomi)**: Overworld: Frozen Peaks, Ice Spikes, Snowy Plains, Snowy Slopes
- ISO Aging: vita molto lunga
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `survivalreimagined:mammoth_food` = melon_slice (ultimo: datapack)

### Mole (`naturalist:mole`)  · D
- **Dove (biomi)**: Overworld: Birch Forest, Dappled Forest, Dark Forest, Flower Forest, Forest, Meadow, Old Growth Birch Forest, Pale Garden, Plains, Sunflower Plains

### Ostrich (`naturalist:ostrich`)  · D
- **Dove (biomi)**: Overworld: Savanna, Savanna Plateau, Windswept Savanna
- ISO Aging: vita media
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `naturalist:ostrich_food_items` = beetroot_seeds, melon_seeds, pitcher_pod, pumpkin_seeds, torchflower_seeds, wheat_seeds (ultimo: naturalist)

### Piranha (`naturalist:piranha`)  · D
- **Dove (biomi)**: Overworld: Bamboo Jungle, Jungle, Lush Caves, Sparse Jungle
- EAI MPR `scale/sea_creatures`: dimensioni casuali

### Rat (`naturalist:rat`)  · A D
- **Dove (biomi)**: Overworld: Birch Forest, Dappled Forest, Dark Forest, Flower Forest, Forest, Grove, Old Growth Birch Forest, Pale Garden, Plains, Sunflower Plains
- ISO Aging: vita breve
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `naturalist:rat_food` = bread (ultimo: naturalist)

### Ray (`naturalist:ray`)  · D
- **Dove (biomi)**: Overworld: Cold Ocean, Deep Cold Ocean, Deep Lukewarm Ocean, Deep Ocean, Lukewarm Ocean, Ocean, Warm Ocean
- EAI MPR `scale/sea_creatures`: dimensioni casuali

### Rhino (`naturalist:rhino`)  · D
- **Dove (biomi)**: Overworld: Savanna, Savanna Plateau, Windswept Savanna

### Snail (`naturalist:snail`)  · D
- **Dove (biomi)**: Overworld: Birch Forest, Cherry Grove, Dappled Forest, Dark Forest, Deep Dark, Dripstone Caves, Flower Forest, Forest, Frozen River, Glimmering Weald, Lush Caves, Mangrove Swamp, Meadow, Mushroom Fields, Old Growth Birch Forest, Pale Garden, Plains, River, Savanna, Savanna Plateau, Stony Peaks, Sulfur Caves, Sunflower Plains, Swamp, Windswept Forest, Windswept Gravelly Hills, Windswept Hills, Windswept Savanna
- ISO Aging: vita breve
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- Supplementaries Cage: catturabile in gabbia
- Supplementaries Jar: catturabile in un barattolo
- **Cibo (tag)**: `survivalreimagined:snail_food` = beetroot (ultimo: datapack)

### Snake (`naturalist:snake`)  · D
- **Dove (biomi)**: Overworld: Badlands, Bamboo Jungle, Beach, Birch Forest, Dappled Forest, Dark Forest, Desert, Eroded Badlands, Flower Forest, Forest, Frozen River, Jungle, Mangrove Swamp, Old Growth Birch Forest, Pale Garden, Plains, River, Savanna, Savanna Plateau, Sparse Jungle, Stony Shore, Sunflower Plains, Swamp, Windswept Savanna, Wooded Badlands
- **Cibo (tag)**: `naturalist:snake_tempt_items` = chicken, egg, rabbit, rabbit_foot (ultimo: naturalist) · `survivalreimagined:snake_food` = chicken, cooked_rabbit, egg, rabbit, rabbit_foot, spider_eye (ultimo: datapack)

### Starfish (`naturalist:starfish`)  · D
- **Dove (biomi)**: Overworld: Cold Ocean, Deep Cold Ocean, Deep Lukewarm Ocean, Deep Ocean, Lukewarm Ocean, Ocean, Warm Ocean

### Tiger (`naturalist:tiger`)  · D
- **Dove (biomi)**: Overworld: Badlands, Bamboo Jungle, Cherry Grove, Dark Forest, Desert, Eroded Badlands, Frozen Peaks, Grove, Jagged Peaks, Jungle, Mangrove Swamp, Meadow, Snowy Plains, Snowy Slopes, Sparse Jungle, Stony Peaks, Swamp, Wooded Badlands
- ISO Aging: vita lunga
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `naturalist:tiger_food_items` = ecologics:crab_meat, beef, chicken, cooked_beef, cooked_chicken, cooked_mutton, cooked_porkchop, cooked_rabbit, mutton, porkchop ... (ultimo: naturalist)

### Tortoise (`naturalist:tortoise`)  · D
- **Dove (biomi)**: Overworld: Bamboo Jungle, Desert, Jungle, Mangrove Swamp, Sparse Jungle, Swamp
- ISO Aging: vita lunga
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `naturalist:tortoise_tempt_items` = bamboo, brown_mushroom, cactus, dandelion (ultimo: naturalist) · `survivalreimagined:tortoise_food` = bamboo, brown_mushroom, cactus, dandelion (ultimo: datapack)

### Turkey (`naturalist:turkey`)  · A D
- **Dove (biomi)**: Overworld: Flower Forest, Forest, Grove, Old Growth Pine Taiga, Old Growth Spruce Taiga, Taiga
- ISO Aging: vita breve
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- EAI MPR `small_animals`: attacco più debole
- **Cibo (tag)**: `naturalist:turkey_food_items` = beetroot_seeds, melon_seeds, pitcher_pod, pumpkin_seeds, torchflower_seeds, wheat_seeds (ultimo: naturalist)

### Vulture (`naturalist:vulture`)  · D
- **Dove (biomi)**: Overworld: Badlands, Desert, Eroded Badlands, Savanna, Savanna Plateau, Windswept Savanna, Wooded Badlands
- Supplementaries Cage: catturabile in gabbia

### Whale (`naturalist:whale`)  · D
- **Dove (biomi)**: Overworld: Cold Ocean, Deep Cold Ocean, Deep Lukewarm Ocean, Deep Ocean, Lukewarm Ocean, Ocean, Warm Ocean
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- **Cibo (tag)**: `survivalreimagined:whale_food` = cod, cooked_cod, cooked_salmon, salmon, naturalist:cooked_crab_meat, naturalist:crab_meat (ultimo: datapack)

### Zebra (`naturalist:zebra`)  · A D
- **Dove (biomi)**: Overworld: Savanna, Savanna Plateau, Windswept Savanna
- ISO Aging: vita molto lunga
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- Supplementaries Flute: richiamabile con il Flauto
- Supplementaries Fodder: mangia il Fodder
- **Cibo (tag)**: `survivalreimagined:zebra_food` = apple, enchanted_golden_apple, golden_apple, hay_block, sugar, wheat, supplementaries:flax, supplementaries:flax_block, supplementaries:sugar_cube (ultimo: datapack)

## Ecologics

### Coconut Crab (`ecologics:coconut_crab`)  · D S
- **Dove (biomi)**: —
- **Altre fonti**: esce dal 20% dei Cocchi che si rompono cadendo dalle palme (spiagge)
- ISO Aging: vita breve
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- Ecologics: ?esce dal Cocco che cade dalle palme
- Supplementaries Cage: catturabile in gabbia
- **Cibo (tag)**: `ecologics:coconut_crab_tempt_items` = ecologics:coconut_slice, ecologics:cooked_prickly_pear, ecologics:prickly_pear, ecologics:walnut, apple, chorus_fruit, enchanted_golden_apple, golden_apple, melon_slice, naturalist:cooked_crab_meat (ultimo: datapack(replace))

### Penguin (`ecologics:penguin`)  · A D S
- **Dove (biomi)**: Overworld: Frozen Ocean, Frozen River, Snowy Plains
- ISO Aging: vita media
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- EAI MPR `small_animals`: attacco più debole
- Supplementaries Cage: catturabile in gabbia
- **Cibo (tag)**: `ecologics:penguin_tempt_items` = cod, salmon, tropical_fish (ultimo: Ecologics)

### Squirrel (`ecologics:squirrel`)  · A D S
- **Dove (biomi)**: Overworld: Plains
- ISO Aging: vita breve
- ISO Breeding: riproduzione più lenta, può fallire, gemelli
- ISO Breeding + Well fed: non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato
- Ecologics: spawna nelle Plains (biome modifier `ecologics:spawn_squirrel`)
- Supplementaries Cage: catturabile in gabbia da cucciolo
- **Cibo (tag)**: `ecologics:squirrel_tempt_items` = ecologics:walnut (ultimo: Ecologics)

## Supplementaries

### Red Merchant (`supplementaries:red_merchant`)
- **Dove (biomi)**: —
- **Altre fonti**: ?con il Wandering Trader
- Supplementaries + datapack: spawna con il Wandering Trader; trade sovrascritti nel datapack (1 Smeraldo, pochi usi)

### Plunderer (`supplementaries:plunderer`)
- **Dove (biomi)**: —
- **Altre fonti**: nei raid vicino all'acqua, al timone delle barche dei Pillager (Galleon spenti)
- ISO Misc mobs `Passive regen chance`: si cura lentamente da solo
- Supplementaries `naval_raid_chance` 0.75: nei raid parte dei Pillager arriva in barca dal mare, guidata da un Plunderer; Galleon spenti
