# Exercises XP - Day 4 : Functions
import random


# ---------- Exercise 1: What Are You Learning? ----------
def display_message():
    print("I am learning about functions in Python.")


display_message()


# ---------- Exercise 2: What's Your Favorite Book? ----------
def favorite_book(title):
    print(f"One of my favorite books is {title}.")


favorite_book("Alice in Wonderland")


# ---------- Exercise 3: Some Geography ----------
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")


describe_city("Reykjavik", "Iceland")
describe_city("Paris")


# ---------- Exercise 4: Random ----------
def compare_with_random(number):
    random_number = random.randint(1, 100)
    if number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {number}, Random number: {random_number}")


compare_with_random(50)


# ---------- Exercise 5: Personalized Shirts ----------
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")


make_shirt()
make_shirt("medium")
make_shirt("small", "Custom message")
make_shirt(size="small", text="Hello!")  # bonus: keyword arguments


# ---------- Exercise 6: Magicians ----------
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def show_magicians(names):
    for name in names:
        print(name)


def make_great(names):
    # modify the list itself (by index), so the change stays after the function
    for i in range(len(names)):
        names[i] = names[i] + " the Great"


make_great(magician_names)
show_magicians(magician_names)


# ---------- Exercise 7: Temperature Advice ----------
def get_season(month):
    if month in (12, 1, 2):
        return "winter"
    elif month in (3, 4, 5):
        return "spring"
    elif month in (6, 7, 8):
        return "summer"
    else:
        return "autumn"


def get_random_temp(season=None):
    # Bonus: float temperatures, depending on the season
    if season == "winter":
        return round(random.uniform(-10, 16), 1)
    elif season == "spring" or season == "autumn":
        return round(random.uniform(10, 25), 1)
    elif season == "summer":
        return round(random.uniform(24, 40), 1)
    return random.randint(-10, 40)


def main():
    month = int(input("Enter a month (1-12): "))
    season = get_season(month)
    temperature = get_random_temp(season)
    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temperature < 16:
        print("Quite chilly! Don't forget your coat.")
    elif temperature < 24:
        print("Nice weather.")
    elif temperature < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")


main()
