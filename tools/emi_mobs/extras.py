# Manual facts that don't come from tags (config/code/data). (source, text). "?" prefix = da verificare.
ZOMBIES = ["minecraft:zombie", "minecraft:husk", "minecraft:drowned", "minecraft:zombie_villager", "minecraft:zombified_piglin"]
E = {}
def add(mobs, src, txt):
    for m in ([mobs] if isinstance(mobs, str) else mobs):
        E.setdefault(m, []).append((src, txt))

# --- Zombies
add(ZOMBIES, "Enhanced AI (MPR `fuck_baby_zombies`)", "niente Zombie bambini: tutti spawnano adulti (vale per tutto `#minecraft:zombies`)")
add(["minecraft:zombie", "minecraft:husk", "minecraft:drowned", "minecraft:zombie_villager"], "ISO `Zombie siege`", "assedio di zombie anche lontano dai villaggi")
add("minecraft:zombie", "ISO `Always convert zombie`", "i villager uccisi dagli zombie diventano sempre Zombie Villager")
add("minecraft:drowned", "Enhanced AI (MPR `drowned_trident_nerf`)", "il Tridente lanciato dai Drowned fa metà danno")
add("minecraft:drowned", "Vanilla Backport `zombie_nautilus_spawn_chance` 0.5", "metà dei Drowned negli oceani spawna in groppa a uno Zombie Nautilus")
add("minecraft:husk", "Vanilla Backport `has_camel_husks`", "nei deserti il 10% degli Husk spawnati naturalmente cavalca un Camel Husk, con un Parched dietro (`HuskMixin`)")
add("minecraft:zombie_villager", "ISO Villagers", "unica fonte di villager: si cura con Weakness + Golden Carrot (tag `#insanesurvivaloverhaul:zombie_villager_cure_items`, la durata della cura è quella vanilla), poi convalescenza di un giorno (non commercia, rallentato)")
add("minecraft:zombie_villager", "ISO `Fire resistant structure zombie villagers`", "quelli piazzati dalle strutture hanno Fire Resistance infinita, così non bruciano prima di essere trovati")
add("minecraft:zombie_villager", "ISO `No nitwits`", "i nitwit curati diventano disoccupati e possono prendere un lavoro")
add("minecraft:zombified_piglin", "Enhanced AI `Break anger`", "OFF: da disattivare (decisione 2026-11-26; il config usava `#forge:ores/quartz`, inesistente): non va nella pagina")

# --- Skeletons & arrows
add("minecraft:skeleton", "ISO `Remove skeletons from fortresses`", "non spawna più nelle Fortezze del Nether (anche se lo `spawn_overrides` di DnT lo elenca)")
add("minecraft:skeleton", "Supplementaries `quiver_skeleton_spawn_chance`", "raramente spawna con una Faretra (dipende dalla difficoltà locale)")
add(["minecraft:stray", "minecraft:bogged", "minecraft:parched"], "Bits and Balance `tippedArrowLingeringClouds.mobsEnabled`", "le sue frecce con effetto lasciano una nuvola dell'effetto dove atterrano (vale per tutte le frecce con effetto, anche dei giocatori: va sulla pagina della Tipped Arrow, qui solo un accenno)")
add("minecraft:skeleton", "Bits and Balance `tippedArrowLingeringClouds.mobsEnabled`", "?solo se ha frecce con effetto (es. Faretra di Supplementaries)")
add("minecraft:wither_skeleton", "Enhanced AI `Wither instead of fire`", "con l'arco tira frecce di Wither invece che infuocate")
add("minecraft:wither_skeleton", "Enhanced AI (MPR `wither_skeleton`)", "a volte spawna con un arco (a volte incantato)")
add("minecraft:wither_skeleton", "Progressive Bosses `no_wither_rose`", "se ucciso dal Wither non lascia la Wither Rose")
add("minecraft:parched", "Vanilla Backport `has_parched_skeletons`", "spawna nei biomi con la Desert Pyramid (codice, non nei JSON dei biomi); non brucia al sole; frecce con Weakness")

