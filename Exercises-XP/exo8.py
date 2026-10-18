# Exercise 8 : What's your name ?
# 1. Demande son nom à l'utilisateur (input)
# 2. Si c'est le même nom que le tien, affiche un message drôle

name = input("What's your name")

if name.title() == "Nathan":
    print("You just met your clone")
else :
    print("We are not meant to be friends")