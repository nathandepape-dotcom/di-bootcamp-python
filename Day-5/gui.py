# Remote Exercise: Our First GUI (Day 5)
# Display an image by looping through a list of lists:
# 0 -> space, 1 -> star.

picture = [
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0]
]

for row in picture:
    for pixel in row:
        if pixel == 0:
            print(' ', end='')
        else:
            print('*', end='')
    print()
