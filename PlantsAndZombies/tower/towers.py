from PlantsAndZombies.tower.tower import Tower


class Towers:
    def __init__(self):
        self.towers = {}

    def __repr__(self):
        return f'Towers(len={len(self.towers)})'

    def __iter__(self):
        return iter(self.towers.values())

    def add_tower(self, name, i, j):
        tmp = self.towers.get((i, j))
        if tmp is not None:
            raise ValueError(f'Position {i}, {j} is already occupied.')

        self.towers[(i, j)] = Tower(name, i, j)

    def update_targets(self, zombies):
        for tower in self:
            for zombie in zombies:
                zombie_pos = (zombie.row, zombie.col)
                if zombie_pos[1] is None:
                    break

                if zombie_pos in tower.range:
                    tower.targets.append(zombie)

    def fire_towers(self, zombies):
        for tower in self:
            for zombie in zombies:
                zombie_pos = (zombie.row, zombie.col)
                if zombie_pos[1] is None:
                    break

                if zombie_pos in tower.range:
                    tower.fire(zombie)
