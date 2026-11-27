"""Write Field Guide mob descriptions as lang keys (idempotent: existing keys are replaced in place, new ones appended).
Each mob gets one key, fieldguide.<ns>.<mob>.description: its texts followed by its shared texts, as paragraphs (\\n\\n).
Shared texts can be defined in any batch, so pass every batch in one call.
Usage: python -I write_pages.py <assets_dir> <batch_module.py> [<batch_module.py> ...]"""
import json, os, re, sys, runpy

assets, batches = sys.argv[1], [runpy.run_path(b) for b in sys.argv[2:]]
SHARED = {}
for B in batches:
    SHARED.update(B.get("SHARED", {}))

lang_path = os.path.join(assets, "survivalreimagined", "lang", "en_us.json")
raw = open(lang_path, encoding="utf-8").read()
json.loads(raw)
lines = raw.rstrip().rstrip("}").rstrip().split("\n")

new = {}
for B in batches:
    for (ns, mob), (texts, shared) in B["PAGES"].items():
        key = f"fieldguide.{ns}.{mob}.description"
        assert key not in new, key
        new[key] = "\n\n".join(texts + [SHARED[s] for s in shared])

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
print(len(new), "mobs")
