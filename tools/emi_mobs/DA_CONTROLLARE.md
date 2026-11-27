# Da controllare alla fine (pagine EMI dei mob)

Tutti i test in gioco e tutti i `?` delle pagine EMI dei mob, da fare insieme a fine lavoro. Ogni fase aggiunge qui i suoi. Dopo la verifica: correggere `pages_<fase>.py` (testi) o `extras.py` (matrice), poi rilanciare `write_pages.py` e `run.sh`.

## Test generali

- [ ] Le pagine compaiono nella scheda Info di EMI su ogni uovo (fase 1: 42 mob passivi; fase 2: 24 mob ostili).
- [ ] I testi condivisi (`mob.breeds_alone`, `mob.breeds`, `mob.lifespan.*`, `mob.equine`, `mob.zombie.1`/`.2`, `mob.skeleton`) si vedono in fondo alle pagine giuste, senza chiavi non tradotte.
- [ ] Le pagine con più righe (`.1`, `.2`, `.3`: Chicken, Iron Golem, Villager, Creeper, Zombie Villager, uova con testi condivisi) non vengono tagliate o divise male.
- [ ] La descrizione dell'advancement di EMI dice che le Spawn Egg hanno una pagina sul loro mob.

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

### Fasi successive (già nella matrice)

- [ ] **Elder Guardian** (Progressive Bosses): come sale il livello (numero di Elder uccisi nel Monumento?)
- [ ] **Ender Dragon** (Progressive Bosses): cos'è la definizione `corrupted` (Corrupted End Crystal?); dettagli da leggere nei JSON
- [ ] **Wither** (Progressive Bosses): come si sceglie la variante (Corrupted Soul Sand?)
- [ ] **Camel Husk** (Vanilla Backport): spawna nei deserti di notte con Husk e Parched in sella (dal codice, non nei JSON dei biomi)?
- [ ] **Parched** (Vanilla Backport `has_parched_skeletons`): spawna nei deserti (dal codice)?
- [ ] **Caterpillar** (Naturalist): nasce dalle Butterfly (uova/crisalide)?
- [ ] **Coconut Crab** (Ecologics): esce dal Cocco che cade dalle palme?
- [ ] **Red Merchant** (Supplementaries): arriva con il Wandering Trader?

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
