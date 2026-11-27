#!/usr/bin/env bash
# Regenerates EMI_MOB_MATRICE.md from the pack's data. Run from anywhere: bash tools/emi_mobs/run.sh
# Needs the CurseForge install next to the instance (Install/versions/1.21.1, NeoForge 21.1.265 in Install/libraries).
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
INST="$(cd "$HERE/../.." && pwd)"
OUT="$HERE/out"
python -I "$HERE/data.py" "$INST" "$OUT"
python -I "$HERE/struct.py" "$INST" "$OUT/structure_spawns.json" > /dev/null
python -I "$HERE/nbtscan.py" "$INST" "$OUT/nbt_mobs.json" > "$OUT/nbt_mobs.txt"
python -I "$HERE/matrix.py" "$OUT" "$INST" "$INST/EMI_MOB_MATRICE.md"
# EMI pages (one file per batch): python -I "$HERE/write_pages.py" "$INST/resourcepacks/survivalreimagined_lang/assets" "$HERE/pages_<batch>.py"
