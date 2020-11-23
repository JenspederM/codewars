import numpy as np

pyramid_test = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]


def longest_slide_down(pyramid):
    n = max([len(e) for e in pyramid])
    pyr = np.zeros((n, n))
    i = 0
    for i, row in enumerate(pyramid):
        for j, el in enumerate(row):
            pyr[i, j] = np.int(el)
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            if pyr[i + 1][j] > pyr[i + 1][j + 1]:
                pyr[i][j] += pyr[i + 1][j]
            else:
                pyr[i][j] += pyr[i + 1][j + 1]
    return int(pyr[0][0])
