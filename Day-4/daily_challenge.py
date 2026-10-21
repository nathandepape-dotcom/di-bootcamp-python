# ============================================================
# Daily Challenge : Coffee Shop Menu Manager  (Day 4)
# ============================================================
# Tu es embauché pour gérer le menu d'un café en Python.
# Le programme doit être organisé en FONCTIONS (pas tout dans
# une grosse boucle).
#
# STRUCTURE DE DONNÉES :
#   menu = dictionnaire { nom_boisson (str) : prix (float) }
#   (on DOIT commencer avec ces 3 boissons pour que les tests passent)
#
# FONCTIONS À IMPLÉMENTER :
#   a) show_menu(menu_dict)      -> affiche "drink - price₪" pour chaque
#                                   item. Si vide -> "The menu is empty."
#   b) add_item(menu_dict)       -> demande nom + prix, ajoute au dict.
#                                   Si existe déjà -> "Item already exists!"
#   c) update_price(menu_dict)   -> demande le drink. Si existe -> nouveau
#                                   prix + "Price updated!". Sinon "Item not found."
#   d) delete_item(menu_dict)    -> demande le drink. Si existe -> supprime
#                                   + "Item deleted.". Sinon "Item not found."
#   e) show_options()            -> affiche le menu d'actions (1..5)
#   f) run_coffee_shop()         -> boucle principale : affiche options,
#                                   lit le choix, appelle la bonne fonction.
#                                   Choix invalide -> "Invalid choice, try again."
#                                   Choix 5 -> "Goodbye!" (stop)
# ============================================================


# --- Données initiales ---
menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}


def show_menu(menu_dict):
    """Print all drinks and prices."""
    if len(menu_dict) == 0:
        print("The menu is empty.")
    else:
        for nom, prix in menu_dict.items():
            print(f"{nom} - {prix}₪")


def add_item(menu_dict):
    """Add a new drink to the menu."""
    nom = input("Enter new drink name: ")
    prix = float(input("Enter price: "))
    if nom in menu_dict:
        print("Item already exists!")
    else:
        menu_dict[nom] = prix
        print(f'"{nom}" added!')


def update_price(menu_dict):
    """Change the price of an existing drink."""
    wich_drink = input("Which drink do you want to update? ")
    if wich_drink in menu_dict:
        new_price = float(input("Enter the new price: "))
        menu_dict[wich_drink] = new_price
        print("Price updated!")
    else:
        print("Item not found.")


def delete_item(menu_dict):
    """Remove a drink from the menu."""
    wich_drink_to_delete = input("Which drink do you want to delete? ")
    if wich_drink_to_delete in menu_dict:
        del menu_dict[wich_drink_to_delete]
        print("Item deleted.")
    else:
        print("Item not found.")


def show_options():
    """Print the available actions."""
    print("What would you like to do?")
    print("1. Show menu")
    print("2. Add item")
    print("3. Update price")
    print("4. Delete item")
    print("5. Exit")


def run_coffee_shop():
    """Main loop of the program."""
    while True:
        show_options()
        option_selected = input("> ")
        if option_selected == "1":
            show_menu(menu)
        elif option_selected == "2":
            add_item(menu)
        elif option_selected == "3":
            update_price(menu)
        elif option_selected == "4":
            delete_item(menu)
        elif option_selected == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


run_coffee_shop()
