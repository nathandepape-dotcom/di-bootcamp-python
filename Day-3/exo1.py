# Exercice 1 : Converting Lists into Dictionaries
# On te donne deux listes :
#   keys = ['Ten', 'Twenty', 'Thirty']
#   values = [10, 20, 30]
# Convertis-les en un dictionnaire :
#   la 1ère liste = les clés, la 2e liste = les valeurs
# Résultat attendu : {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionnary = dict(zip(keys, values))  

print(dictionnary)


