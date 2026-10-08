#!/usr/bin/env bash
set -euo pipefail
out=$(python facts.py)
[ "$out" = "Largest ward: Test Ward Four (2310 people)" ] || { echo "unexpected: $out"; exit 1; }
python - <<'PY'
import sqlite3
c = sqlite3.connect(":memory:")
c.executescript(open("schema.sql").read())
rows = c.execute("SELECT SUM(population) FROM wards").fetchone()[0]
assert rows == 6210, rows
top = c.execute("SELECT ward_name, population FROM wards ORDER BY population DESC LIMIT 1").fetchone()
assert top == ("Test Ward Four", 2310), top
PY
echo "g09 ok"
