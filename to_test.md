# Da testare: ISO 5.16.0.0-beta (overhaul dei villager) ed Enhanced AI 4.3.1.0

Meglio in un **mondo nuovo**: villaggi, magioni, minerale di smeraldo e la disattivazione di pollai e case del Carpenter valgono solo per i chunk nuovi.

Comandi di base: `/gamemode creative`, `/effect give @s minecraft:night_vision infinite 0 true`, `/time set day`, F3+H per vedere durabilità e ID negli oggetti. Nei comandi sotto `@e[type=minecraft:villager,sort=nearest,limit=1]` è il villager più vicino.

## Prima di tutto
- [x] `/datapack list`: `survivalreimagined` deve stare **sopra** (edit: in realtà nella lista deve stare sotto a tutto, cio' vuol dire che viene caricata per ultima e sostituisce quello che é già stato caricato, se non ricordo male)`insanesurvivaloverhaul:villagers_overhaul`. Se è sotto, gli override del Librarian (rune) e dello scudo del Weaponsmith non funzionano
- [x] Log senza errori su `survivalreimagined`, sui remolder di Incubation (`incubation/remolders`) e sugli scambi Moonlight del Red Merchant
- [ ] `/insanesurvivaloverhaul villager_trades dump`, poi controllare `logs/insanesurvivaloverhaul/villager_trades_<data>/`:
  - [ ] nessuno scambio di Vanilla Backport, Supplementaries (globo, lino, mappe dell'avventuriero, ash bricks), Ecologics o Quark sopravvissuto. Per vedere solo gli scambi registrati dalle mod: `/insanesurvivaloverhaul villager_trades dump all modded`
  - [ ] ci sono le aggiunte del pack: Mason (limestone, jasper, shale liv. 2, myalite liv. 4), Leatherworker (tronchi modded liv. 2-3), Butcher (carni Naturalist liv. 2-4), Farmer (uova liv. 3), Weaponsmith (scudi Shields+)
  - [ ] il Carpenter ha solo gli scambi nuovi (bastoni, scale, armor stand, chest, scaffolding, barrel, pistone, daylight detector, ascia di diamante): `/insanesurvivaloverhaul villager_trades dump sawmill:carpenter`

## Strutture
- [x] Villaggio: `/locate structure minecraft:village_plains` (o `/place structure minecraft:village_plains ~ ~ ~`). Abbandonato, solo zombie villager (resistenti al fuoco), niente golem, animali, letti, campane o job site. **Niente casa del Carpenter (Sawmill) né pollai (Incubation)**
- [x] Loot del villaggio: casse povere, il grosso nella ghiaia e sabbia sospette sotto i pavimenti
- [x] Avamposto: `/locate structure minecraft:pillager_outpost` (o `/place structure minecraft:pillager_outpost ~ ~ ~`). Guarnigione con capitano; dopo averli uccisi, allontanarsi e tornare dopo `/time add 24000`: i pillager **non rispawnano**
- [ ] Magione: ora è l'Illager Manor di DnT. `/locate structure nova_structures:illager_manor` (o `/place structure nova_structures:illager_manor ~ ~ ~`; il locate cerca fino a ~100 chunk e le magioni sono rade: se fallisce, teletrasportarsi di qualche migliaio di blocchi e riprovare). Log senza errori sui pool `illager_mansion`. Illager, golem e allay in gabbia
  - [ ] I pochi villager del manor sono disoccupati e senza scambi: dandogli un job site prendono gli scambi di ISO (niente scambi vanilla)
  - [ ] Le casse `map_chest`, `secret_room` e `library_chest` hanno le versioni di Woodland Mansion Replacement: nessuna mappa verso strutture della mod DnT completa, che non è nel pack
  - [ ] `/locate structure minecraft:mansion` e la mappa della magione del Wandering Trader portano allo stesso punto del manor
  - [ ] Le casse dei giardini che usavano loot della mod DnT completa (`nova_structures:chests/dungeon_6`, `dungeon_7`, `undead_crypts_grave`) non sono vuote
- [ ] Stronghold di DnT: la cella prigione con 2 villager (in 1 cella su 8) torna a generarsi; i villager sono disoccupati e, con un job site, prendono gli scambi di ISO. `/locate structure minecraft:stronghold`
- [ ] Ponte infestato di Abridged (ora disattivato): per capire se i suoi pillager rispawnano, togliere temporaneamente `datapacks/survivalreimagined/data/abridged/tags/worldgen/biome/has_bridge/pillager_infested.json`, riavviare e cercare con `/locate structure abridged:bridge` in chunk nuovi (trova anche i ponti normali)

## Villager
Per gli scambi conviene evocare villager già con lavoro e livello (`NoAI` li tiene fermi, ma senza AI non lavorano né fanno restock):
```
/give @s minecraft:emerald 64
/summon minecraft:villager ~ ~ ~ {NoAI:1b,VillagerData:{profession:"minecraft:librarian",level:2,type:"minecraft:plains"}}
```
Un villager evocato a livello N ha solo i 2 scambi casuali del livello N: per vedere gli altri, ucciderlo (`/kill @e[type=minecraft:villager,sort=nearest,limit=1]`) ed evocarne un altro. Il dump resta il controllo completo.

- [x] Cura di uno zombie villager con Debolezza e una **Golden Carrot**, la Golden Apple non deve funzionare:
  ```
  /summon minecraft:zombie_villager ~ ~ ~ {PersistenceRequired:1b,VillagerData:{profession:"minecraft:nitwit",level:1,type:"minecraft:plains"}}
  /effect give @e[type=minecraft:zombie_villager,sort=nearest,limit=1] minecraft:weakness 120
  /effect give @e[type=minecraft:zombie_villager,sort=nearest,limit=1] minecraft:fire_resistance infinite
  /give @s minecraft:golden_carrot 2
  /give @s minecraft:golden_apple 2
  ```
  Dopo aver usato la carota, per accelerare: `/data merge entity @e[type=minecraft:zombie_villager,sort=nearest,limit=1] {ConversionTime:40}`
- [x] Il villager curato ha Convalescenza per un giorno: non scambia, non lavora, è rallentato. Per saltarla: `/effect clear @e[type=minecraft:villager,sort=nearest,limit=1] insanesurvivaloverhaul:convalescence`
- [x] Un nitwit curato (quello sopra) diventa disoccupato e prende un lavoro piazzando un job site vicino (es. `/give @s minecraft:lectern`)
- [x] I villager non si riproducono: due villager senza `NoAI`, qualche letto e `/give @s minecraft:bread 32` da lanciargli
- [x] Il villager tiene lavoro e scambi anche se perde il job site: rompere il job site dopo che l'ha preso
- [x] Librarian liv. 2-4 (`profession:"minecraft:librarian"`, `level:2`/`3`/`4`): vende **una runa casuale per 1 smeraldo, 1 volta per restock**, mai una curse. Il restock va provato con un Librarian senza `NoAI` vicino al suo leggio (`/time add 12000`)
- [x] Weaponsmith (`profession:"minecraft:weaponsmith"`): Copper Shield (liv. 1, +27 pepite di rame), Iron Shield (liv. 2, +27 pepite di ferro), Golden Shield (liv. 3, +27 pepite d'oro), Diamond Shield (liv. 5, +3 diamanti). Niente scudo vanilla
  ```
  /give @s insanesurvivaloverhaul:copper_nugget 27
  /give @s minecraft:iron_nugget 27
  /give @s minecraft:gold_nugget 27
  /give @s minecraft:diamond 3
  ```
- [x] Mason (liv. 2 e 4), Leatherworker (liv. 2 e 3), Butcher (liv. 2, 3 e 4), Farmer (liv. 3): le aggiunte del pack compaiono tra gli scambi possibili
- [x] Un villager vicino a una Sawmill diventa Carpenter e ha gli scambi nuovi. Evocato: `/summon minecraft:villager ~ ~ ~ {NoAI:1b,VillagerData:{profession:"sawmill:carpenter",level:4,type:"minecraft:plains"}}`
- [x] Local Flavours: il primo scambio compra un piatto complesso (anche Tropical Stew o Maple Cream Pie): `/give @s ecologics:tropical_stew`, `/give @s ecologics:maple_pie`
- [x] I prezzi salgono colpendo i villager e non scendono sotto il prezzo base, nemmeno con Hero of the Village (`/effect give @s minecraft:hero_of_the_village 600 0`)
- [x] Hero of the Village: i villager (senza `NoAI`, di giorno) regalano un oggetto che vendono. Il Librarian non deve regalare libri incantati, ma rune (conversione di RuneEnchanting)
- [x] Quark: tenendo uno (blocco di*) smeraldo i villager ti seguono

## Smeraldi
- [x] Non si trasformano più in rune, nel loot di nessun tipo: `/loot give @s loot minecraft:chests/jungle_temple` e `/loot give @s loot minecraft:chests/desert_pyramid` più volte
- [x] Minerale di smeraldo raro in tutto l'overworld, più frequente in montagna: `/insanesurvivaloverhaul count_ores_in_chunk` in qualche chunk di pianura e di montagna
- [ ] (ISO 5.16.1.0) Lo smeraldo extra ora genera tra y -32 e 32, 2 vene per chunk, e non più sospeso in aria fuori dalle montagne (solo chunk nuovi)
- [x] Pillager uccisi dal giocatore: 0-1 smeraldo (di più con Looting). Senza ucciderlo ogni volta: `/summon minecraft:pillager ~ ~ ~ {NoAI:1b}` e poi `/loot give @s kill @e[type=minecraft:pillager,sort=nearest,limit=1]` ripetuto (se gli smeraldi non escono così, ucciderli davvero: potrebbero non venire dalla loot table)
- [x] Pesca in mare aperto: raramente uno smeraldo
- [ ] Gli advancement con ricompensa XP danno 1 smeraldo ogni 25 XP: `/advancement grant @s only minecraft:adventure/kill_all_mobs` (100 XP, quindi 4 smeraldi), per ripetere `/advancement revoke @s only minecraft:adventure/kill_all_mobs`

## Wandering Trader e Red Merchant
- [x] Il Wandering Trader torna a spawnare da solo. Scambi: `/summon minecraft:wandering_trader`, compra 2 oggetti, vende 6 piante e blocchi di altri biomi e 2 mappe
- [x] Red Merchant (spawna con il Wandering Trader, evocabile con `/summon supplementaries:red_merchant`), 10 scambi:
  - bomba: 1 smeraldo + 3 lingotti di ferro → 4, 2 usi
  - bomba blu: 1 smeraldo + 2 bombe → 2, 2 usi
  - cannone: 1 smeraldo + 2 lingotti di ferro, 1 uso
  - palle di cannone: 1 smeraldo + 8 lingotti di ferro → 2, 4 usi
  - polvere da sparo: 16, 4 usi
  - TNT: 4, 4 usi
  - corda: 16, 6 usi
  - rope arrow: 1 con 8 corde, 4 usi
  - firework star casuali: 4, 4 usi
  - razzi casuali: 8, 4 usi, **senza carta** (è quello più a rischio di non caricarsi)
  ```
  /give @s minecraft:iron_ingot 32
  /give @s supplementaries:bomb 4
  ```

## Pattuglie e raid
- [x] Le pattuglie spawnano da sole. Il capitano (`/summon minecraft:pillager ~ ~ ~ {PatrolLeader:1b}`) dà Bad Omen o lascia l'Ominous Bottle
- [x] Con Bad Omen vicino ~alla base~ a letti con villager (i letti contano come POI) parte un raid: `/effect give @s minecraft:bad_omen 6000 0` vicino a qualche letto con villager
- [x] Nel villaggio abbandonato il raid non parte (non ha letti né campane)
- [x] Raid navale di Supplementaries se la base è vicino all'acqua

## Morte (Death Inventory Penalty)
```
/gamerule keepInventory
/gamerule insanesurvivaloverhaul:death_keep_equipment
/give @s minecraft:iron_chestplate
/give @s minecraft:iron_sword
/give @s minecraft:iron_pickaxe[minecraft:enchantments={levels:{"minecraft:vanishing_curse":1}}]
/give @s minecraft:cobblestone 32
/kill @s
```
- [ ] Morendo, armatura, offhand e oggetti con durabilità nella hotbar restano addosso con **-15% di durabilità**
- [ ] Tutto il resto finisce nel Totem of Holding
- [ ] Gli oggetti con Curse of Vanishing (incantesimo o runa) spariscono
- [ ] `keepInventory` resta false (in `WSCommands.toml`), `death_keep_equipment` true

## Enhanced AI
- [ ] Un villager ferito mangia pane, carote, patate o barbabietole dall'inventario:
  ```
  /summon minecraft:villager ~ ~ ~ {Health:8f,Inventory:[{id:"minecraft:bread",count:4}]}
  ```
- [ ] Un fabbro (armorer, toolsmith, weaponsmith) ripara un Iron Golem sotto il 75%; un golem sotto il 50% va da un fabbro:
  ```
  /summon minecraft:villager ~ ~ ~ {VillagerData:{profession:"minecraft:weaponsmith",level:1,type:"minecraft:plains"}}
  /summon minecraft:iron_golem ~5 ~ ~ {Health:40f}
  ```
- [ ] I mob vanno alla scala più vicina per raggiungerti in alto, salgono e possono attaccare mentre salgono; i miner non rompono le scale (`/summon minecraft:zombie` sotto un pilastro con una scala, di notte o con `/difficulty hard`)
- [ ] Le api restano vicino all'alveare
- [ ] I Creeper arrabbiati hanno 50% di resistenza al knockback (`/summon minecraft:creeper`, colpirlo prima e dopo che ti ha preso di mira)

## Altre modifiche di ISO
- [ ] Looting dà +1 drop con il 33% per livello (Ender Pearl 20%) e non toglie mai drop:
  ```
  /give @s minecraft:iron_sword[minecraft:enchantments={levels:{"minecraft:looting":3}}]
  /summon minecraft:enderman ~ ~ ~ {NoAI:1b}
  /loot give @s kill @e[type=minecraft:enderman,sort=nearest,limit=1]
  ```
  (l'ultimo ripetuto tenendo la spada in mano, poi senza)
- [ ] Piglin: 1-2 Ender Pearl dal baratto: `/loot give @s loot minecraft:gameplay/piglin_bartering` ripetuto
- [ ] Lingering Potion stackabili a 4, Spider Eye con stack normale: `/give @s minecraft:lingering_potion[minecraft:potion_contents={potion:"minecraft:healing"}] 8`, `/give @s minecraft:spider_eye 64`
- [ ] Attrezzi e armi d'oro fanno meno danno (circa come il rame): `/give @s minecraft:golden_sword` e confrontare il tooltip
- [ ] Runa Bane of Noses riattivata: compare in loot e scambi del Librarian, e fa danno bonus a villager e illager

## ISO 5.16.1.0 e RuneEnchanting 1.5.2.0
- [ ] Dopo aver caricato un mondo, `config/insanesurvivaloverhaul/server.toml` ha `restocks_per_day`, `catch_up_demand_counts_uses` e `negative_demand_limit` (al posto di `clamp_negative_demand`), e `config/runeenchanting/runes.toml` ha `Shard Damage`, `Shard Inaccuracy` e `Shard Speed Multiplier` in `[shatterburst]`
- [ ] I villager fanno restock una volta al giorno: comprare tutto da un villager senza `NoAI` vicino al job site, `/time add 6000` (niente restock), poi `/time add 24000` (restock). Gli scambi usati il giorno prima salgono di prezzo, quelli non usati non scendono sotto il prezzo base
- [ ] Spugne: una Wet Sponge al sole (di giorno, senza pioggia) si asciuga, una Sponge sotto la pioggia si bagna (`/weather rain`)
- [ ] Shatterburst: la freccia si frantuma solo colpendo un'entità (non sui blocchi), in un anello orizzontale di schegge di selce da 3 danni. Nessun crash se una scheggia uccide un mob:
  ```
  /give @s runeenchanting:rune[runeenchanting:stored_rune="runeenchanting:shatterburst"]
  /summon minecraft:zombie ~5 ~ ~ {NoAI:1b}
  ```
