"""Alphabetic Anagrams

Consider a "word" as any sequence of capital letters A-Z (not limited to just "dictionary words"). For any word
with at least two different letters, there are other words composed of the same letters but in a different order (for
instance, STATIONARILY/ANTIROYALIST, which happen to both be dictionary words; for our purposes "AAIILNORSTTY" is
also a "word" composed of the same letters as these two).

We can then assign a number to every word, based on where it falls in an alphabetically sorted list of all words made
up of the same group of letters. One way to do this would be to generate the entire list of words and find the
desired one, but this would be slow if the word is long.

Given a word, return its number. Your function should be able to accept any word 25 letters or less in length (
possibly with some letters repeated), and take no more than 500 milliseconds to run. To compare, when the solution
code runs the 27 test cases in JS, it takes 101ms.

For very large words, you'll run into number precision issues in JS (if the word's position is greater than 2^53).
For the JS tests with large positions, there's some leeway (.000000001%). If you feel like you're getting it right
for the smaller ranks, and only failing by rounding on the larger, submit a couple more times and see if it takes.

Python, Java and Haskell have arbitrary integer precision, so you must be precise in those languages (unless someone
corrects me).

C# is using a long, which may not have the best precision, but the tests are locked so we can't change it.

Sample words, with their rank:
ABAB = 2
AAAB = 1
BAAA = 4
QUESTION = 24572
BOOKKEEPER = 10743

"""
from collections import Counter
from functools import reduce
from math import factorial
from operator import mul
from string import ascii_uppercase


# substring of a string
def countOfAnagramSubstring(s):
    # Returns total number of anagram
    # substrings in s
    n = len(s)
    mp = dict()

    # loop for length of substring
    for i in range(n):
        sb = ''
        for j in range(i, n):
            sb = ''.join(sorted(sb + s[j]))
            mp[sb] = mp.get(sb, 0)

            # increase count corresponding
            # to this dict array
            mp[sb] += 1

    anas = 0

    # loop over all different dictionary
    # items and aggregate substring count
    for k, v in mp.items():
        anas += (v * (v - 1)) // 2
    return anas


countOfAnagramSubstring('AAAB')


def get_alphabet_index(x):
    alphabet = {key: index for index, key in enumerate(ascii_uppercase)}
    return alphabet[x]


def toString(word):
    return ''.join(word)


def position(word):
    charset = Counter(word)
    pos = 1  # Per OP 1 index
    chars1 = sorted(charset)
    for letter in word:
        chars = sorted(charset)
        for char in chars[:chars.index(letter)]:
            ns = Counter(charset) - Counter(char)
            pos += factorial(sum(ns.values())) // reduce(mul, map(factorial, ns.values()))
        charset -= Counter([letter])
    return pos


position('BCAA')

# testValues = {'A': 1, 'ABAB': 2, 'AAAB': 1, 'BAAA': 4, 'QUESTION': 24572, 'BOOKKEEPER': 10743}
# [listPosition(k) == v for k, v in testValues.items()]

"""
test.describe('Anagram')
test.it('Must return appropriate values for known inputs')

for word in testValues:
    test.assert_equals(listPosition(word), testValues[word], 'Incorrect list position for: ' + word)
"""

word = 'CAAAB'


def toString(List):
    return ''.join(List)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack


n = len(word)
a = list(word)
permute(a, 0, n - 1)
# %%
