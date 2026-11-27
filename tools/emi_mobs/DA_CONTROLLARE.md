# Da controllare alla fine (pagine EMI dei mob)

Tutti i test in gioco e tutti i `?` delle pagine EMI dei mob, da fare insieme a fine lavoro. Ogni fase aggiunge qui i suoi. Dopo la verifica: correggere `pages_<fase>.py` (testi) o `extras.py` (matrice), poi rilanciare `write_pages.py` e `run.sh`.

## Test generali

- [ ] Le pagine compaiono nella scheda Info di EMI su ogni uovo (fase 1: 42 mob passivi; fase 2: 24 mob ostili; fase 3: 12 mob del Nether e dell'End, più Elder Guardian e Shulker).
- [ ] I testi condivisi (`mob.breeds_alone`, `mob.breeds`, `mob.lifespan.*`, `mob.equine`, `mob.zombie.1`/`.2`, `mob.skeleton`) si vedono in fondo alle pagine giuste, senza chiavi non tradotte.
- [ ] Le pagine con più righe (`.1`, `.2`, `.3`: Chicken, Iron Golem, Villager, Creeper, Zombie Villager, uova con testi condivisi) non vengono tagliate o divise male.
- [ ] Dopo aver tolto le pagine di Drago e Wither (uova inesistenti) non restano file o chiavi `emi.info.vanillabackport.ender_dragon_*`/`wither_*`.
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

### Fase 3 (Nether, End, boss)

- [ ] **Decisione: Drago e Wither non hanno uovo.** Vanilla Backport ha solo texture e modelli di `ender_dragon_spawn_egg` e `wither_spawn_egg`, gli item non sono registrati. I testi sono pronti in `pages_vanilla_nether_end.py` (`NO_EGG`, non scritti). Dove vanno? Sul Dragon Egg / sulla Nether Star (o sul Corrupted Soul Sand e sul Corrupted End Crystal), oppure nel plugin EMI di Progressive Bosses come dice CLAUDE.md?
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
- [ ] Ender Dragon (testo non pubblicato): "Hitting it in flight hurts it more than when it's perched, and explosions hurt it less"
- [ ] Wither (testo non pubblicato): "the Ultimate does all of this and hits harder"
