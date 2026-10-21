# ============================================================
# Day 3 - Dictionaries : Exercises XP (regroupé)
# ============================================================

# --- Exercice 1 : Converting Lists into Dictionaries ---
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionnary = dict(zip(keys, values))

print(dictionnary)


# --- Exercice 2 : Cinemax #2 ---
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total = 0

for nom, age in family.items():
    if age < 3:
        print(f"gratuit pour {nom}")
    elif age <= 12:
        print(f"le prix pour {nom} est de 10$")
        total += 10
    else:
        print(f"le prix pour {nom} est de 15$")
        total += 15

print(f"Total: ${total}")


# --- Exercice 3 : Zara ---
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2
brand["country_creation"] = "Spain"
print(f"Zara sells clothes for {brand['type_of_clothes']}")

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand['creation_date']
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys())


# --- Exercice 4 : Disney Characters ---
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

dico1 = {}
for position, disney in enumerate(users):
    dico1[disney] = position

dico2 = {}
for position, disney in enumerate(users):
    dico2[position] = disney

dico3 = {}
for position, disney in enumerate(sorted(users)):
    dico3[disney] = position

print(dico1)
print(dico2)
print(dico3)
