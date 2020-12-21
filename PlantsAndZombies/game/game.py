from PlantsAndZombies.tower.towers import Towers
from PlantsAndZombies.zombie.zombies import Zombies


class Game:
    def __init__(self, board, zombies):
        self.input_board = board
        self.input_zombies = zombies

        self.rows = len(board)
        self.cols = len(board[0])

        self.board = []
        self.towers = Towers()
        self.zombies = Zombies(start_col=self.cols)

        self.move = 0
        self.game_over = False

        self.initialize_board()

    def __repr__(self):
        return f'Board(rows={self.rows}, cols={self.cols})'

    def initialize_board(self):
        input_board = self.input_board
        rows = self.rows
        cols = self.cols

        # Add game and tower positions
        for i in range(rows):
            for j in range(cols - 1, -1, -1):
                self.board.append((i, j))
                value = input_board[i][j]
                if value != ' ':
                    self.towers.add_tower(value, i, j)

        # Set range for towers
        for tower in self.towers:
            tower.set_range(rows, cols)

        # Add zombies
        for (entry_move, row, hp) in self.input_zombies:
            self.zombies.add_zombie(entry_move, row, hp)

        self.zombies.zombies.sort(key=lambda x: x.entry_move)

    def advance(self):
        self.move += 1
        self.towers.update_targets(self.zombies)
        self.towers.fire_towers(self.zombies)
        return self.zombies.advance(self.move)
