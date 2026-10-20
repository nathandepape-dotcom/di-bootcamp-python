# Exercice 9 : Cinemax Tickets
# 1. Demande l'âge de chaque personne de la famille qui veut un billet de cinéma
# 2. Calcule le coût total selon ces règles :
#    - Gratuit pour les moins de 3 ans
#    - $10 pour les 3 à 12 ans
#    - $15 pour les plus de 12 ans
# 3. Affiche le coût total des billets

# Bonus :
# Un groupe d'ados veut voir un film interdit (réservé aux 16-21 ans).
# - Demander l'âge de chaque personne
# - Retirer ceux qui n'ont pas le droit
# - Afficher la liste finale des participants
price = 0

while True:
    age=input("Give me the age of each family member one by one (say 'Quit' when you're done)")
    if age == "Quit":
        break

    response=int(age)
    if response < 3:
        pass
    elif response <= 12:
        price += 10
    else:
        price += 15

    
print((f"Total cost : {price}"))


