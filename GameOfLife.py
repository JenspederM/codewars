import numpy as np


def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('\n')
    return ''.join(s)


start = [[1, 1, 1, 0, 0, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0, 1, 1, 1]]


def iterate(z):
    # find number of neighbours that each square has
    N = np.zeros(z.shape)
    N[1:, 1:] += z[:-1, :-1]
    N[1:, :-1] += z[:-1, 1:]
    N[:-1, 1:] += z[1:, :-1]
    N[:-1, :-1] += z[1:, 1:]
    N[:-1, :] += z[1:, :]
    N[1:, :] += z[:-1, :]
    N[:, :-1] += z[:, 1:]
    N[:, 1:] += z[:, :-1]
    # a live cell is killed if it has fewer than 2 or more than 3 neighbours.
    part1 = ((z == 1) & (N < 4) & (N > 1))
    # a new cell forms if a square has exactly three members
    part2 = ((z == 0) & (N == 3))
    return (part1 | part2).astype(int)


def get_generation(cells, generations):
    ar = np.asarray(cells)
    ar = np.pad(ar, generations, 'constant')
    for _ in range(generations):
        ar = iterate(ar)
        print(htmlize(ar))

    # remove zero cols
    col_idxs = np.where(np.all(ar == 0, axis=0) == False)[0]
    row_idxs = np.where(np.all(ar == 0, axis=1) == False)[0]
    ar = ar[:, col_idxs.min():col_idxs.max() + 1]
    # remove zero rows
    ar = ar[row_idxs.min():row_idxs.max() + 1, :]
    return ar.tolist()
