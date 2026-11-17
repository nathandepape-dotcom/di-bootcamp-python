# Daily Challenge: Dictionaries (Day 3)

# ---------- Challenge 1: Letter Index Dictionary ----------
word = input("Enter a word: ")

letter_indexes = {}
for index, letter in enumerate(word):
    if letter in letter_indexes:
        letter_indexes[letter].append(index)
    else:
        letter_indexes[letter] = [index]

print(letter_indexes)


# ---------- Challenge 2: Affordable Items ----------
def clean_price(price):
    """'$1,000' -> 1000"""
    return int(price.replace("$", "").replace(",", ""))


def affordable_items(items_purchase, wallet):
    money = clean_price(wallet)
    basket = []

    # Dictionary order = priority, so we buy in that order
    for item, price in items_purchase.items():
        cost = clean_price(price)
        if cost <= money:
            basket.append(item)
            money -= cost

    if not basket:
        return "Nothing"
    return sorted(basket)


print(affordable_items({"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}, "$300"))
print(affordable_items({"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}, "$100"))
print(affordable_items({"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}, "$1"))
