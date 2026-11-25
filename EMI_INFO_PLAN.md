# Pagine EMI info nelle mod di Insane96

Questo file si usa come prompt in una sessione aperta nel repo di una mod (`C:\Users\delvi\source\repos\Insane96\<Mod>`). Il lavoro nel pack è finito, e le pagine delle mod di Insane96 sono state scritte: restano le voci in [Da fare](#da-fare).

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

## ISO: pagine spostate dal codice (fatto, 2026-11-24)

Le pagine statiche sugli oggetti di ISO sono ora in `assets/emi/recipe/additions/insanesurvivaloverhaul_*.json` (echo_lantern, daggers, shortbow, beacon, explosive_barrel, mining_charge, copper/golden_powered_rail, rich_farmland, più le nuove ore_rocks, cloth, pumpkin_pulp, solanum_neorossii, glow_block). In `ISOEmiPlugin` restano le pagine sugli oggetti vanilla, quelle con righe condizionali e quelle calcolate. Nessun riferimento ai vecchi ID trovato in ISO, nel pack, nella config o nella wiki.

## Stato del pack (2026-11-24)

Le fasi 0-4 sono fatte in `resourcepacks/survivalreimagined_lang` (inventario, vanilla, mod di terzi, revisione); resta il controllo in gioco a campione. Le pagine sui comportamenti delle mod di Insane96 sono state scritte nelle mod (ISO, RuneEnchanting, Progressive Bosses, Shields+), non ancora committate. Restano le voci qui sotto.

## Da fare

### InsaneSurvivalOverhaul

- Non è una pagina: penalità alla morte (`DeathInventoryPenalty`, gamerule `death_keep_equipment`). Una riga nella schermata di morte, del tipo "Your equipment was kept but lost durability", e un'altra con il numero di morti (ISO ha già `ClientboundDeathStatsPacket`, da vedere se si può estendere).
- Non è una pagina: Turtle Scute e Armadillo Scute (`Scutes`, `Scute drops as block`) dovrebbero avere un tooltip "Placeable" tramite InsaneLib, come fa Supplementaries con Stick e Blaze Rod.
- Non è una pagina, è da sistemare: `Portal requires crying obsidian` (`Nether.onPortalTryToActivate`) non controlla gli angoli, ma conta la Crying Obsidian in tutto il rettangolo della cornice e ne vuole almeno 4.
- Non è una pagina: la ricetta di riciclo in EMI (`Recycling`) dovrebbe dire che la resa cala con la durabilità consumata.
- `minecraft:ender_pearl`: nessuna pagina. Il plan diceva che gli Enderman la lasciano solo con Looting, ma `mob_loot_changes/entities/enderman` ne dà sempre una (Looting aggiunge la possibilità di una seconda), quindi la fonte è quella vanilla.
- Divine Fragment: con le gamerule di default (e quelle del pack, `death_min_health 20`) morire non scende sotto i 10 cuori, quindi il Crystal Heart dà vita extra oltre i 10 cuori e la morte toglie solo quella. La pagina lo dice così. Le gamerule non sono sincronizzate al client, quindi il testo non può seguirle.

### RuneEnchanting

- Librarian come fonte di Rune: con solo ISO vende un Enchanted Book vanilla (`villagers_overhaul` usa `enchant_with_levels`, e i GLM di RuneEnchanting non girano sugli scambi). Il pack sovrascrive `librarian/enchanted_book*.json` in `datapacks/survivalreimagined` con `runeenchanting:set_random_rune`, quindi nel pack vende Rune (verificato in gioco). La pagina di RuneEnchanting non cita il Librarian: la riga è nella pagina del pack `runeenchanting_rune_librarian.json` (fatto).
- Le righe su Spawner e Sculk dipendono dal data pack integrato `enchantment_changes` (attivo di default), ma RuneEnchanting non ha un plugin EMI: le pagine in JSON lo danno per attivo.

### Stamina

- Non ha oggetti. Se serve una spiegazione, va fuori da EMI (tooltip o HUD).
