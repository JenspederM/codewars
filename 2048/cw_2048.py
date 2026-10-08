from copy import deepcopy

# from preloaded import DOWN, LEFT, RIGHT, UP
# from preloaded import TFE   # TFE.UP, TFE.LEFT, ...
#
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"
UP = "UP"


def print_board(board: list[list[int]]):
    for r in board:
        print(" ".join(str(v) for v in r))


def transpose(board: list[list[int]]):
    return list(map(list, zip(*board)))


def sum_list(l: list):
    i = 0
    is_summed = [False] * len(l)
    while True:
        if i + 1 == len(l):
            break
        if l[i] == 0 and l[i + 1] != 0:
            l[i], l[i + 1] = l[i + 1], l[i]
            i = 0
        elif l[i] == l[i + 1] and not is_summed[i] and not is_summed[i + 1]:
            l[i] += l[i + 1]
            is_summed[i] = True
            l[i + 1] = 0
            i += 1
        else:
            i += 1
    return l


def update_board(board: list[list[int]], direction):
    while True:
        if direction == UP:
            rows = transpose(board)
            nb = [sum_list(l) for l in rows]
            return transpose(nb)
        elif direction == DOWN:
            rows = transpose(board)
            nb = [list(reversed(sum_list(list(reversed(l))))) for l in rows]
            return transpose(nb)
        elif direction == RIGHT:
            nb = [list(reversed(sum_list(list(reversed(l))))) for l in board]
            return nb
        else:
            nb = [sum_list(l) for l in board]
            return nb


sample_test_cases = [
    (
        "Slide tiles to the edge of the board when none are in the way",
        [[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        (
            (UP, [[0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
            (LEFT, [[0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
            (DOWN, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 0]]),
            (RIGHT, [[0, 0, 0, 0], [0, 0, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0]]),
        ),
    ),
    (
        "Combine like tiles",
        [[0, 0, 0, 0], [0, 2, 2, 0], [0, 2, 2, 0], [0, 0, 0, 0]],
        (
            (UP, [[0, 4, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
            (LEFT, [[0, 0, 0, 0], [4, 0, 0, 0], [4, 0, 0, 0], [0, 0, 0, 0]]),
            (DOWN, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 4, 4, 0]]),
            (RIGHT, [[0, 0, 0, 0], [0, 0, 0, 4], [0, 0, 0, 4], [0, 0, 0, 0]]),
        ),
    ),
    (
        "Collapse tiles only once per turn",
        [[0, 2, 2, 0], [2, 2, 2, 2], [2, 2, 2, 2], [0, 2, 2, 0]],
        (
            (UP, [[4, 4, 4, 4], [0, 4, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
            (LEFT, [[4, 0, 0, 0], [4, 4, 0, 0], [4, 4, 0, 0], [4, 0, 0, 0]]),
            (DOWN, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 4, 4, 0], [4, 4, 4, 4]]),
            (RIGHT, [[0, 0, 0, 4], [0, 0, 4, 4], [0, 0, 4, 4], [0, 0, 0, 4]]),
        ),
    ),
    (
        "Don't merge tiles which were the result of a merge earlier this turn",
        [[4, 4, 4, 4], [4, 4, 4, 4], [8, 8, 8, 8], [0, 0, 0, 0]],
        ((UP, [[8, 8, 8, 8], [8, 8, 8, 8], [0, 0, 0, 0], [0, 0, 0, 0]]),),
    ),
    (
        "Random tests",
        [[8, 8, 8, 16], [8, 8, 16, 16], [16, 8, 16, 16], [16, 8, 8, 16]],
        ((LEFT, [[16, 8, 16, 0], [16, 32, 0, 0], [16, 8, 32, 0], [16, 16, 16, 0]]),),
    ),
]


def main():
    # print(sum_list([0, 0, 2, 0]))
    # print(sum_list([4, 4, 8, 0]))
    # return

    for name, board, test_cases in sample_test_cases:
        print(f"=== Testing {name}")

        for direction, expected in test_cases:
            if direction not in [UP, DOWN, LEFT, RIGHT]:
                print(f"skipped {direction}")
                continue
            actual = update_board(deepcopy(board), direction)
            if actual == expected:
                print(f"pass({direction})")
            else:
                print(f"fail({direction})")
                print("board")
                print_board(board)
                print("actual")
                print_board(actual)
                print("expected")
                print_board(expected)
                raise StopIteration


if __name__ == "__main__":
    main()
