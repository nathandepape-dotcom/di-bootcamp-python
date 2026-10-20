# Exercice 4 : Floats
# Rappel : c'est quoi un float ? Quelle est la différence entre un float et un int ?
# Crée une liste contenant cette séquence (mix de floats et d'entiers) :
#   1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5
# Évite de taper chaque nombre à la main.
# Réfléchis : peux-tu générer cette séquence avec une boucle ou une autre méthode ?



seq = []

for i in range(3,11):
    seq.append(i/2)


print(seq)

