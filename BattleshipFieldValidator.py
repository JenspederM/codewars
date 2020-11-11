import numpy as np

battlefield_test = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def validate_battlefield(field):
    """
    Write a method that takes a field for well-known board game "Battleship"
    as an argument and returns true if it has a valid disposition of ships,
    false otherwise. Argument is guaranteed to be 10*10 two-dimension array.
    Elements in the array are numbers, 0 if the cell is free and 1 if
    occupied by ship.

    Battleship (also Battleships or Sea Battle) is a guessing game for two
    players. Each player has a 10x10 grid containing several "ships" and
    objective is to destroy enemy's forces by targetting individual cells on
    his field. The ship occupies one or more cells in the grid. Size and
    number of ships may differ from version to version. In this kata we will
    use Soviet/Russian version of the game.

    Before the game begins, players set up the board and place the ships
    accordingly to the following rules:
    - There must be single battleship (size of 4 cells), 2 cruisers (size 3),
    3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are
    not allowed, as well as missing ships.
    - Each ship must be a straight line, except for submarines, which are just
    single cell.
    - The ship cannot overlap or be in contact with any other ship, neither by
    edge nor by corner.
    :param field: Battlefield
    :return: boolean
    """
    ships = {4: 0, 3: 0, 2: 0, 1: 0}
    mat = np.asarray(field)
    occupied_fields = []
    for i in range(10):
        for j in range(10):
            for offset, value in ships.items():
                indices, check_ship = validate_ship(mat, offset, i, j)
                if check_ship is True and \
                        all([i not in occupied_fields for i in indices]):
                    check_neighbors = validate_neighbors(mat, indices)
                    if check_neighbors is False:
                        return False
                    ships[offset] += 1
                    occupied_fields.extend(indices)

    return ships[4] == 1 and \
           ships[3] == 2 and \
           ships[2] == 3 and \
           ships[1] == 4


def validate_ship(mat, offset, i, j):
    indices = {'down': [], 'right': []}
    for key in indices.keys():
        for o in range(offset):
            if key == 'down':
                indices[key].append((i + o, j))
            else:
                indices[key].append((i, j + o))

    for key, value in indices.items():
        idx = tuple(np.array(value).T)
        if np.all((idx[0] >= 0) & (idx[0] < 10)) and \
                np.all((idx[0] >= 0) & (idx[1] < 10)) and \
                np.sum(mat[idx]) == offset:
            return value, True
    return None, False


def validate_neighbors(mat, indices):
    for idx in indices:
        i, j = idx
        directions = [(i - 1, j),  # Up
                      (i - 1, j - 1),  # Up-Left
                      (i - 1, j + 1),  # Up-Right
                      (i + 1, j),  # Down
                      (i + 1, j - 1),  # Down-Left
                      (i + 1, j + 1),  # Down-Right
                      (i, j + 1),  # Right
                      (i, j - 1)]  # Left
        directions = np.array([d for d in directions if d not in indices])
        in_lim = np.all((directions >= 0) & (directions < 10), axis=1)
        directions = tuple(directions[in_lim].T)
        if np.any(mat[directions] == 1):
            return False

    return True
