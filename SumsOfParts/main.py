"""https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python
Let us consider this example (array written in general format):

ls = [0, 1, 3, 6, 10]

Its following parts:

ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []
The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]

The function parts_sums (or its variants in other languages) will take as parameter a list ls and return a list of the sums of its parts as defined above.

Other Examples:
ls = [1, 2, 3, 4, 5, 6]
parts_sums(ls) -> [21, 20, 18, 15, 11, 6, 0]

ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
parts_sums(ls) -> [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]
Notes
Take a look at performance: some lists have thousands of elements.
Please ask before translating.
"""

tests = [
    [0, 1, 3, 6, 10],
    [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
]


def parts_sums2(ls):
    result = [sum(ls)]
    for i in range(len(ls)):
        result.append(result[-1] - ls[i])
    return result


def parts_sums1(ls):
    return [sum(ls[i:]) for i in range(len(ls))] + [0]


def parts_sums(ls):
    ls = ls.copy()
    result = []
    for i in range(len(ls)):
        result.append(sum(ls))
        ls.pop()
    result.append(0)
    return result


if __name__ == "__main__":
    for test in tests:
        print(f'0: {parts_sums(test)}')
        print(f'1: {parts_sums1(test)}')
        print(f'2: {parts_sums2(test)}')
