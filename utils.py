import csv

def load_providers():
    providers = []
    with open("data/solar_providers.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            providers.append(row)
    return providers
