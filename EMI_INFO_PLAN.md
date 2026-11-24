# Pagine EMI info nelle mod di Insane96

Questo file si usa come prompt in una sessione aperta nel repo di una mod (`C:\Users\delvi\source\repos\Insane96\<Mod>`). Il lavoro nel pack è finito: restano le pagine dei comportamenti che vengono dalle mod di Insane96, elencate in [Pagine da aggiungere](#pagine-da-aggiungere).

## Come si aggiungono

Le pagine si aggiungono come risorse della mod, senza codice: EMI legge `assets/emi/recipe/additions/` da tutte le risorse caricate, jar delle mod compresi. Non serve nemmeno la dipendenza da EMI.

- Un file per pagina in `src/main/resources/assets/emi/recipe/additions/<modid>_<nome>.json`. Il namespace `emi` è obbligatorio: EMI ignora gli altri. Il prefisso `<modid>_` evita collisioni con le pagine di altre mod e dei resource pack.
- Formato:
  ```json
  {
      "type": "emi:info",
      "stacks": ["item:<modid>:<id>", "#item:<namespace>:<tag>"],
      "text": ["emi.info.<modid>.<nome>", "emi.info.<modid>.<nome>.2"]
  }
  ```
  Ogni voce di `text` è una chiave di traduzione e diventa un paragrafo. Le varianti vanno in un'unica pagina con più `stacks` o con un tag `#item:`.
- I testi vanno nel file lang della mod (`assets/<modid>/lang/en_us.json`). RuneEnchanting genera il suo con la datagen (`src/generated`), quindi lì la chiave va aggiunta al provider.
- Un resource pack con lo stesso percorso sostituisce la pagina, quindi un modpack può correggerla o toglierla.

**Limite**: un file JSON non ha condizioni. Una pagina il cui contenuto dipende dalla config (feature spenta, riga che compare solo con un'opzione) o da una lista calcolata a runtime resta nel plugin EMI in codice. Per gli oggetti della mod stessa di solito la condizione non serve: se la feature è spenta, l'oggetto non si ottiene.

## Regole di stile

- Inglese, frasi brevi, comprensibili anche per chi conosce poco Minecraft.
- Niente numeri esatti, salvo quando servono per usare la meccanica.
- Sempre da dove viene un oggetto che si ottiene da una loot table (chest, drop dei mob, pesca, archeologia), perché EMI non le mostra. Niente "dove trovarlo" per gli oggetti comuni in superficie.
- Niente pagina, o niente riga, per quello che il giocatore vede già da solo: ricetta in EMI, tooltip, advancement, primo utilizzo.
- Si descrive il comportamento con la config di default; se dipende da un'opzione, vale il limite sopra.
- Prima di scrivere si controlla il comportamento effettivo nel codice e nei data pack integrati, non nella descrizione della feature.

## ISO: spostare le pagine dal codice

`ISOEmiPlugin` registra 29 pagine in codice (`createSimpleInfo` in `register` e `addInfo` in `addInfos`). Quelle statiche vanno spostate in `assets/emi/recipe/additions/`, con le stesse chiavi lang. Le pagine in codice hanno ID `insanesurvivaloverhaul:/info/<id>` o `insanesurvivaloverhaul:/<id>`, quelle in JSON lo prendono dal percorso del file: da controllare che non ci siano riferimenti al vecchio ID.

- **Da spostare** (oggetti di ISO, nessuna riga condizionale): `echo_lantern`, `daggers`, `shortbow`, `beacon` (il Beacon di ISO), `explosive_barrel`, `mining_charge`, `copper_powered_rail`, `golden_powered_rail`, `rich_farmland` (righe `bone_meal.rich_farmland` e `rich_farmland`; l'oggetto esiste solo con Rich Farmland attivo).
- **Restano in codice**, perché riguardano oggetti vanilla e la pagina o alcune righe dipendono dalla config: `name_tag`, `crops` (semi), `info_portal_corners` (`Portal requires crying obsidian`), `beds` (`allowSleepingEvenWhenNotTired`), `hoes`, `wooden_equipment`, `copper_ore` (data pack di Stone Tools Gone), `conduit` (`removeHaste`), `fishing_rod`, `sweet_berry_bush` (`noDamageIfDressed`), `cake` (`buffCake`), `sponge` (`dryWetWeather`), `campfire`, `spawner`, `bone_meal`, `totem_of_undying`, `shulker_box_from_pouches`, `zombie_villager_cure` (`convalescenceDuration`).
- **Restano in codice perché calcolate**: `falling_blocks_damage` (blocchi `Fallable` che fanno danno) e `break_on_fall` (tag di blocchi, non di oggetti).

Le nuove pagine di ISO elencate sotto seguono lo stesso criterio: in JSON se sono statiche, nel plugin se dipendono dalla config.

## Stato del pack (2026-11-24)

Le fasi 0-4 sono fatte in `resourcepacks/survivalreimagined_lang` (inventario, vanilla, mod di terzi, revisione); resta il controllo in gioco a campione. Le pagine sui comportamenti delle mod di Insane96 non sono state scritte nel pack: sono qui sotto, con la fonte (opzione di config o classe) e, dove c'era, il testo già scritto. Quando una mod aggiunge una pagina, la voce si toglie da qui. Se il pack ha una pagina che la mod rende inutile, va tolta dal pack.

## Pagine da aggiungere

Formato: `oggetti` — cosa spiegare (origine). Le voci "Non è una pagina" sono emerse durante il lavoro e vanno fatte in altro modo (tooltip, HUD, correzione di un bug).

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
