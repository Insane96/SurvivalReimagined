"""Scan structure templates (.nbt) of vanilla, mods and datapacks for mobs placed as entities or in spawners/trial spawners.
Usage: python -I nbtscan.py <instance_dir> <out_json>"""
import gzip, io, json, os, re, struct, sys, zipfile, glob

def read_nbt(b):
    f = io.BytesIO(b)
    def rd(n): return f.read(n)
    def s():
        (l,) = struct.unpack(">H", rd(2)); return rd(l).decode("utf-8", "replace")
    def payload(t):
        if t == 1: return struct.unpack(">b", rd(1))[0]
        if t == 2: return struct.unpack(">h", rd(2))[0]
        if t == 3: return struct.unpack(">i", rd(4))[0]
        if t == 4: return struct.unpack(">q", rd(8))[0]
        if t == 5: return struct.unpack(">f", rd(4))[0]
        if t == 6: return struct.unpack(">d", rd(8))[0]
        if t == 7: (n,) = struct.unpack(">i", rd(4)); rd(n); return None
        if t == 8: return s()
        if t == 9:
            et = rd(1)[0]; (n,) = struct.unpack(">i", rd(4)); return [payload(et) for _ in range(n)]
        if t == 10:
            d = {}
            while True:
                tt = rd(1)[0]
                if tt == 0: return d
                k = s(); d[k] = payload(tt)
        if t == 11: (n,) = struct.unpack(">i", rd(4)); rd(4 * n); return None
        if t == 12: (n,) = struct.unpack(">i", rd(4)); rd(8 * n); return None
        raise ValueError(t)
    t = rd(1)[0]; s(); return payload(t)

def ids_in(o, acc):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == "id" and isinstance(v, str):
                acc.add(v)
            else:
                ids_in(v, acc)
    elif isinstance(o, list):
        for v in o: ids_in(v, acc)

inst, out = sys.argv[1], sys.argv[2]
cf = os.path.abspath(os.path.join(inst, "..", ".."))
srcs = [("minecraft", os.path.join(cf, "Install", "versions", "1.21.1", "1.21.1.jar"))] + \
       [(os.path.basename(j), j) for j in sorted(glob.glob(os.path.join(inst, "mods", "*.jar")))] + \
       [(os.path.basename(z), z) for z in glob.glob(os.path.join(inst, "datapacks", "*.zip"))]
RE = re.compile(r"^data/([^/]+)/structures?/(.+)\.nbt$")
res = {}  # entity -> {template_folder: kinds}
def handle(label, ns, path, raw):
    try:
        n = read_nbt(gzip.decompress(raw))
    except Exception:
        return
    folder = ns + ":" + "/".join(path.split("/")[:2])
    found = []
    for e in n.get("entities", []) or []:
        i = (e.get("nbt") or {}).get("id")
        if i: found.append((i, "placed"))
    palette = n.get("palette") or (n.get("palettes") or [[]])[0]
    for b in n.get("blocks", []) or []:
        nb = b.get("nbt")
        if not nb: continue
        bid = nb.get("id") or (palette[b["state"]].get("Name", "") if palette and b.get("state", -1) < len(palette) else "")
        if bid in ("minecraft:mob_spawner", "minecraft:spawner", "minecraft:trial_spawner") or "spawner" in bid:
            acc = set(); ids_in({k: v for k, v in nb.items() if k != "id"}, acc)
            kind = "trial" if "trial" in bid else "spawner"
            for i in acc: found.append((i, kind))
    for i, k in found:
        res.setdefault(i, {}).setdefault(folder, set()).add(k + ("" if label in ("minecraft",) else f"@{label[:22]}"))
for label, p in srcs:
    try: z = zipfile.ZipFile(p)
    except Exception: continue
    for nm in z.namelist():
        m = RE.match(nm)
        if m: handle(label, m.group(1), m.group(2), z.read(nm))
dp = os.path.join(inst, "datapacks", "survivalreimagined")
for root, _, fs in os.walk(dp):
    for f in fs:
        rel = os.path.relpath(os.path.join(root, f), dp).replace("\\", "/")
        m = RE.match(rel)
        if m: handle("datapack", m.group(1), m.group(2), open(os.path.join(root, f), "rb").read())
json.dump({e: {k: sorted(v) for k, v in d.items()} for e, d in sorted(res.items())}, open(out, "w"), indent=1)
for e, d in sorted(res.items()):
    if ":" in e and not e.startswith("minecraft:item"):
        print(e, "->", "; ".join(f"{k}({','.join(sorted(v))})" for k, v in sorted(d.items()))[:700])
