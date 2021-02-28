import functools
import operator


def persistence(n):
    counter = 0
    while n > 10:
        n_list = [int(c) for c in list(str(n))]
        n = functools.reduce(operator.mul, n_list)
        counter += 1

    return counter


if __name__ == "__main__":
    test_cases = [39, 4, 25, 999]

    for test in test_cases:
        print(str(persistence(test)))
