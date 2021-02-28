def find_outlier(integers):
    evens = []
    odds = []

    for i in integers:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    if len(evens) > len(odds):
        return odds[0]
    else:
        return evens[0]


test_cases = [
    [2, 4, 6, 8, 10, 3],
    [2, 4, 0, 100, 4, 11, 2602, 36],
    [160, 3, 1719, 19, 11, 13, -21]
]

if __name__ == '__main__':
    for test in test_cases:
        print(find_outlier(test))
