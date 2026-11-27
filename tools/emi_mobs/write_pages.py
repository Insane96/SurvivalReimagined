"""Write EMI info pages for spawn eggs and their lang keys (idempotent: existing keys are replaced in place).
Usage: python -I write_pages.py <assets_dir> <batch_module.py>"""
import json, os, re, sys, runpy

assets, batch = sys.argv[1], sys.argv[2]
B = runpy.run_path(batch)
SHARED, PAGES = B.get("SHARED", {}), B["PAGES"]

lang_path = os.path.join(assets, "survivalreimagined", "lang", "en_us.json")
raw = open(lang_path, encoding="utf-8").read()
lang = json.loads(raw)
lines = raw.rstrip().rstrip("}").rstrip().split("\n")

new = {}
for k, v in SHARED.items():
    new["emi.info.survivalreimagined.mob." + k] = v
for (ns, mob), (texts, shared) in PAGES.items():
    keys = []
    base = f"emi.info.{ns}.{mob}_spawn_egg"
    for i, t in enumerate(texts):
        k = base if len(texts) == 1 else f"{base}.{i + 1}"
        new[k] = t
        keys.append(k)
    keys += ["emi.info.survivalreimagined.mob." + s for s in shared]
    for s in shared:
        assert "emi.info.survivalreimagined.mob." + s in new or "emi.info.survivalreimagined.mob." + s in lang, s
    page = {"type": "emi:info", "stacks": [f"item:{ns}:{mob}_spawn_egg"], "text": keys}
    with open(os.path.join(assets, "emi", "recipe", "additions", f"{ns}_{mob}_spawn_egg.json"), "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(page, indent=4, ensure_ascii=False) + "\n")

def entry(k, v):
    return "\t" + json.dumps(k, ensure_ascii=False) + ": " + json.dumps(v, ensure_ascii=False)

key_re = re.compile(r'^\t"([^"]+)":')
idx = {}
for i, l in enumerate(lines):
    m = key_re.match(l)
    if m:
        idx[m.group(1)] = i
for k, v in new.items():
    if k in idx:
        comma = lines[idx[k]].endswith(",")
        lines[idx[k]] = entry(k, v) + ("," if comma else "")
    else:
        if not lines[-1].endswith(","):
            lines[-1] += ","
        lines.append(entry(k, v))
        idx[k] = len(lines) - 1
out = "\n".join(lines) + "\n}\n"
json.loads(out)
open(lang_path, "w", encoding="utf-8", newline="\n").write(out)
print(len(PAGES), "pages,", len(new), "keys")
