# Exercice 4 : Disney Characters
# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# Crée 3 dictionnaires :
# 1. caractère -> index     : {"Mickey": 0, "Minnie": 1, "Donald": 2, ...}
# 2. index -> caractère     : {0: "Mickey", 1: "Minnie", 2: "Donald", ...}
# 3. caractères triés par ordre alphabétique -> index :
#    {"Ariel": 0, "Donald": 1, "Mickey": 2, ...}

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
