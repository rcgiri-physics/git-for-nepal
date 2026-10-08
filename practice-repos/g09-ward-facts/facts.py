"""Answer a question about the (synthetic) ward table."""
import csv


def load(path="data/wards.csv"):
    with open(path, newline="", encoding="utf-8") as f:
        return [
            {**row, "population": int(row["population"]), "households": int(row["households"])}
            for row in csv.DictReader(f)
        ]


def largest_ward(wards):
    return max(wards, key=lambda w: w["population"])


if __name__ == "__main__":
    wards = load()
    top = largest_ward(wards)
    print(f"Largest ward: {top['ward_name']} ({top['population']} people)")
