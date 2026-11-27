"""Print every option of a TOML config with its comment and value: [section] key = value  # comment
Usage: python -I cfgdesc.py <toml> [section_regex]"""
import re, sys
path = sys.argv[1]
flt = re.compile(sys.argv[2]) if len(sys.argv) > 2 else None
section, comment = "", []
for line in open(path, encoding="utf-8"):
    s = line.strip()
    if not s:
        comment = []
        continue
    if s.startswith("#"):
        c = s.lstrip("#").strip()
        if not c.startswith(("Default:", "Range:", "Allowed Values:")):
            comment.append(c)
        continue
    if s.startswith("["):
        section = s
        comment = []
        continue
    if flt and not flt.search(section + " " + s):
        comment = []
        continue
    print(f"{section} {s}" + (f"  # {' '.join(comment)}" if comment else ""))
    comment = []
