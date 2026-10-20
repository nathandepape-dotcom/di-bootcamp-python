# Exercice 8 : Pizza Toppings
# 1. Écris une boucle qui demande les garnitures de pizza une par une
# 2. Arrête la boucle quand l'utilisateur tape 'quit'
# 3. Pour chaque garniture, affiche : "Adding [garniture] to your pizza."
# 4. Après la boucle, affiche toutes les garnitures et le coût total
#    Prix de base : $10, chaque garniture ajoute $2.50

garniture = []
while True:
    question = input("Wich toppings do you want on top of your pizza? (Say 'STOP' when you're done with your order)")
    if question == "STOP":
        break
    garniture.append(question)
    print(f"Adding {question} to your pizza.")

print(f"Toppings: {garniture}")
print(f"Total cost: ${10 + len(garniture) * 2.5}")

