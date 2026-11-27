"""Collect the pack's data (vanilla + NeoForge + mod jars + enabled integrated packs + datapack) and resolve:
entity_type/item/biome tags, biome spawns (biome json spawners + neoforge add/remove_spawns + Naturalist add_animals).
Usage: python -I data.py <instance_dir> <out_dir>"""
import json, os, re, sys, zipfile, glob

inst, outd = sys.argv[1], sys.argv[2]
cf = os.path.abspath(os.path.join(inst, "..", ".."))
VANILLA = os.path.join(cf, "Install", "versions", "1.21.1", "1.21.1.jar")
NEO = os.path.join(cf, "Install", "libraries", "net", "neoforged", "neoforge", "21.1.265", "neoforge-21.1.265-universal.jar")
SKIP_PACKS = {"insanesurvivaloverhaul": {"echo_pillar", "farmable_iron", "nether_tweaks"},
              "progressivebosses": {"endergetic_integration"},
              "insanelib": None}  # None = skip all
PATH_RE = re.compile(r"^(?:integrated_packs/([^/]+)/)?data/([^/]+)/(.+)\.json$")

files = {}  # (ns, path) -> list of (label, data) in load order (last wins for non-tags)

def add(label, ns, path, raw):
    try:
        data = json.loads(raw)
    except Exception:
        return
    files.setdefault((ns, path), []).append((label, data))

def want(path):
    return path.startswith(("tags/entity_type", "tags/item/", "tags/worldgen/biome/", "worldgen/biome/", "neoforge/biome_modifier/"))

def scan_zip(p, label):
    try:
        z = zipfile.ZipFile(p)
    except Exception:
        return
    for n in z.namelist():
        m = PATH_RE.match(n)
        if not m or not want(m.group(3)):
            continue
        pack = m.group(1)
        if pack:
            skip = next((v for k, v in SKIP_PACKS.items() if label.lower().startswith(k)), "none")
            if skip is None or (skip != "none" and pack in skip):
                continue
        add(label + (f"[{pack}]" if pack else ""), m.group(2), m.group(3), z.read(n).decode("utf-8", "replace"))

scan_zip(VANILLA, "minecraft")
scan_zip(NEO, "neoforge")
for j in sorted(glob.glob(os.path.join(inst, "mods", "*.jar"))):
    scan_zip(j, os.path.basename(j))
dp = os.path.join(inst, "datapacks", "survivalreimagined")
for root, _, fs in os.walk(dp):
    for f in fs:
        rel = os.path.relpath(os.path.join(root, f), dp).replace("\\", "/")
        m = PATH_RE.match(rel)
        if m and want(m.group(3)):
            add("datapack", m.group(2), m.group(3), open(os.path.join(root, f), encoding="utf-8").read())

def build_tags(prefix):
    tags = {}
    for (ns, path), entries in files.items():
        if not path.startswith(prefix):
            continue
        tid = ns + ":" + path[len(prefix):]
        t = tags.setdefault(tid, {"values": [], "remove": [], "from": []})
        for label, d in entries:
            if d.get("replace"):
                t["values"], t["remove"] = [], []
            t["from"].append(label + ("(replace)" if d.get("replace") else ""))
            t["values"] += [v["id"] if isinstance(v, dict) else v for v in d.get("values", [])]
            t["remove"] += [v["id"] if isinstance(v, dict) else v for v in d.get("remove", [])]
    cache = {}
    def resolve(tid, stack=()):
        if tid in cache:
            return cache[tid]
        if tid in stack or tid not in tags:
            return set()
        r = set()
        for v in tags[tid]["values"]:
            r |= resolve(v[1:], stack + (tid,)) if v.startswith("#") else {v}
        for v in tags[tid]["remove"]:
            r -= resolve(v[1:], stack + (tid,)) if v.startswith("#") else {v}
        cache[tid] = r
        return r
    return tags, resolve

etags, eres = build_tags("tags/entity_type/")
itags, ires = build_tags("tags/item/")
btags, bres = build_tags("tags/worldgen/biome/")

def biomes_of(spec):
    if isinstance(spec, str):
        return bres(spec[1:]) if spec.startswith("#") else {spec}
    if isinstance(spec, list):
        r = set()
        for s in spec:
            r |= biomes_of(s)
        return r
    if isinstance(spec, dict) and spec.get("type") == "neoforge:any":  # rare
        return biomes_of(spec.get("values", []))
    return set()

