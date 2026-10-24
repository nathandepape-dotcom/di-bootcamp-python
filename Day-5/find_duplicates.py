# Remote Exercise : Find Duplicates (Day 5)
# Print the duplicate values of a list (no sets allowed).

some_list = ['A', 'B', 'C', 'B', 'D', 'D']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:      # the value appears more than once
        if value not in duplicates:     # keep only one instance of it
            duplicates.append(value)

print(duplicates)
