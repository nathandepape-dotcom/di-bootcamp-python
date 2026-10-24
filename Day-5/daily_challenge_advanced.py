# Daily Challenge : Advanced Algorithm (Day 5)
#
# Find all the pairs of numbers in list_of_numbers that sum to
# the target number.

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

seen = set()
pairs = set()
for n in list_of_numbers:
    complement = target_number - n
    if complement in seen:
        pairs.add(tuple(sorted((n, complement))))
    seen.add(n)

for a, b in sorted(pairs):
    print(f"{a} and {b} sums to the target_number {target_number}")
