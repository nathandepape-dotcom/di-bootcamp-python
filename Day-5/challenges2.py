# Challenges #2 (Day 5)

# Exercise 1: Draw patterns using for loops

# Pattern 1 - pyramid
#   *
#  ***
# *****
print("Pattern 1:")
n = 3
for i in range(n):
    print(" " * (n - 1 - i) + "*" * (2 * i + 1))

# Pattern 2 - right-aligned triangle
#     *
#    **
#   ***
#  ****
# *****
print("\nPattern 2:")
n = 5
for i in range(n):
    print(" " * (n - 1 - i) + "*" * (i + 1))

# Pattern 3 - arrow (growing, flat, then shrinking)
# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *
print("\nPattern 3:")
for i in range(1, 6):
    print("*" * i)
print("*" * 5)
for i in range(4, 0, -1):
    print(" " * (5 - i) + "*" * i)


# Exercise 2: Analyse this code (selection sort)
# Goal: sort a list in ascending order using the "selection sort" idea.
my_list = [2, 24, 12, 354, 233]

# Loop over each position i except the last one.
for i in range(len(my_list) - 1):       # i = 0, 1, 2, 3
    minimum = i                          # assume the smallest is at index i
    # Scan the rest of the list (from i+1 to the end).
    for j in range(i + 1, len(my_list)):
        # If we find a smaller value, remember its index...
        if my_list[j] < my_list[minimum]:
            minimum = j
            # ...and swap it into position i right away.
            if minimum != i:
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]

# Final output: [2, 12, 24, 233, 354]
print(my_list)
