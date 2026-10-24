# Challenges (Day 5) - 20 exercises

import math

# Exercise 1: insert an item at a defined index in a list
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 'x')
print(my_list)

# Exercise 2: count the number of spaces in a string
sentence = "hello world, how are you"
print(sentence.count(" "))

# Exercise 3: count upper case and lower case letters in a string
text = "Hello World"
upper = sum(1 for c in text if c.isupper())
lower = sum(1 for c in text if c.islower())
print(upper, lower)

# Exercise 4: sum of a list without the built-in sum()
def my_sum(lst):
    total = 0
    for x in lst:
        total += x
    return total

# Exercise 5: max number in a list
def find_max(lst):
    m = lst[0]
    for x in lst:
        if x > m:
            m = x
    return m

# Exercise 6: factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Exercise 7: count an element in a list (without .count)
def list_count(lst, el):
    count = 0
    for x in lst:
        if x == el:
            count += 1
    return count

# Exercise 8: L2-norm (sqrt of the sum of squares)
def norm(lst):
    return math.sqrt(sum(x * x for x in lst))

# Exercise 9: check if an array is monotonic
def is_mono(arr):
    return arr == sorted(arr) or arr == sorted(arr, reverse=True)

# Exercise 10: print the longest word in a list
def print_longest_word(words):
    longest = ""
    for w in words:
        if len(w) > len(longest):
            longest = w
    print(longest)

# Exercise 11: split integers and strings into two lists
def separate(mixed):
    ints = []
    strings = []
    for x in mixed:
        if isinstance(x, str):
            strings.append(x)
        else:
            ints.append(x)
    return ints, strings

# Exercise 12: check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Exercise 13: number of words with length > k
def sum_over_k(sentence, k):
    count = 0
    for w in sentence.split():
        if len(w) > k:
            count += 1
    return count

# Exercise 14: average value in a dictionary
def dict_avg(d):
    return sum(d.values()) / len(d)

# Exercise 15: common divisors of two numbers
def common_div(a, b):
    result = []
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            result.append(i)
    return result

# Exercise 16: test if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Exercise 17: print elements where both index and value are even
def weird_print(lst):
    result = []
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            result.append(lst[i])
    return result

# Exercise 18: count the different types of keyworded arguments
def type_count(**kwargs):
    counts = {}
    for v in kwargs.values():
        t = type(v).__name__
        counts[t] = counts.get(t, 0) + 1
    return counts

# Exercise 19: mimic the built-in .split() method
def my_split(s, sep=None):
    result = []
    current = ""
    if sep is None:
        for c in s:
            if c.isspace():
                if current:
                    result.append(current)
                    current = ""
            else:
                current += c
    else:
        for c in s:
            if c == sep:
                result.append(current)
                current = ""
            else:
                current += c
    if current:
        result.append(current)
    return result

# Exercise 20: convert a string to password format
password = "mypassword"
print("*" * len(password))

# --- Tests (examples from the instructions) ---
print(my_sum([1, 5, 4, 2]))
print(find_max([0, 1, 3, 50]))
print(factorial(4))
print(list_count(['a', 'a', 't', 'o'], 'a'))
print(norm([1, 2, 2]))
print(is_mono([7, 6, 5, 5, 2, 0]))
print(is_mono([2, 3, 3, 3]))
print(is_mono([1, 2, 0, 4]))
print(is_palindrome('radar'))
print(is_palindrome('John'))
print(sum_over_k('Do or do not there is no try', 2))
print(dict_avg({'a': 1, 'b': 2, 'c': 8, 'd': 1}))
print(common_div(10, 20))
print(is_prime(11))
print(weird_print([1, 2, 2, 3, 4, 5]))
print(type_count(a=1, b='string', c=1.0, d=True, e=False))
