"""Build the mob x mod matrix (Markdown). Usage: python -I matrix.py <out_dir> <instance_dir> <matrix.md>"""
import json, os, sys, zipfile, glob, importlib.util
outd, inst, dest = sys.argv[1], sys.argv[2], sys.argv[3]
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("extras", os.path.join(here, "extras.py")); ex = importlib.util.module_from_spec(spec); spec.loader.exec_module(ex)
L = lambda f: json.load(open(os.path.join(outd, f), encoding="utf-8"))
etags, itags, spawns = L("entity_tags.json"), L("item_tags.json"), L("spawn_biomes.json")
btags, biomes, sstruct, nbt = L("biome_tags.json"), L("biomes.json"), L("structure_spawns.json"), L("nbt_mobs.json")
cf = os.path.abspath(os.path.join(inst, "..", ".."))

# names
names = {}
def lang(z, path):
    try: names.update(json.loads(z.read(path).decode("utf-8")))
    except Exception: pass
vz = zipfile.ZipFile(os.path.join(cf, "Install", "versions", "1.21.1", "1.21.1.jar"))
lang(vz, "assets/minecraft/lang/en_us.json")
for j in glob.glob(os.path.join(inst, "mods", "*.jar")):
    z = zipfile.ZipFile(j)
    for n in z.namelist():
        if n.endswith("/lang/en_us.json"): lang(z, n)
nm = lambda e: names.get("entity." + e.replace(":", "."), e)
bname = lambda b: names.get("biome." + b.replace(":", "."), b.split(":")[1].replace("_", " ").title())

VANILLA = "allay armadillo axolotl bat bee blaze bogged breeze camel cat cave_spider chicken cod cow creeper dolphin donkey drowned elder_guardian ender_dragon enderman endermite evoker fox frog ghast glow_squid goat guardian hoglin horse husk iron_golem llama magma_cube mooshroom mule ocelot panda parrot phantom pig piglin piglin_brute pillager polar_bear pufferfish rabbit ravager salmon sheep shulker silverfish skeleton skeleton_horse slime sniffer snow_golem spider squid stray strider tadpole trader_llama tropical_fish turtle vex villager vindicator wandering_trader warden witch wither wither_skeleton wolf zoglin zombie zombie_horse zombie_villager zombified_piglin".split()
VB = "camel_husk copper_golem creaking happy_ghast nautilus parched sulfur_cube zombie_nautilus".split()
NAT = "alligator anglerfish ant bass bear bird black_bear blobfish boar butterfly capybara caterpillar catfish clam crab deer desert_scorpion dragonfly duck elephant firefly giant_isopod giraffe great_white_shark hedgehog hippo jellyfish jungle_scorpion komodo_dragon lion lizard mammoth mole ostrich piranha rat ray rhino snail snake starfish tiger tortoise turkey vulture whale zebra".split()
GROUPS = [("Vanilla", [("minecraft:" + m) for m in VANILLA]), ("Vanilla Backport", [("minecraft:" + m) for m in VB]),
          ("Naturalist", ["naturalist:" + m for m in NAT]), ("Ecologics", ["ecologics:coconut_crab", "ecologics:penguin", "ecologics:squirrel"]),
          ("Supplementaries", ["supplementaries:red_merchant", "supplementaries:plunderer"])]

