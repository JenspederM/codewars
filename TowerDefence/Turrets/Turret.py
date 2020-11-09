class Turret:
    __slots__ = ['name', 'position', 'fire_rate', 'fire_range',
                 'positions_in_range', 'ammo']

    def __init__(self, name, position, fire_rate, fire_range, path):
        self.name = name
        self.position = position
        self.fire_rate = fire_rate
        self.fire_range = fire_range
        self.positions_in_range = self.find_positions_in_range(path)
        self.ammo = 0

    def __repr__(self):
        return f'Turret(Name: {self.name}, Position: {self.position}, ' \
               f'Rate: {self.fire_rate}, Range: {self.fire_range}, ' \
               f'Ammo: {self.ammo})'

    def reset(self):
        self.ammo = self.fire_rate

    def reload(self):
        self.ammo = self.fire_rate

    def fire(self, monster, debug=False):
        monster.afflict_damage()
        if debug is True:
            if debug:
                print(f'Turret {self.name} show at '
                      f'monster {monster.name}, which now have '
                      f'{monster.health} health')

            if not monster.is_alive:
                print(f'Turret {self.name} killed '
                      f'monster {monster.name}!')
        self.ammo -= 1

    def in_range(self, position):
        if position is None:
            return False
        else:
            return position in self.positions_in_range

    def find_positions_in_range(self, path):
        positions_in_range = []
        for position in path:
            if self.in_range2(position):
                positions_in_range.append(position)

        positions_in_range.reverse()  # We want to look at the last one first

        return positions_in_range

    def in_range2(self, position):
        i0, j0 = self.position
        i1, j1 = position
        from math import sqrt
        return sqrt((i1 - i0) ** 2 + (j1 - j0) ** 2) <= self.fire_range
