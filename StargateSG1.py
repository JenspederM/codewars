import numpy as np

no_existingWires = """
SX.
XX.
..G
""".strip('\n')

no_solution = "Oh for crying out loud..."

existingWires = """
SX.
X..
XXG
""".strip('\n')

solution = """
SX.
XP.
XXG
""".strip('\n')


def wire_DHD_SG1(existingWires):
    wires = np.asarray([list(row) for row in existingWires.split('\n')])
    start = [int(i) for i in np.where(wires == 'S')]
    path = [list(start),
            __get_next_position(wires, start, start, '.')]

    while True:
        next_position = __get_next_position(wires, path[-2], path[-1],
                                            ['.', 'G'])
        if next_position is not None:
            path.append(next_position)
            i, j = next_position
            if wires[i, j] == 'G':
                return path
        else:
            break

    return "Oh for crying out loud..."


def __get_next_position(wires,
                        last_position,
                        current_position,
                        path_symbol=['.', 'G']):
    i, j = current_position

    directions = [
        [i - 1, j],  # Up
        [i - 1, j - 1],  # Up-Left
        [i - 1, j + 1],  # Up-Right
        [i + 1, j],  # Down
        [i + 1, j - 1],  # Down-Left
        [i + 1, j + 1],  # Down-Right
        [i, j + 1],  # Right
        [i, j - 1]  # Left
    ]

    for next_position in directions:
        i, j = next_position
        if 0 <= i <= wires.shape[0] - 1 and \
                0 <= j <= wires.shape[1] - 1 and \
                wires[i][j] in path_symbol and \
                next_position != last_position:
            return next_position

    return None  # When there are no possible directions, i.e. the path ends
