# Exercice 3 : List Manipulation
# Tu as une liste : basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# 1. Retire "Banana" de la liste
# 2. Retire "Blueberries" de la liste
# 3. Ajoute "Kiwi" à la fin de la liste
# 4. Ajoute "Apples" au début de la liste
# 5. Compte combien de fois "Apples" apparaît dans la liste
# 6. Vide la liste
# 7. Affiche l'état final de la liste





basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")         # 1. retire "Banana"
basket.remove("Blueberries")    # 2. retire "Blueberries"
basket.append("Kiwi")           # 3. ajoute "Kiwi" à la fin
basket.insert(0, "Apples")      # 4. ajoute "Apples" au début
print(basket.count("Apples"))   # 5. compte → affiche 2
basket.clear()                  # 6. vide la liste
print(basket)                   # 7. affiche l'état final → []

