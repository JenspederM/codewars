from collections import OrderedDict

from PlantsAndZombies.tower.tower import Tower
from PlantsAndZombies.zombie.zombie import Zombie


class Game:
    def __init__(self, board, zombies, solution=None):
        self.input_board = board
        self.input_zombies = zombies
        self.solution = solution

        self.rows = len(board)
        self.cols = len(board[0])

        self.board = []
        self.towers = OrderedDict()
        self.zombies = {}

        self.move = -1
        self.game_over = False

        self.initialize_towers_and_zombies()

    def __repr__(self):
        return f'Game([{self.rows}, {self.cols}], Towers = {len(self.towers)}, Zombies = {len(self.zombies)})'

    def initialize_towers_and_zombies(self):
        input_board = self.input_board
        rows = self.rows
        cols = self.cols

        # Construct towers
        for j in range(cols - 1, -1, -1):
            for i in range(rows):
                name = input_board[i][j]
                if name != ' ':
                    tower = Tower(name, i, j)
                    tower.add_bullets(rows, cols)
                    self.towers[(i, j)] = tower

        # Sort zombies according to entry move
        self.input_zombies.sort(key=lambda x: x[0])

    def move_zombies(self):
        zombies = OrderedDict({(i, j - 1): zombie for (i, j), zombie in self.zombies.items()})
        for (entry_move, row, hp) in self.input_zombies:
            if entry_move <= self.move:
                col = (self.cols - 1) - (self.move - entry_move)
                zombie = zombies.get((row, col))
                if zombie is None:
                    zombie = Zombie(entry_move, row, hp)
                zombie.col = col
            else:
                break

            # Destroy tower, if zombie position reaches its position
            tower = self.towers.get((row, col))
            if tower is not None:
                tower.is_destroyed = True

            if zombie.col < 0 and zombie.hp > 0:
                self.game_over = True

            zombies[(row, col)] = zombie

        self.zombies = zombies

    def fire_towers(self):
        if self.move > 0:
            for tower in self.towers.values():
                for bullet in tower.bullets:
                    for position in bullet.path:
                        zombie = self.zombies.get(position)
                        if zombie is not None:
                            zombie.hp -= 1
                            break

    def advance(self):
        """
        During a move, new zombies appear and/or existing ones move forward one space to the left. Then the shooters
        fire. This two-step process repeats. If a zombie reaches a shooter's position, it destroys that shooter.

        :return: Game Over
        """
        self.move += 1
        self.move_zombies()
        self.fire_towers()

    def run(self):
        while not self.game_over:
            self.advance()

        if any(True for zombie in self.zombies.values() if zombie.hp > 0):
            return self.move
        else:
            return None
