# Daily Challenge: Challenges (Day 5)

# Challenge 1: Sorting
# Take a comma-separated string of words and output them sorted
# alphabetically, still separated by commas.
words_input = input("Enter words separated by commas: ")
words_list = words_input.split(",")
words_list.sort()
print(",".join(words_list))

# Challenge 2: Longest Word
# Return the longest word in a sentence. If several words tie for the
# longest, return the first one. Punctuation counts as part of the word.
def longest_word(sentence):
    words = sentence.split(" ")
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))
