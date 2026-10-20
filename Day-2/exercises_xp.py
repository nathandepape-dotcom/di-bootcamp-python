# =============================================
# Day 2 - Exercises XP
# List, iterating and formatting data
# =============================================

# --- Exercice 1 : Favorite Numbers (sets) ---
favorite_set = {6, 13, 666}
friend_fav_numbers = {2, 1000, 379}
favorite_set.add(999)
favorite_set.add(333)
favorite_set.remove(333)
our_fav_numbers = favorite_set | friend_fav_numbers
print(our_fav_numbers)

# --- Exercice 2 : Tuple (immutabilité) ---
# Les tuples sont immuables : on ne peut pas y ajouter d'éléments après création.
mon_tuple = (1, 2, 3, 4, 5)
# mon_tuple.add(1)  # → AttributeError: 'tuple' object has no attribute 'add'

# --- Exercice 3 : List Manipulation ---
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)

# --- Exercice 4 : Floats ---
seq = []
for i in range(3, 11):
    seq.append(i / 2)
print(seq)

# --- Exercice 5 : For Loop ---
for i in range(1, 21):
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# --- Exercice 6 : While Loop ---
while True:
    name = input("Quel est ton nom ? ")
    if len(name) >= 3 and not name.isdigit():
        print("thank you")
        break

# --- Exercice 7 : Favorite Fruits ---
fruits = input("Put your favorite fruits : ").split()
fruit = input("Put a fruit that you want to eat : ")
if fruit in fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# --- Exercice 8 : Pizza Toppings ---
garniture = []
while True:
    question = input("Which toppings do you want? (Say 'STOP' to cancel): ")
    if question == "STOP":
        break
    garniture.append(question)
    print(f"Adding {question} to your pizza.")
print(f"Toppings: {garniture}")
print(f"Total cost: ${10 + len(garniture) * 2.5}")

# --- Exercice 9 : Cinemax Tickets ---
price = 0
while True:
    age = input("Age of each family member (say 'Quit' when done): ")
    if age == "Quit":
        break
    response = int(age)
    if response < 3:
        pass
    elif response <= 12:
        price += 10
    else:
        price += 15
print(f"Total cost : {price}")