T = {  # tag -> (source, italian text); "OFF" source = present but neutralized
 "enhancedai:animal/scared_attack/can_be_neutral": ("EAI Animal scared attack", "a volte reagisce se colpito"),
 "enhancedai:animal/scared_attack/can_be_hostile": ("EAI Animal scared attack", "raramente è ostile"),
 "enhancedai:animal/scared_attack/can_be_scared_by_players": ("EAI Animal scared attack", "a volte scappa dai giocatori"),
 "enhancedai:animal/can_panic": ("EAI Animals panic", "il branco scappa se uno viene colpito"),
 "enhancedai:animal/can_ignore_food_temptation": ("EAI Not tempted animals", "metà non segue il cibo in mano"),
 "enhancedai:animal/stay_near_dismount": ("EAI Stay near dismount", "non si allontana da dove scendi"),
 "enhancedai:creeper/can_launch": ("EAI Creeper launch", "a volte si lancia contro il giocatore"),
 "enhancedai:creeper/change_swell": ("EAI Creeper swell", "esplode anche attraverso i muri, a volte cammina innescato, sfonda muri (breach), raramente 'angry' più potente"),
 "enhancedai:creeper/disable_falling_swelling": ("EAI Disable falling swelling", "non si innesca cadendo"),
 "enhancedai:creeper/tnt_like": ("EAI Tnt like creepers", "a volte si innesca se colpito da un'esplosione"),
 "enhancedai:drowned/change_swim_up": ("EAI Better drowned swim up", "salta fuori dall'acqua"),
 "enhancedai:drowned/attack_during_day": ("EAI Drowned attack during day", "attacca anche di giorno"),
 "enhancedai:drowned/sun_resistant": ("EAI Sun resistant drowned", "brucia al sole solo dopo un po'"),
 "enhancedai:mobs/drowning_targets": ("EAI Drowning targets", "afferra i bersagli e li porta sott'acqua"),
 "enhancedai:mobs/air_stealer": ("EAI Air steal", "ruba aria colpendo"),
 "enhancedai:mobs/biting_mobs/can_bite": ("EAI Biting mobs", "morde se colpito senza un'arma"),
 "enhancedai:mobs/can_flee": ("EAI Flee target", "a volte si tiene a distanza"),
 "enhancedai:mobs/healed_by_snowballs": ("EAI Healed by snowballs", "curato dalle palle di neve"),
 "enhancedai:mobs/can_disrupt_item": ("OFF", "Item disruption (feature spenta)"),
 "enhancedai:mobs/can_jump_in_place": ("EAI Jump", "salta sul posto se sei poco più in alto"),
 "enhancedai:mobs/leaders": ("EAI Leaders", "alcuni sono leader e chiamano rinforzi"),
 "enhancedai:mobs/can_open_doors": ("EAI Open doors", "apre le porte"),
 "enhancedai:mobs/panic_on_fire": ("EAI Panic on fire", None), "enhancedai:mobs/can_equip_shield": ("OFF", "Shielding (`Chance to equip` 0)"),
 "enhancedai:mobs/swim_speed_multiplier": ("EAI Swimmers", "nuoto più veloce"),
 "enhancedai:mobs/vehicle_anti_cheese/break_vehicle": ("EAI Vehicle anti cheese", None),
 "enhancedai:mobs/vehicle_anti_cheese/prevent_riding": ("EAI Vehicle anti cheese", None),
 "enhancedai:mobs/can_run_from_explosions": ("EAI Avoid explosions", None), "enhancedai:mobs/can_climb": ("EAI Climbing", "sale le scale a pioli"),
 "enhancedai:mobs/shockwave/can_use": ("OFF", "Falling shockwave (feature spenta)"),
 "enhancedai:mobs/can_equip_fishing_rod": ("EAI Fisher mobs", "a volte ha una canna da pesca e ti tira a sé"),
 "enhancedai:mobs/can_lunge": ("EAI Lunge at target", "si ferma un attimo e poi si lancia contro il bersaglio"),
 "enhancedai:mobs/can_mine": ("OFF", "Miner mobs da config (`Miner chance` 0); per gli zombie lo attiva MPR (vedi sotto)"),
 "enhancedai:mobs/can_parkour": ("OFF", "Parkour (feature spenta)"), "enhancedai:mobs/can_patrol": ("EAI Patrol", "torna dove è spawnato"),
 "enhancedai:mobs/can_equip_pearl": ("EAI Pearler mobs", "a volte ha Ender Pearl e le lancia per raggiungerti"),
 "enhancedai:mobs/pick_up_and_throw/can_pick_up": ("EAI Pick up and throw", "a volte raccoglie altri mob e te li lancia"),
 "enhancedai:mobs/riding/can_mount": ("EAI Riding", "a volte cavalca altri mob"),
 "enhancedai:mobs/riding/can_be_mounted": ("EAI Riding", "altri mob possono cavalcarlo"),
 "enhancedai:mobs/can_sprint": ("EAI Sprint", "a volte corre vicino al bersaglio"),
 "enhancedai:mobs/targeting/apply_xray": ("EAI Targeting", None), "enhancedai:mobs/targeting/alert_nearby": ("EAI Targeting", None),
 "enhancedai:mobs/targeting/follow_range_override": ("EAI Targeting", None),
 "enhancedai:mobs/teleport_anti_cheese/can_use": ("EAI Teleport anti-cheese", "se lo bersagli da posti irraggiungibili si teletrasporta"),
 "enhancedai:mobs/teleport_to_target/can_teleport": ("EAI Teleport to target", "teletrasporta altri mob vicino al bersaglio"),
 "enhancedai:mobs/throwing_web/can_throw_webs": ("EAI Web thrower", "a volte lancia ragnatele che rallentano"),
 "enhancedai:mobs/throwing_web/poisonous_webs": ("EAI Web thrower", "le ragnatele avvelenano"),
 "enhancedai:phantom/grab_targets": ("EAI Grabbing phantoms", "afferra e porta in aria finché non lo colpisci"),
 "enhancedai:shulker/apply_armor_modifiers": ("EAI Shulker armor", "armatura anche da aperto e da socchiuso"),
 "enhancedai:skeleton/can_flee": ("EAI Skeleton flee target", "si allontana se ti avvicini"),
 "enhancedai:skeleton/better_shooting": ("EAI Skeleton shoot", "tira più lontano, più spesso e si sposta di lato"),
 "enhancedai:slime/magma_cube_surf_speed": ("EAI Magma cube surf speed", "veloce nella lava"),
 "enhancedai:slime/jump_rate": ("EAI Slime jump delay", "salta più spesso"), "enhancedai:slime/spawn_size": ("EAI Slime size", "può spawnare più grande"),
 "enhancedai:villager/alert_protectors": ("EAI Villager alert protectors", "se in pericolo avvisa gli Iron Golem"),
 "enhancedai:villager/can_attack": ("EAI Villager attacking", "si difende"), "enhancedai:villager/eats_to_heal": ("EAI Villager eat to heal", "mangia per curarsi"),
 "enhancedai:villager/can_repair_golems": ("EAI Villager golem repair", "i fabbri riparano gli Iron Golem"),
 "enhancedai:villager/repairable_golems": ("EAI Villager golem repair", "riparato dai fabbri, va da loro se ferito"),
 "enhancedai:witch/thirsty": ("EAI Thirsty witches", "beve più pozioni"), "enhancedai:witch/allied_monsters/can_target_monsters": ("EAI Allied monsters", "lancia pozioni buone ai mostri vicini"),
 "enhancedai:witch/allied_monsters/eligible_targets": ("EAI Allied monsters", None), "enhancedai:witch/can_perform_dark_arts": ("OFF", "Dark art (feature spenta)"),
 "enhancedai:witch/better_potion_throwing": ("EAI Witch potion throwing", "lancia più lontano, più veloce e più tipi di pozione"),
 "enhancedai:ghast/change_shoot": ("EAI Ghast shooting", "più palle di fuoco, a volte anche senza vederti"),
 "enhancedai:illager/better_shooting": ("EAI Pillager shoot", "tira più lontano e più preciso"),
 "enhancedai:blaze_attack/change_attack": ("EAI Blaze attack", "raffiche di palle di fuoco più lunghe"),
 "enhancedai:snow_golem/damaging_snowballs": ("EAI Snow golems", "le palle di neve fanno danno"), "enhancedai:snow_golem/freezing_snowballs": ("EAI Snow golems", "e congelano"),
 "enhancedai:speed_bonus": ("EAI MPR `speed_bonus` + `outside_nerf`", None),
 "enhancedai:zombies": ("EAI MPR `zombies`, `scale/zombies`", "più piccoli a caso; nelle grotte dell'Overworld alcuni sono minatori (più in profondità, più spesso)"),
 "enhancedai:overworld_zombies": ("EAI MPR `overworld_zombies_equipment`", "armatura (anche rame) e armi/attrezzi, più spesso con la luna piena, alla luce del cielo e in profondità"),
 "enhancedai:skeletons": ("EAI MPR `scale/skeletons`", "più piccoli a caso"),
 "enhancedai:overworld_skeletons": ("EAI MPR `overworld_skeletons`", "armatura (più spesso con la luna piena e in profondità), meno preciso"),
 "enhancedai:iron_golems": ("EAI MPR `iron_golems`", "subisce molto meno danno e quasi non viene spinto"),
 "enhancedai:snow_golems": ("EAI MPR `snow_golems`", "ha un po' di armatura"),
 "enhancedai:wolves": ("EAI MPR `wolves`", "più veloce"), "enhancedai:slow_passive_healing": ("EAI MPR `slow_passive_healing`", "si cura lentamente da solo"),
 "enhancedai:small_animals": ("EAI MPR `small_animals`", "attacco più debole"), "enhancedai:sea_creatures": ("EAI MPR `scale/sea_creatures`", "dimensioni casuali"),
 "enhancedai:spiders": ("EAI MPR `spiders`", "quasi niente danno da caduta, un po' più lento"),
 "enhancedai:all_mobs": ("EAI MPR `deepness_buff`", None),
 "insanesurvivaloverhaul:prevent_breeding": ("ISO Breeding + Well fed", "non si fa riprodurre a mano: si innamora da solo, più spesso se nutrito ('well fed'), meno se affollato"),
 "insanesurvivaloverhaul:breedable_animals": ("ISO Breeding", "riproduzione più lenta, può fallire, gemelli"),
 "insanesurvivaloverhaul:really_low_lifespan": ("ISO Aging", "vita molto breve"), "insanesurvivaloverhaul:low_lifespan": ("ISO Aging", "vita breve"),
 "insanesurvivaloverhaul:medium_lifespan": ("ISO Aging", "vita media"), "insanesurvivaloverhaul:high_lifespan": ("ISO Aging", "vita lunga"),
 "insanesurvivaloverhaul:really_high_lifespan": ("ISO Aging", "vita molto lunga"),
 "insanesurvivaloverhaul:passive_regen": ("ISO Misc mobs `Passive regen chance`", "si cura lentamente da solo"),
 "supplementaries:cage_catchable": ("Supplementaries Cage", "catturabile in gabbia"), "supplementaries:cage_baby_catchable": ("Supplementaries Cage", "catturabile in gabbia da cucciolo"),
 "supplementaries:jar_catchable": ("Supplementaries Jar", "catturabile in un barattolo"), "supplementaries:jar_baby_catchable": ("Supplementaries Jar", "catturabile in un barattolo da cucciolo"),
 "supplementaries:flute_pet": ("Supplementaries Flute", "richiamabile con il Flauto"), "supplementaries:eats_fodder": ("Supplementaries Fodder", "mangia il Fodder"),
 "supplementaries:urn_spawn": ("Supplementaries Urn", "può uscire dalle Urne rotte nelle grotte"),
}
GENERIC = {"enhancedai:mobs/targeting/apply_xray", "enhancedai:mobs/targeting/alert_nearby", "enhancedai:mobs/targeting/follow_range_override",
           "enhancedai:mobs/can_run_from_explosions", "enhancedai:mobs/panic_on_fire", "enhancedai:mobs/vehicle_anti_cheese/break_vehicle",
           "enhancedai:all_mobs", "enhancedai:speed_bonus", "enhancedai:witch/allied_monsters/eligible_targets",
           "enhancedai:animal/scared_attack/can_be_neutral", "enhancedai:animal/scared_attack/can_be_hostile",
           "enhancedai:animal/scared_attack/can_be_scared_by_players", "enhancedai:animal/can_panic", "enhancedai:animal/can_ignore_food_temptation"}