# biome spawners: biome -> {entity: category}
biome_spawns = {}
biome_src = {}
for (ns, path), entries in files.items():
    if path.startswith("worldgen/biome/"):
        label, d = entries[-1]
        b = ns + ":" + path[len("worldgen/biome/"):]
        biome_src[b] = label
        sp = biome_spawns.setdefault(b, {})
        for cat, lst in (d.get("spawners") or {}).items():
            for s in lst:
                sp[s["type"]] = cat

mods_log = []
for (ns, path), entries in sorted(files.items()):
    if not path.startswith("neoforge/biome_modifier/"):
        continue
    label, d = entries[-1]  # last one wins (datapack overrides)
    rid = ns + ":" + path[len("neoforge/biome_modifier/"):]
    t = d.get("type")
    if t == "neoforge:add_spawns":
        sps = d["spawners"] if isinstance(d["spawners"], list) else [d["spawners"]]
        bs = biomes_of(d.get("biomes"))
        for b in bs:
            for s in sps:
                biome_spawns.setdefault(b, {})[s["type"]] = "added:" + rid
        mods_log.append((rid, label, t, [s["type"] for s in sps], d.get("biomes")))
    elif t == "neoforge:remove_spawns":
        ents = d["entity_types"]
        es = eres(ents[1:]) if isinstance(ents, str) and ents.startswith("#") else ({ents} if isinstance(ents, str) else set(ents))
        bs = biomes_of(d.get("biomes"))
        for b in bs:
            for e in es:
                biome_spawns.get(b, {}).pop(e, None)
        mods_log.append((rid, label, t, sorted(es), d.get("biomes")))
    elif t == "naturalist:add_animals":
        mods_log.append((rid, label, t, [], None))

# Naturalist: naturalist:has_<x> minus naturalist:blacklist/blacklist_<x>
NAT = {"bluejay": "naturalist:bird", "canary": "naturalist:bird", "cardinal": "naturalist:bird", "finch": "naturalist:bird",
       "robin": "naturalist:bird", "sparrow": "naturalist:bird", "coral_snake": "naturalist:coral_snake",
       "rattlesnake": "naturalist:rattlesnake", "forest_foxes": "minecraft:fox(naturalist)", "forest_rabbits": "minecraft:rabbit(naturalist)",
       "ant_hill": None}
for tid in list(btags):
    if tid.startswith("naturalist:has_"):
        x = tid[len("naturalist:has_"):]
        ent = NAT.get(x, "naturalist:" + x)
        if ent is None:
            continue
        bs = bres(tid) - bres("naturalist:blacklist/blacklist_" + x)
        for b in bs:
            biome_spawns.setdefault(b, {})[ent] = "naturalist:" + x

per_entity_biomes = {}
for b, sp in biome_spawns.items():
    for e, c in sp.items():
        per_entity_biomes.setdefault(e, {})[b] = c

per_entity_tags = {}
for t in etags:
    for e in eres(t):
        per_entity_tags.setdefault(e, []).append(t)

os.makedirs(outd, exist_ok=True)
json.dump({e: sorted(v) for e, v in per_entity_tags.items()}, open(os.path.join(outd, "entity_tags.json"), "w"), indent=1)
json.dump({t: {"entities": sorted(eres(t)), "from": etags[t]["from"]} for t in sorted(etags)}, open(os.path.join(outd, "entity_tag_defs.json"), "w"), indent=1)
json.dump({t: {"items": sorted(ires(t)), "from": itags[t]["from"]} for t in sorted(itags)}, open(os.path.join(outd, "item_tags.json"), "w"), indent=1)
json.dump({e: dict(sorted(v.items())) for e, v in sorted(per_entity_biomes.items())}, open(os.path.join(outd, "spawn_biomes.json"), "w"), indent=1)
json.dump(mods_log, open(os.path.join(outd, "biome_modifiers.json"), "w"), indent=1)
json.dump(biome_src, open(os.path.join(outd, "biomes.json"), "w"), indent=1)
json.dump({t: sorted(bres(t)) for t in btags}, open(os.path.join(outd, "biome_tags.json"), "w"), indent=1)
print(len(etags), "entity tags,", len(itags), "item tags,", len(btags), "biome tags,", len(biome_spawns), "biomes,", len(per_entity_biomes), "spawning entities")
