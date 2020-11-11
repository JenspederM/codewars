import copy

from TowerDefence.Monsters.Monsters import Monsters


class Board:
    def __init__(self,
                 input_board,
                 start_symbol='0',
                 path_symbol='1',
                 empty_symbol=' '):
        self.field = self.transform_board(input_board)
        self.start_symbol = start_symbol
        self.path_symbol = path_symbol
        self.empty_symbol = empty_symbol
        self.n = len(input_board)
        self.start = self.find_start()
        self.path = self.find_path()
        self.turret_positions = self.find_turret_positions()

    def __repr__(self):
        return f'Board(Shape: ({self.n}, {self.n}) Start: {self.start}, ' \
               f'End: ({self.path[-1]}), Path Length: {len(self.path)}, ' \
               f'Turrents: {len(self.turret_positions)})'

    def print_updated_board(self, monsters: Monsters):
        new_field = copy.deepcopy(self.field)
        for monster in monsters.list[monsters.done_count:monsters.spawn_count]:
            i, j = monster.position
            if monster.is_alive:
                new_field[i][j] = '+'
            else:
                new_field[i][j] = '-'
        for i, row in enumerate(new_field):
            new_field[i] = ''.join(row)
        
        print('\n'.join(new_field))

    def find_start(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.field[i][j] == self.start_symbol:
                    return i, j

    def find_path(self):
        path = [list(self.start),
                self.__get_next_position(self.start, self.start)]

        while True:
            next_position = self.__get_next_position(path[-2], path[-1])
            if next_position is not None:
                path.append(next_position)
            else:
                break

        return path

    @staticmethod
    def transform_board(board):
        new_board = []
        for line in board:
            new_board.append(list(line))
        return new_board

    def __get_next_position(self, last_position, current_position):
        i, j = current_position

        directions = {
            'left' : [i, j - 1],
            'right': [i, j + 1],
            'up'   : [i - 1, j],
            'down' : [i + 1, j]
        }

        for key, next_position in directions.items():
            i, j = next_position
            if 0 <= i <= self.n - 1 and \
                    0 <= j <= self.n - 1 and \
                    self.field[i][j] == self.path_symbol and \
                    next_position != last_position:
                return next_position

        return None  # When there are no possible directions, i.e. the path ends

    def find_turret_positions(self):
        turret_positions = {}
        known_symbols = [self.start_symbol, self.path_symbol, self.empty_symbol]
        for i, row in enumerate(self.field):
            for j, col in enumerate(row):
                if self.field[i][j] not in known_symbols:
                    symbol = self.field[i][j]
                    turret_positions[symbol] = [i, j]
        return turret_positions
