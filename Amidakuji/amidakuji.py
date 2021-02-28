ladder = [
    '001001',
    '010000',
    '100100',
    '001000',
    '100101',
    '010010',
    '101001',
    '010100'
]
import numpy as np


class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def visualize(ladder):
    rows = len(ladder)
    cols = len(ladder[0])
    new_ladder = [[] for _ in range(rows + 1)]
    for j in range(cols):
        new_ladder[0].extend([str(j), " "])
        if j == cols - 1:
            new_ladder[0].extend([str(j + 1)])

    for i in range(1, rows + 1):
        for j in range(cols + 1):
            if j == cols:
                new_ladder[i].extend(['| '])
            else:
                cell = ladder[i - 1][j]
                if cell == '0':
                    new_ladder[i].extend(['|', ' '])
                elif cell == '1':
                    new_ladder[i].extend(['|', '_'])

    print('\n'.join([''.join(row) for row in new_ladder]))
    result = {}
    for i in range(1, len(new_ladder + 1)):
        for j in range(0, len(new_ladder[0]), 2):
            print(new_ladder[0][j])
            position = j // 2
            if j > 0 and new_ladder[1][j - 1] == "_":
                position -= 1
            elif new_ladder[1][j + 1] == "_":
                position += 1

            result[j] = position
            print(f'Position: {position}\n, Result {result}')


def walk(array, start_position):
    new_array = np.array([[np.int8(el) for el in row] for row in ladder])
    cols = new_array.shape[1]

    i = 0
    j = start_position
    for i in range(len(array)):
        pass


def amidakuji(ladder):
    visualize(ladder)
    print([walk(ladder, i) for i in range(len(ladder[0]) - 1)])


ar = [
    '|0|0|0|0|0|1|',
    '|0|1|0|0|1|0|',
    '|1|0|1|0|0|1|',
    '|0|1|0|1|0|0|',
    '|0|0|1|0|1|0|',
    '|0|1|0|0|0|0|',
    '|1|0|0|0|1|0|',
    '|0|1|0|1|0|0|'
]

ladder2 = []