# --- Creeper
add("minecraft:creeper", "Explosion Overhaul", "esplosione dal centro del corpo, danno ridotto (x0.85), i blocchi distrutti droppano")
add("minecraft:creeper", "MPR `Better creeper lingering`", "?i Creeper con effetti di pozione lasciano una nuvola 3D esplodendo")
add("minecraft:creeper", "Enhanced AI Creeper swell `Insane survival overhaul integration`", "probabilmente senza effetto: scrive le chiavi `iguanatweaksreborn:explosion_*`, che Explosion Overhaul non legge (legge `knockback_multiplier`/`damage_multiplier`)")

# --- Spiders
add("minecraft:spider", "Enhanced AI (MPR `scale/spider`)", "più piccolo dei Ragni vanilla")
add("minecraft:cave_spider", "Bits and Balance `enableCaveSpidersInCaves` (0.15)", "parte dei Ragni nelle grotte viene sostituita da Cave Spider")
add(["minecraft:spider", "minecraft:cave_spider"], "Enhanced AI `Stuck fix`", "non restano più bloccati sui muri")

# --- Others hostile
add("minecraft:enderman", "Enhanced AI `Look anger cone`", "si arrabbia guardandolo da un angolo più ampio")
add("minecraft:enderman", "Supplementaries `enderman_head`", "la testa droppa e fa da componente redstone quando la guardi (pagina item già esistente?)")
add("minecraft:phantom", "ISO `Tired tied phantoms`", "spawnano in base alla stanchezza (Tired II+), non all'insonnia")
add("minecraft:phantom", "Enhanced AI (MPR `scale/phantoms`)", "dimensioni casuali, fino a molto più grandi")
add("minecraft:phantom", "Bits and Balance `enableImprovedPhantoms`", "i colpi danno Slowness che si accumula; Pickup è spento, le altre opzioni (doppio danno, caduta) ?valgono solo per il suo Pickup o anche per la presa di Enhanced AI")
add(["minecraft:slime", "minecraft:magma_cube"], "Enhanced AI `Slime attack fix`", "fanno danno al salto e all'atterraggio, non a ogni tick di contatto")
add("minecraft:slime", "Quark `Slimes To Magma Cubes`", "uno Slime ucciso da un Magma Block (danno `hotFloor`) si divide in Magma Cube")
add("minecraft:slime", "Quark `Slime In A Bucket`", "gli Slime piccoli si raccolgono con un secchio (fanno saltellare nei chunk slime)")
add("minecraft:slime", "Quark `Safer Creatures`", "niente danno da caduta")
add("minecraft:silverfish", "Enhanced AI `Silverfish merge with stone` / `wake up friends`", "")
add("minecraft:ghast", "Vanilla Backport `dried_ghasts`", "Dried Ghast (fossili del Nether, baratto coi Piglin) -> Ghastling -> Happy Ghast")
add("minecraft:shulker", "Bits and Balance `despawnBulletsWithShulker`", "i proiettili spariscono con lo Shulker")
add("minecraft:shulker", "Enhanced AI `Shulker armor`/`bullets`/`attack`", "armatura anche da aperto e da socchiuso (chiuso poco più del vanilla); sotto metà vita si apre solo a metà mentre spara; spara meno spesso; Levitation VI ma più breve (5 s, 8 s su Hard, contro 10 s di Levitation I)")
add("minecraft:guardian", "ISO `Guardians in deep oceans`", "spawnano anche negli oceani profondi, sotto Y 32: più piccoli e con molta meno vita di quelli del Monumento")
add("minecraft:guardian", "ISO `Guardian magic damage only`", "solo danno magico (ignora l'armatura)")
add("minecraft:elder_guardian", "Progressive Bosses Elder Guardian", "3 livelli (0-2): ogni Elder ucciso alza di 1 il livello degli altri Elder entro 64 blocchi (più vita e assorbimento, attacco più rapido, più resistenza, minion più frequenti); assorbimento e cura a ogni colpo già dal livello 0; evoca Elder Minion (Guardian con metà vita e nuoto più veloce) se ci sono meno di 6 Guardian vicini. Gli Elder da `SPAWNER` (non trial) restano vanilla")
add("minecraft:elder_guardian", "Progressive Bosses `Adventure` = false", "non impedisce di rompere blocchi e la Mining Fatigue resta vanilla (il codice agisce solo con `Adventure` = true)")
add("minecraft:warden", "ISO `Warden`", "si evoca più facilmente: bastano 2 avvisi degli Sculk Shrieker, e gli avvisi calano più lentamente")
add("minecraft:warden", "Enhanced AI (MPR `warden`)", "sale i blocchi interi senza saltare")
add("minecraft:warden", "Enhanced AI `Warden darkness/listen/sonic boom range`", "Darkness e Sonic Boom da molto più lontano, sente le vibrazioni più lontano")
add("minecraft:vindicator", "Enhanced AI (MPR `fuck_vindicators`)", "molto meno danno")
add("minecraft:vex", "Enhanced AI (MPR `fuck_vexes`, `scale/vexes`)", "molta meno vita, più grande")
add(["minecraft:vex", "minecraft:evoker"], "Quark `Vexes Die With Their Masters` / Bits and Balance `despawnVexWithEvoker`", "i Vex muoiono con il loro Evoker")
add("minecraft:pillager", "ISO villagers overhaul", "fonte di Smeraldi; pattuglie e raid attivi (`WSCommands.toml`)")
add("supplementaries:plunderer", "Supplementaries `naval_raid_chance` 0.75", "nei raid parte dei Pillager arriva in barca dal mare, guidata da un Plunderer; Galleon spenti")
add("minecraft:witch", "Enhanced AI `Dark art` = false", "spento: non evocano villager")
add("minecraft:ravager", "", "")