GEN_LABEL = {"enhancedai:speed_bonus": "S", "enhancedai:all_mobs": "D", "enhancedai:mobs/targeting/apply_xray": "T",
             "enhancedai:mobs/can_run_from_explosions": "X", "enhancedai:animal/can_panic": "A", "enhancedai:animal/scared_attack/can_be_neutral": "A"}

OW = set(btags.get("minecraft:is_overworld", [])); NE = set(btags.get("minecraft:is_nether", [])); EN = set(btags.get("minecraft:is_end", []))
def summarize(bs):
    bs = {b for b in bs if b in biomes}
    if not bs: return None
    parts = []
    ow, ne, en = bs & OW, bs & NE, bs & EN
    other = bs - OW - NE - EN
    if ow:
        miss = OW - ow
        if len(ow) >= 40: parts.append(f"quasi tutto l'Overworld ({len(ow)}/{len(OW)}; manca: {', '.join(sorted(bname(b) for b in miss)) or '-'})")
        else: parts.append("Overworld: " + ", ".join(sorted(bname(b) for b in ow)))
    if ne: parts.append("Nether: " + ", ".join(sorted(bname(b) for b in ne)))
    if en: parts.append("End: " + ", ".join(sorted(bname(b) for b in en)))
    if other: parts.append("altri: " + ", ".join(sorted(other)))
    return "; ".join(parts)

