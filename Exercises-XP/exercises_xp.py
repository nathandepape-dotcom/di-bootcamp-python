# ============================================================
# Exercises XP - Starting with Python (Week 1)
# All 9 exercises grouped in a single file.
# ============================================================


# Exercise 1 : Hello World
print("Hello world\n" * 4, end="")


# Exercise 2 : Some Math
b = 99**3 * 8
print(b)


# Exercise 3 : What is the output ?
# Predictions (commented) then execution:
#   5 < 3            -> False
#   3 == 3           -> True
#   3 == "3"         -> False
#   "3" > 3          -> TypeError (cannot compare str and int)
#   "Hello" == "hello" -> False
print(5 < 3)
print(3 == 3)
print(3 == "3")
print("Hello" == "hello")


# Exercise 4 : Your computer brand
computer_brand = "razer"
print(f"I have a {computer_brand} computer.")


# Exercise 5 : Your information
name = "Nathan"
age = 25
shoe_size = 42
info = f"Hi, I'm {name}, I'm {age} years old and I wear size {shoe_size} shoes."
print(info)


# Exercise 6 : A & B
a = 7
b = 6
if a > b:
    print("Hello World")


# Exercise 7 : Odd or Even
n = int(input("Enter a number from 1-10"))
if n % 2 == 0:
    print("your number is even")
else:
    print("Your number is odd")


# Exercise 8 : What's your name ?
name = input("What's your name")
if name.title() == "Nathan":
    print("You just met your clone")
else:
    print("We are not meant to be friends")


# Exercise 9 : Tall enough to ride a roller coaster
height = int(input("What's your height in cm ?"))
if height > 145:
    print("Tall enough to ride")
else:
    print("Need to grow some more ;p")