# --- Golems / villagers
add("minecraft:iron_golem", "ISO `Fixed iron golem damage`", "danno fisso invece che casuale")
add("minecraft:iron_golem", "Enhanced AI `Custom targeting`", "metà dei mostri in `#enhancedai:config/can_attack_iron_golem` lo attacca")
add("minecraft:iron_golem", "Bits and Balance `ironGolemsKillCreepers` = false", "spento")
add("minecraft:snow_golem", "Quark `Snow Golem Player Heads`", "uno Snow Golem con nome di un giocatore ucciso da una Witch droppa la testa del giocatore")
add("minecraft:villager", "ISO Villagers", "solo curando Zombie Villager; niente riproduzione; commerciano solo vendendo per 1 Smeraldo; prezzi che salgono e non scendono; 1 restock al giorno; mantengono i trade se perdono il job site")
add("minecraft:villager", "Quark `Villagers Follow Emeralds`", "ti seguono se tieni uno Smeraldo")
add("minecraft:villager", "Enhanced AI `Villager attacking`", "reagiscono solo ai giocatori con reputazione sotto -100 (come gli Iron Golem); `Villagers fight back enemies` = false, quindi non attaccano i mostri")
add("minecraft:villager", "Enhanced AI `Custom targeting`", "metà dei mostri in `#enhancedai:config/can_attack_villagers` li attacca")
add("minecraft:wandering_trader", "ISO villagers overhaul", "trade propri (ISO), attivo via `WSCommands.toml`")
add("supplementaries:red_merchant", "Supplementaries + datapack", "arriva al posto del Wandering Trader; trade sovrascritti nel datapack (1 Smeraldo, pochi usi)")
add("minecraft:copper_golem", "Vanilla Backport `has_copper_golems`", "si costruisce con Blocco di Rame + Carved Pumpkin; sposta oggetti dalle Copper Chest; si ossida nel tempo")

