from PlantsAndZombies.zombie.zombie import Zombie


class Zombies:
    def __init__(self, start_col):
        self.zombies = []
        self.start_col = start_col
        self.reached_end = False

    def __repr__(self):
        return f'Zombies(len={len(self.zombies)})'

    def __iter__(self):
        return iter(self.zombies)

    def add_zombie(self, entry_move, row, hp):
        self.zombies.append(Zombie(entry_move, row, hp))

    def advance(self, move: int):
        for zombie in self.zombies:
            if zombie.entry_move <= move and zombie.col is None:
                zombie.col = self.start_col
            elif zombie.col is not None:
                zombie.col -= 1
            else:
                break
            if zombie.col == 0:
                self.reached_end = True