SNAME = [("minecraft:trial_chambers", "Trial Chambers"), ("minecraft:fortress", "Fortezza del Nether (DnT)"), ("minecraft:nether_fortress", "Fortezza del Nether (DnT)"),
         ("mns:", "Moog's Nether Structures"), ("minecraft:stronghold", "Stronghold (DnT)"), ("nova_structures:jungle_ruin", "Jungle Temple (DnT)"),
         ("nova_structures:desert_ruin", "Desert Temple (DnT)"), ("nova_structures:trident_trial", "Ocean Monument (DnT)"), ("minecraft:swamp_hut", "Swamp Hut (DnT)"),
         ("minecraft:witch_hut", "Swamp Hut (DnT)"), ("minecraft:illager_mansion", "Woodland Mansion (DnT Illager Manor)"), ("minecraft:pillager_outpost", "Pillager Outpost"),
         ("minecraft:bastion", "Bastion Remnant"), ("minecraft:igloo", "Igloo"), ("minecraft:village", "Villaggi abbandonati (ISO)"), ("philipsruins:", "Philips' Ruins"),
         ("adventuredungeons:", "Adventure Dungeons"), ("hellish_trials:", "Hellish Trials"), ("incendium:", "Incendium"), ("formationsnether:", "Formations Nether"),
         ("immersive_gateways:", "Immersive Gateways"), ("minecraft:abandoned_camp", "Abandoned Camp (VB)"), ("minecraft:ancient_city", "Ancient City (DnT)"),
         ("minecraft:end_city", "End City"), ("minecraft:ocean_ruin", "Ocean Ruins"), ("minecraft:woodland_mansion", None), ("supplementaries:galleon", None),
         ("abridged:pillager_infested", None), ("incubation:village", None), ("moogs_structures:", "Moog's Structure Lib")]
