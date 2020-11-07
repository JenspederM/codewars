# -*- coding: utf-8 -*-
from symbol import test
import numpy as np
from scipy.signal import convolve2d


def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('<:LF:>')
    return ''.join(s)


start = [[1, 0, 0],
         [0, 1, 1],
         [1, 1, 0]]
end = [[0, 1, 0],
       [0, 0, 1],
       [1, 1, 1]]


def pad_array(array):
    a = np.asarray(array)
    conv = convolve2d(a, np.ones((3, 3), dtype=int), 'same') - a
    result = np.zeros(conv.shape)

    return conv


# test.describe('Glider<:LF:>' + htmlize(start))
# test.it('Glider 1')


def get_generation(cells, generations):
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            obs = cells[i][j]


resp = get_generation(start, 1)
