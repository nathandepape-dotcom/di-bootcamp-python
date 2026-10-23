# Mini-Project #2 - Hangman (Day 5)
#
# Goal: Create a Hangman game. The computer picks a random word,
# the player guesses letters until they solve the word or run out
# of 6 body parts (head, body, 2 arms, 2 legs).

import random


wordslist = ['correction', 'childish', 'beach', 'python', 'assertive',
             'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)

### YOUR CODE STARTS FROM HERE ###
cache = []
wrong = 0
guessed =[]
for c in word :
    if c == ' ':
        cache.append(' ')
    else :
        cache.append("*")

while '*' in cache and wrong < 6:
    print(" ".join(cache)) 
    letter = input("Choose a letter to guess the word")

    
    if letter in guessed:
        print("Already tried")
        continue
        
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                
                cache[i] = letter
                print(letter)
        
    else:
        wrong +=1
    guessed.append(letter)
if "*" not in cache:
    
    print("You won")
else:
    print(f"The correct word was {word}")
    print("You lost")

    


  







# 1. Build the "hidden" version of the word: a star '*' for each letter,
#    and keep spaces as spaces (for words like "credit card").

# 2. Track the number of wrong guesses (max 6) and the letters already guessed.

# 3. Game loop: while not solved and wrong guesses < 6:
#    - show the hidden word
#    - ask the player for a letter
#    - reject the letter if it was already guessed
#    - if the letter is in the word, reveal it in all positions
#    - otherwise, add a body part (wrong += 1)

# 4. After the loop, print the result (win or lose) and the word.
