from TowerDefence.Monsters.Monster import Monster


class Monsters:
    def __init__(self, board, wave):
        self.list = self.create_monsters(board, wave)
        self.wave_length = len(wave)
        self.done_count = 0
        self.spawn_count = 0
        self.remaining_health = 0

    def __repr__(self):
        return f'Monsters(Wave Length: {self.wave_length})'

    @staticmethod
    def create_monsters(board, wave):
        monster_list = []
        for health in wave:
            monster_list.append(Monster(health, board.path))
        return monster_list

    def get_monster_positions(self):
        positions = []
        for monster in self.list[self.done_count:self.spawn_count]:
            if monster.position is not None:
                positions.append(monster.position)
        return positions

    def move_monsters(self):
        for monster in self.list[self.done_count:self.spawn_count]:
            monster.move()
            if monster.is_done:
                self.done_count += 1

    def spawn_monster(self):
        monster = self.list[self.spawn_count]
        monster.set_name('M' + str(self.spawn_count))
        monster.spawn()
        self.spawn_count += 1

    def get_remaining_health(self):
        remaining_health = 0
        survivors = []
        for monster in self.list:
            if monster.health > 0:
                remaining_health += monster.health
                survivors.append(monster)
        return survivors, remaining_health
