# Daily Challenge Gold: Solve the Matrix (Day 4 - Functions)
#
# Goal: Decrypt a hidden message from a matrix string by processing it
# column-wise and filtering characters.

MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

# Step 1: Convert MATRIX_STR to a 2D list (matrix)
matrix = []
for ligne in MATRIX_STR.splitlines()[1:]:
    matrix.append(list(ligne))

# Step 2: Iterate through columns
# Step 3: Filter alpha characters
# Step 4: Replace groups of symbols between two letters with a space
decoded_message = ""
gap = False
for col in range(len(matrix[0])):
    for lig in range(len(matrix)):
        char = matrix[lig][col]
        if char.isalpha():
            if gap:
                decoded_message += " "
            decoded_message += char
            gap = False
        else:
            if decoded_message:
                gap = True

# Step 5: Print the decoded message
print(decoded_message)
