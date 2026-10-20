# Exercice 2 : Cinemax #2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# Boucle sur le dictionnaire "family" pour calculer le coût total des billets :
#   - moins de 3 ans : gratuit
#   - 3 à 12 ans : $10
#   - plus de 12 ans : $15
# Affiche le prix du billet pour chaque membre, puis le total à la fin.

# Bonus : demande à l'utilisateur les noms/âges des membres, puis calcule le total.
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