# --- Pets / animals
add(["minecraft:wolf"], "Bits and Balance `speedyWolves`", "i lupi addomesticati accelerano per raggiungerti")
add(["minecraft:wolf", "minecraft:cat", "minecraft:parrot"], "Bits and Balance `friendlyFireFriendlies`", "non puoi colpire per sbaglio i tuoi animali")
add(["minecraft:wolf", "minecraft:cat", "minecraft:parrot"], "Amendments `pets_follow_teleports`", "gli animali che ti seguono si teletrasportano con te (anche portali)")
add("minecraft:wolf", "Quark `Pat The Dogs`", "si accarezzano (tasto destro a mano vuota da accovacciato)")
add("minecraft:wolf", "Let Sleeping Dogs Lie", "seduti a lungo si sdraiano")
add("minecraft:wolf", "Vanilla Backport `wolf_sound_variants`", "varianti di verso")
add("minecraft:ocelot", "ISO `Ocelot to cat`", "addomesticato diventa un Gatto")
add("minecraft:cat", "ISO `Ocelot to cat`", "si ottiene anche addomesticando un Ocelot; villaggi senza gatti; c'è quello della Swamp Hut")
add("minecraft:parrot", "ISO Livestock", "addomesticati e fatti innamorare solo con Semi di Melone e Zucca")
add("minecraft:parrot", "Vibrant Parrots", "colori diversi; innamorati depongono un uovo del loro colore; restano sulla spalla in volo/caduta; si tolgono accovacciandosi; Bird Cage")
add("minecraft:parrot", "ISO `Shoulder dismount fall distance` 4", "cadono dalla spalla solo dopo una caduta di qualche blocco")
add("minecraft:parrot", "Naturalist `parrot_flight`", "con un Parrot per spalla e un Bird di Naturalist (`naturalist:bird`) in testa, tenendo premuto salto in aria si sale lentamente (`ParrotFlight`)")
add(["minecraft:horse", "minecraft:donkey", "minecraft:mule", "minecraft:llama", "minecraft:trader_llama", "minecraft:skeleton_horse", "minecraft:zombie_horse"], "ISO `Equine attributes`", "statistiche fisse per specie (niente genetica), da `equine_attributes.json`")
add(["minecraft:horse", "minecraft:donkey", "minecraft:mule", "minecraft:skeleton_horse", "minecraft:zombie_horse"], "Quark `Horses Swim`", "nuotano con il giocatore in groppa")
add("minecraft:horse", "Bits and Balance `dualRiders`", "due giocatori sullo stesso cavallo")
add(["minecraft:horse", "minecraft:donkey", "minecraft:mule"], "Supplementaries Sugar Cube", "mangiato dà Speed")
add("minecraft:zombie_horse", "Vanilla Backport `has_zombie_horses`", "spawna come i mostri (`MobCategory.MONSTER`, regole dei mostri, peso 5: raro) in pianure e savane, con uno Zombie in sella; brucia al sole senza armatura (che si consuma); domabile senza cavaliere, non si riproduce")
add("minecraft:zombie_horse", "Supplementaries `zombie_horse_inverse_conversion`", "sotto Weakness, con una Golden Carrot torna Horse")
add("minecraft:camel", "Ecologics `camelChestsEnabled`", "gli si può mettere una Chest")
add("minecraft:camel", "Vanilla Backport `camel_spawns` + Ecologics `spawn_camel`", "spawna nei deserti")
add("minecraft:chicken", "Quark `Grab Chickens`", "si prende in testa e rallenta la caduta (Slowness)")
add("minecraft:chicken", "ISO Animal products", "uova più lente; da un uovo lanciato esce un pulcino 1 volta su 8")
add(["minecraft:cow", "minecraft:mooshroom", "minecraft:goat"], "ISO `Fluid cooldown`", "si mungono una volta ogni tanto (anche lo stufato del Mooshroom)")
add("minecraft:mooshroom", "Mooshroom Tweaks `becomeBrownChance` 0.5", "?metà dei Mooshroom è marrone")
add("minecraft:sheep", "ISO Aging", "adulti e anziani danno più lana")
add("minecraft:sheep", "Name Tag Upgrade", "il nome si toglie con le cesoie (prima la lana)")
add(["minecraft:rabbit"], "Quark `Safer Creatures`", "meno danno da caduta")
add(["minecraft:pig"], "Naturalist `remove_forest_pigs`", "niente maiali nelle foreste")
add(["minecraft:chicken", "minecraft:cow", "minecraft:pig", "minecraft:sheep"], "Naturalist `remove_farm_animals_savanna/swamp`", "niente in savane e paludi")
add(["minecraft:cow", "minecraft:pig", "minecraft:chicken"], "Vanilla Backport `farm_animal_variants` = false", "spento: nessuna variante")
add("minecraft:fox", "Ecologics `foxesAttackSquirrels`", "cacciano gli Squirrel")
add(["minecraft:fox", "minecraft:rabbit"], "Naturalist forest foxes/rabbits", "spawn extra nelle foreste")
add("minecraft:bee", "Enhanced AI `Bee hive navigation`", "si allontanano meno dall'alveare")
add(["minecraft:turtle", "minecraft:armadillo"], "ISO `Scutes`", "le scaglie cadono come blocco impilabile")
add("minecraft:armadillo", "ISO `Disable armadillo brushing`", "non si spazzolano: le scaglie si raccolgono quando le perde")
add(["minecraft:wolf", "minecraft:horse", "minecraft:parrot"], "ISO Aging", "invecchiano e muoiono di vecchiaia (`Die of old age` = true; una Poisonous Potato li ferma, vale per tutti i mob con un tag lifespan)")
add("minecraft:cat", "ISO Aging", "non invecchia: non è in nessun tag `*_lifespan`")