VILLAGE_OK = {"minecraft:zombie_villager"}
def sname(k):
    for p, n in SNAME:
        if k.startswith(p): return n
    return k
def structures(e):
    out = {}
    for s in sstruct.get(e, []):
        out.setdefault(sname(s.split(" ")[0]), set()).add("spawn naturale")
    for k, kinds in nbt.get(e, {}).items():
        n = sname(k)
        if n is None or (n.startswith("Villaggi") and e not in VILLAGE_OK): continue
        for kd in kinds:
            out.setdefault(n, set()).add({"placed": "piazzato", "spawner": "spawner", "trial": "trial spawner"}[kd.split("@")[0]])
    return "; ".join(f"{n} ({', '.join(sorted(v))})" for n, v in sorted(out.items(), key=lambda x: str(x[0])) if n) or None

def foods(e):
    short = e.split(":")[1]
    res = []
    for t, v in itags.items():
        leaf = t.split(":")[1].split("/")[-1]
        if leaf in (short + "_food", short + "_tempt_items", short + "_breeding_items", short + "_temptations", short + "_food_items", short + "_breeding_food", short + "_tempt"):
            items = ", ".join(i.split(":")[1] if i.startswith("minecraft:") else i for i in v["items"][:10]) + (" ..." if len(v["items"]) > 10 else "")
            src = v["from"][-1].split("-")[0].split("[")[0] if v["from"] else "?"
            res.append(f"`{t}` = {items} (ultimo: {src})")
    return res

