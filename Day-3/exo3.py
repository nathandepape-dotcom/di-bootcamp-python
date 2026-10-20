# Exercice 3 : Zara
# Crée un dictionnaire "brand" avec ces infos :
#   name: Zara
#   creation_date: 1975
#   creator_name: Amancio Ortega Gaona
#   type_of_clothes: men, women, children, home
#   international_competitors: Gap, H&M, Benetton
#   number_stores: 7000
#   major_color: France: blue, Spain: red, US: pink, green
# Puis :
# 1. Change number_stores à 2
# 2. Affiche une phrase sur les clients (avec type_of_clothes)
# 3. Ajoute country_creation = "Spain"
# 4. Si international_competitors existe, ajoute "Desigual" à la liste
# 5. Supprime la clé creation_date
# 6. Affiche le DERNIER élément de international_competitors
# 7. Affiche les couleurs majeures aux US
# 8. Affiche le nombre de clés du dictionnaire
# 9. Affiche toutes les clés du dictionnaire

# Bonus : crée un dict "more_on_zara" avec creation_date et number_stores,
# puis fusionne-le avec "brand" et affiche le résultat



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