# --- bosses
add("minecraft:ender_dragon", "Progressive Bosses Dragon", "2 definizioni: base (livello 0) e corrupted (livello 4 = respawn con 4 Corrupted End Crystal, ricetta End Crystal + Dragon Egg). Si rigenera da sola e dai cristalli (di più dai corrotti); distruggere un cristallo che la cura la ferisce; più danno in volo, meno da appollaiata e dalle esplosioni; si arrabbia col danno (più veloce, più attacchi); acid ball con nube, blast attack che respinge lontano, carica, minion Shulker; sotto metà vita può far rinascere cristalli (con Phantom); gabbie sulle torri, alcune con cristalli corrotti; cristalli immuni alle altre esplosioni; gabbie con ossidiana agli angoli. ?con 1-3 cristalli corrotti non c'è definizione: Drago vanilla?")
add("minecraft:wither", "Progressive Bosses Wither", "4 varianti: base (evocazione normale) e, con Corrupted Soul Sand al centro (1/2/3 Nether Star), armored, summoner, ultimate (solo nel Nether). Tutte: si rigenera, si cura con le uccisioni dei teschi, raffiche di teschi quando colpito, cariche sotto metà vita e se non ti vede, esplode alla morte, ogni uccisione lascia una Wither Rose. Armored: armatura alta; summoner: Wither Minion (alcuni con arco) e cura alta; ultimate: tutto. Dalla armored in su le esplosioni ignorano i blocchi wither-proof")
add("minecraft:wither", "Explosion Overhaul", "nessun knockback dalle esplosioni")

# --- VB new mobs
add("minecraft:creaking", "Vanilla Backport `creaking`", "nasce di notte dal Creaking Heart nel Pale Garden; non si ferma il giorno (`do_creaking_hearts_work_on_day` = false)")
add("minecraft:happy_ghast", "Vanilla Backport + Bits and Balance `speedyHappyGhasts`", "cavalcabile con Harness; risente di Speed/Slowness")
add(["minecraft:nautilus", "minecraft:zombie_nautilus"], "Vanilla Backport `has_nautilus`", "cavalcabile sott'acqua, armatura da Nautilus nei loot")
add("minecraft:sulfur_cube", "Vanilla Backport `has_sulfur_cubes`", "spawna nelle Sulfur Caves; archetipi esplosivi e dannosi attivi; si mette nel secchio")
add("minecraft:camel_husk", "Vanilla Backport `has_camel_husks`", "arriva con il 10% degli Husk dei deserti, con Husk e Parched in sella; si sella e si cavalca, non si riproduce")

# --- Naturalist / Ecologics
NATURALIST_SPEED = True
add("ecologics:coconut_crab", "Ecologics", "esce dal Cocco che cade dalle palme; con il Cocco addosso prende metà danno e reagisce, senza scappa")
add("ecologics:squirrel", "Ecologics", "spawna nelle Plains (biome modifier `ecologics:spawn_squirrel`)")

