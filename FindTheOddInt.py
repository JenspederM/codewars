"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""

tests = [
    ([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], 5),
    ([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5], -1),
    ([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5], 5),
    ([10], 10),
    ([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1], 10),
    ([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10], 1)
]

from collections import Counter


def find_it(seq):
    count = Counter(seq)
    for k, v in count.items():
        if v % 2 != 0:
            return k


if __name__ == '__main__':
    for test, answer in tests:
        ans = find_it(test)
        print(f'Test: {test}\nCalculted Answer: {ans}, Actual Answer: {answer}')
