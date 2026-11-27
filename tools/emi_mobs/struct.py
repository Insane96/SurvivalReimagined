"""Structure spawn_overrides per entity (last definition wins) + entities named in structure templates/jigsaw json
(e.g. DnT spawners, Moonlight spawn_boxes) as a hint.
Usage: python -I struct.py <instance_dir> <out_json>"""
import json, os, re, sys, zipfile, glob
inst, out = sys.argv[1], sys.argv[2]
cf = os.path.abspath(os.path.join(inst, "..", ".."))
srcs = [("minecraft", os.path.join(cf, "Install", "versions", "1.21.1", "1.21.1.jar"))] + \
       [(os.path.basename(j), j) for j in sorted(glob.glob(os.path.join(inst, "mods", "*.jar")))]
RE = re.compile(r"^data/([^/]+)/worldgen/structure/(.+)\.json$")
defs = {}
def handle(label, rid, raw):
    try:
        d = json.loads(raw)
    except Exception:
        return
    defs[rid] = (label, d)
for label, p in srcs:
    try:
        z = zipfile.ZipFile(p)
    except Exception:
        continue
    for n in z.namelist():
        m = RE.match(n)
        if m:
            handle(label, m.group(1) + ":" + m.group(2), z.read(n).decode("utf-8", "replace"))
dp = os.path.join(inst, "datapacks", "survivalreimagined")
for root, _, fs in os.walk(dp):
    for f in fs:
        rel = os.path.relpath(os.path.join(root, f), dp).replace("\\", "/")
        m = RE.match(rel)
        if m:
            handle("datapack", m.group(1) + ":" + m.group(2), open(os.path.join(root, f), encoding="utf-8").read())
per = {}
for rid, (label, d) in defs.items():
    for cat, ov in (d.get("spawn_overrides") or {}).items():
        for s in ov.get("spawns", []):
            per.setdefault(s["type"], []).append(f"{rid} ({cat}, {ov.get('bounding_box')}, {label[:25]})")
json.dump(per, open(out, "w"), indent=1)
for e, v in sorted(per.items()):
    print(e, "->", "; ".join(v))
