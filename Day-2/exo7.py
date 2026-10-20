# Exercice 7 : Favorite Fruits
# 1. Demande à l'utilisateur ses fruits favoris (plusieurs fruits, séparés par des espaces)
# 2. Stocke ces fruits dans une liste
# 3. Demande à l'utilisateur le nom d'un fruit
# 4. Si ce fruit est dans sa liste de favoris, affiche :
#    "You chose one of your favorite fruits! Enjoy!"
# 5. Sinon, affiche :
#    "You chose a new fruit. I hope you enjoy it!"

fruits = input("Put your favorite fruits : ").split()

fruit = input("Put a fruit that you want to eat : ")

if fruit in fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
