# ============================================================
# Daily Challenge : Lists & Strings  (Day 2)
# ============================================================
# Ce que tu vas apprendre : Python Basics, Loops, Lists, Strings
#
# ------------------------------------------------------------
# CHALLENGE 1 : Multiples of a Number
# ------------------------------------------------------------
# 1. Demande à l'utilisateur DEUX inputs :
#      - un nombre (integer)
#      - une longueur (integer)
# 2. Génère une liste de multiples de ce nombre.
# 3. La liste s'arrête quand elle atteint la longueur demandée.
#
# Exemple 1 :
#   number: 7  /  length: 5   ->  [7, 14, 21, 28, 35]
# Exemple 2 :
#   number: 12 /  length: 10  ->  [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
# Exemple 3 :
#   number: 17 /  length: 6   ->  [17, 34, 51, 68, 85, 102]
#
# ------------------------------------------------------------
# CHALLENGE 2 : Remove Consecutive Duplicate Letters
# ------------------------------------------------------------
# 1. Demande à l'utilisateur un mot (string).
# 2. Enlève les lettres identiques qui se suivent (consécutives).
#    La nouvelle string ne garde que les lettres consécutives uniques.
#    Ex : "ppoeemm"  ->  "poem"   (supprime 'pp', 'ee', 'mm')
# 3. Affiche le mot modifié.
#
# Exemples :
#   "ppoeemm"         ->  "poem"
#   "wiiiinnnnd"      ->  "wind"
#   "ttiiitllleeee"   ->  "title"
#   "cccccaaarrrbbonnnnn"  ->  "carbon"
#
# NOTE : les doublons NON consécutifs sont autorisés.
# Ex : dans "recursive", les deux 'r' et les deux 'e' sont gardés
#      car ils ne sont pas l'un à côté de l'autre.
# ============================================================
number = int(input("Give a number"))
length = int(input("Give a length")) 
number_list = []

range1 = range(1,length+1)
for i in range1:
    number_list.append(number*i)

print(number_list)


# ---------------- CHALLENGE 2 ----------------
word = input("Give a word: ")
result = ""

previous = ""              # la lettre qu'on vient de voir
for letter in word:
    if letter != previous:  # si elle diffère de la précédente...
        result += letter    # ...on la garde
    previous = letter       # on mémorise la lettre courante

print(result)
