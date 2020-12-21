from collections import OrderedDict

from PlantsAndZombies.tower.tower import Tower
from PlantsAndZombies.zombie.zombie import Zombie


class Game:
    def __init__(self, board, zombies):
        self.input_board = board
        self.input_zombies = zombies

        self.rows = len(board)
        self.cols = len(board[0])

        self.board = []
        self.towers = OrderedDict()
        self.zombies = {}

        self.move = -1
        self.game_over = False

        self.initialize_game()

    def __repr__(self):
        return f'Board(rows={self.rows}, cols={self.cols})'

    def initialize_game(self):
        input_board = self.input_board
        rows = self.rows
        cols = self.cols

        # Add game and tower positions

        for j in range(cols - 1, -1, -1):
            for i in range(rows):
                self.board.append((i, j))
                name = input_board[i][j]
                if name != ' ':
                    tower = Tower(name, i, j)
                    tower.add_bullets(self.rows, self.cols)
                    self.towers[(i, j)] = tower

        # Sort zombies according to entry move
        self.input_zombies.sort(key=lambda x: x[0])

    def move_zombies(self):
        zombies = {(i, j - 1): zombie for (i, j), zombie in self.zombies.items()}
        for (entry_move, row, hp) in self.input_zombies:
            if entry_move <= self.move:
                col = (self.cols - 1) - (self.move - entry_move)
                zombie = zombies.get((row, col))
                if zombie is None:
                    zombie = Zombie(entry_move, row, hp)
                zombie.col = col
            else:
                break

            if zombie.col == 0 and zombie.hp > 0:
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

    def destroy_towers(self):
        for zombie_position in self.zombies.keys():
            # Destroy tower, if zombie position reaches its position
            tower = self.towers.get(zombie_position)
            if tower is not None:
                tower.is_destroyed = True

    def advance(self):
        """
        During a move, new zombies appear and/or existing ones move forward one space to the left. Then the shooters
        fire. This two-step process repeats. If a zombie reaches a shooter's position, it destroys that shooter.

        :return: Game Over
        """
        self.move += 1
        self.move_zombies()
        self.fire_towers()
        self.destroy_towers()
