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
    print('\n'.join([''.join(row) for row in ladder]))


def transform_ladder(ladder):
    rows = len(ladder)
    cols = len(ladder[0])
    new_ladder = [[[] for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            cell = ladder[i][j]
            if cell == '0':
                new_ladder[i][j] = '|' + '0'
            elif cell == '1':
                new_ladder[i][j] = '|' + '1'

            if j == cols - 1:
                new_ladder[i][j] += '|'
    return new_ladder


def walk(ladder, start_position):
    rows = len(ladder)
    cols = len(ladder[0])
    i = 0
    j = start_position
    direction = 'r'
    while True:
        cell = ladder[i][j]
        if direction == 'r' and cell == '1':
            j += 1
        elif direction == 'l' and cell == '1':
            j -= 1
        if j + 1 == cols - 1:
            direction = 'l'
        if j - 1 == 0:
            direction = 'r'
        if i == rows - 1:
            return j
        else:
            i += 1


def amidakuji(ladder):
    visualize(transform_ladder(ladder))
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
