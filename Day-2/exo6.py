# Exercice 6 : While Loop
# 1. Utilise un input pour demander à l'utilisateur son nom
# 2. Avec une boucle "while True", vérifie que l'utilisateur a donné un vrai nom
#    (pas des chiffres, et au moins 3 lettres)
#    Indice : utilise la méthode isdigit()
# 3. Si l'entrée est incorrecte, continue de demander jusqu'à ce qu'elle soit correcte
# 4. Si l'entrée est correcte, affiche "thank you" et sors de la boucle (break)
while True:
    name = input("Quel est ton nom ? ")

    if len(name)>=3 and not name.isdigit():
        print("thank you")
        break
