"""Clean raw/schools.csv -> clean/schools.csv (strip spaces, Title Case names, drop rows with no student count)."""
import csv

with open("raw/schools.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

out = []
for r in rows:
    if not r["students"].strip():
        continue
    out.append({
        "school_id": r["school_id"].strip(),
        "name": r["name"].strip().title(),
        "district": r["district"].strip(),
        "students": int(r["students"]),
    })

with open("clean/schools.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["school_id", "name", "district", "students"], lineterminator="\n")
    w.writeheader()
    w.writerows(out)
print(f"{len(out)} rows written ({len(rows) - len(out)} dropped)")