# Where, for mobs not (only) spawned by biomes. "?" = da verificare
DOVE = {
 "minecraft:allay": "nelle gabbie delle Pillager Outpost e nella Woodland Mansion (DnT)",
 "minecraft:bee": "dai Bee Nest sugli alberi (foreste di betulle, pianure, prati, ciliegi) e dagli alveari",
 "minecraft:breeze": "solo dai trial spawner (Trial Chambers, Hellish Trials)",
 "minecraft:cat": "Swamp Hut (DnT) e addomesticando un Ocelot; ?i villaggi abbandonati non ne generano (pool vuoto), da verificare se il CatSpawner vanilla li fa comparire vicino ai letti",
 "minecraft:elder_guardian": "nell'Ocean Monument (DnT Trident Trial Monument), piazzati e da trial spawner",
 "minecraft:ender_dragon": "nell'End, si può far rinascere con 4 End Crystal sul portale",
 "minecraft:endermite": "a volte da una Ender Pearl lanciata; spawner in Formations Nether e Philips' Ruins",
 "minecraft:evoker": "Woodland Mansion (DnT Illager Manor) e raid",
 "minecraft:iron_golem": "si costruisce (4 blocchi di ferro + Carved Pumpkin); i villager lo evocano (ogni tanto, più spesso in pericolo); piazzato in Pillager Outpost (gabbia), Woodland Mansion, Stronghold (DnT)",
 "minecraft:mule": "da Cavallo + Asino; con ISO `prevent_breeding` ?solo se si innamorano da soli",
 "minecraft:piglin_brute": "Bastion Remnant; spawner in Formations Nether; Incendium",
 "minecraft:pillager": "Pillager Outpost, pattuglie nell'Overworld, raid; Woodland Mansion (DnT)",
 "minecraft:ravager": "raid; Woodland Mansion (DnT)",
 "minecraft:shulker": "End City; Philips' Ruins (End Gate Fortress)",
 "minecraft:silverfish": "dai blocchi infestati (Stronghold, montagne); spawner nello Stronghold (DnT)",
 "minecraft:skeleton_horse": "trappola: un fulmine durante un temporale crea 4 cavalieri scheletro",
 "minecraft:sniffer": "solo da Sniffer Egg (archeologia nelle Warm Ocean Ruins)",
 "minecraft:snow_golem": "si costruisce (2 blocchi di neve + Carved Pumpkin)",
 "minecraft:tadpole": "dalla Frogspawn che le Rane depongono",
 "minecraft:trader_llama": "con il Wandering Trader",
 "minecraft:vex": "evocati dagli Evoker; spawner in Incendium (Sanctum)",
 "minecraft:villager": "solo curando Zombie Villager (ISO); pochi nelle strutture: cella dello Stronghold (DnT), Woodland Mansion (DnT), Igloo",
 "minecraft:vindicator": "Woodland Mansion (DnT Illager Manor), raid",
 "minecraft:wandering_trader": "compare vicino ai giocatori ogni tanto (attivo in `WSCommands.toml`)",
 "minecraft:warden": "evocato dagli Sculk Shrieker nel Deep Dark (Ancient City)",
 "minecraft:wither": "si costruisce (4 Soul Sand + 3 teschi di Wither Skeleton)",
 "minecraft:zoglin": "Hoglin portato nell'Overworld; spawner in Philips' Ruins",
 "minecraft:zombie_horse": "Vanilla Backport: al buio (regole dei mostri) in Plains, Snowy Plains e savane (`spawns_zombie_horses`), raro",
 "minecraft:camel_husk": "Vanilla Backport: con il 10% degli Husk dei deserti (codice)",
 "minecraft:copper_golem": "si costruisce",
 "minecraft:creaking": "dai Creaking Heart nel Pale Garden, di notte",
 "minecraft:happy_ghast": "da un Dried Ghast (fossili del Nether, baratto) messo in acqua -> Ghastling",
 "minecraft:nautilus": "oceani: raro in quelli freddi e ghiacciati, più frequente in quelli normali, tiepidi e caldi (`spawns_nautilus*`)",
 "minecraft:parched": "Vanilla Backport: biomi con la Desert Pyramid (codice)",
 "minecraft:sulfur_cube": "Sulfur Caves (Vanilla Backport)",
 "minecraft:zombie_nautilus": "con i Drowned negli oceani (metà dei Drowned ne cavalca uno); variante corallo negli Warm Ocean",
 "naturalist:ant": "dagli Ant Hill (`add_ant_hills`)",
 "naturalist:caterpillar": "dalle Butterfly innamorate, poi diventa Chrysalis su un tronco",
 "ecologics:coconut_crab": "esce dal 20% dei Cocchi che si rompono cadendo dalle palme (spiagge)",
 "supplementaries:red_merchant": "quando non arriva il Wandering Trader (`RedMerchantSpawnerMixin`); gli Evoker trasformano i Wandering Trader",
 "supplementaries:plunderer": "nei raid vicino all'acqua, al timone delle barche dei Pillager (Galleon spenti)",
 "minecraft:cave_spider": "spawner nelle Mineshaft",
 "minecraft:zombie": "spawner nei Dungeon",
 "minecraft:skeleton": "spawner nei Dungeon",
 "minecraft:spider": "spawner nei Dungeon",
 "minecraft:witch": "raid",
}
add("minecraft:chicken", "ISO Crops (`chicken_food_items`)", "si nutrono solo con Semi di Melone, Zucca e Torchflower; gli altri semi (grano, barbabietola, lino, carota) le attirano soltanto")