out = ["# Matrice mob × mod — SurvivalReimagined4", "",
       "Generata da `tools/emi_mobs/run.sh` (dati del pack: tag, biomi, strutture, config) più le note manuali in `tools/emi_mobs/extras.py`: non modificare questo file a mano, modifica `extras.py` e rigenera. `?` = da verificare. "
       "**OFF** = il mob è nel tag ma la feature è spenta o azzerata da config.", "",
       "## Comportamenti generici (non ripetuti per ogni mob)", "",
       "Questi valgono per quasi tutti i mob e nella matrice sono solo una sigla accanto al nome:", "",
       "- **T** (Enhanced AI Targeting): ti sentono attraverso i muri a corto raggio, ti seguono da più lontano, avvisano i vicini.",
       "- **X** (Enhanced AI): scappano da Creeper innescati e TNT, vanno nel panico se in fiamme, rompono barche e minecart per scappare.",
       "- **S** (MPR di Enhanced AI `speed_bonus`/`outside_nerf`): più veloci (meno all'aperto di giorno senza luna piena), nuotano più veloci, all'aperto ti seguono da meno lontano.",
       "- **D** (MPR di Enhanced AI `deepness_buff`): nelle grotte dell'Overworld hanno più vita e ti sentono da più lontano, crescendo con la profondità.",
       "- **A** (Enhanced AI animali): a volte reagiscono o sono ostili, a volte scappano dai giocatori, il branco scappa se uno viene colpito, metà non segue il cibo.",
       "- ISO (tutti i mostri): equipaggiamento droppato il 50% delle volte e mai integro; spawn possibile anche vicino allo spawn del mondo; niente spawn vicino a una Echo Lantern; gli spawner ignorano la luce e partono con una raffica (vedi CLAUDE.md); i non-morti bruciano alla luce del sole anche sotto un blocco (`Burn in sky light`).",
       "- Enhanced AI: i mostri spariscono solo più lontano; mob cramming ridotto (ISO).",
       "", "## Decisioni (2026-11-26)", "",
       "- Pagine EMI sulle uova, una per mob, nel pack (`resourcepacks/survivalreimagined_lang`), anche per il comportamento delle mod di Insane96. Niente drop; sempre dove si trova.",
       "- I comportamenti generici qui sopra **non** si scrivono nelle pagine: solo quelli distintivi del mob.",
       "- Le meccaniche degli oggetti (Cage, Jar, Flute, guinzaglio, frecce con effetto) vanno sulle pagine degli oggetti, non ripetute sulle uova.",
       "- Le voci `?` che non si chiariscono dal codice le controlla l'utente in gioco.", ""]
unknown = set()
for title, mobs in GROUPS:
    out += [f"## {title}", ""]
    if title == "Naturalist":
        out += ["Il comportamento proprio di Naturalist (cosa mangiano, chi cacciano, abitudini) lo ricavo dal codice della mod in fase di scrittura. "
                "Modifiche del pack: esclusi da `enhancedai:speed_bonus` (quindi niente sigla S), carne ridotta (drop esclusi dalle pagine), cibi crudi in `raw_foods`.", ""]
    for e in mobs:
        tg = etags.get(e, [])
        gen = sorted({GEN_LABEL[t] for t in tg if t in GEN_LABEL})
        out.append(f"### {nm(e)} (`{e}`){'  · ' + ' '.join(gen) if gen else ''}")
        b = dict(spawns.get(e, {}))
        if e in ("minecraft:fox", "minecraft:rabbit"): b.update(spawns.get(e + "(naturalist)", {}))
        if e == "naturalist:snake": b.update(spawns.get("naturalist:coral_snake", {})); b.update(spawns.get("naturalist:rattlesnake", {}))
        sm = summarize(b.keys())
        st = structures(e)
        out.append(f"- **Dove (biomi)**: {sm or '—'}")
        if st: out.append(f"- **Strutture**: {st}")
        if e in ex.DOVE: out.append(f"- **Altre fonti**: {ex.DOVE[e]}")
        feats, offs = {}, []
        for t in tg:
            if t in GENERIC: continue
            if t in T:
                src, txt = T[t]
                if src == "OFF": offs.append(txt); continue
                if txt: feats.setdefault(src, []).append(txt)
            elif t.split(":")[0] in ("enhancedai", "insanesurvivaloverhaul", "supplementaries"):
                unknown.add(t)
        for src, txt in ex.E.get(e, []):
            if src or txt: feats.setdefault(src, []).append(txt)
        for src in sorted(feats, key=lambda s: (not s.startswith("ISO"), not s.startswith("EAI"), s)):
            txt = "; ".join(x for x in feats[src] if x)
            out.append(f"- {src}: {txt}" if txt else f"- {src}")
        if offs: out.append(f"- **OFF**: {'; '.join(offs)}")
        fd = foods(e)
        if fd: out.append(f"- **Cibo (tag)**: {' · '.join(fd)}")
        out.append("")
open(dest, "w", encoding="utf-8").write("\n".join(out))
print("written", dest, "unknown tags:", sorted(unknown))
