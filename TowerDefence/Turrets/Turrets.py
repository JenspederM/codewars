from TowerDefence.Monsters.Monsters import Monsters
from TowerDefence.Turrets.Turret import Turret


class Turrets:
    def __init__(self, board, turrets):
        self.max_fire_rate = 0
        self.list = self.create_turrets(board, turrets)

    def __repr__(self):
        return f'Turrets({[t.name for t in self.list]})'

    def find_monsters_in_range(self, monsters: Monsters):
        for turret in self.list:
            for monster in monsters.list:
                if turret.in_range2(monster.position):
                    turret.monsters_in_range.append(monster)
            if turret.has_monsters_in_range():
                turret.reload()

    def reset_turrets(self):
        for turret in self.list:
            turret.reset()

    def fire_turrets(self, monsters: Monsters, debug=False):
        monster_list = monsters.list[monsters.done_count:monsters.spawn_count]
        for _ in range(self.max_fire_rate):
            for turret in self.list:
                if turret.ammo == 0:
                    continue
                for monster in monster_list:
                    alive = monster.is_alive
                    in_range = turret.in_range2(monster.position)
                    if alive and in_range:
                        turret.fire(monster, debug=debug)
                        break

    def create_turrets(self, board, turrets):
        output = []

        for name, specs in turrets.items():
            fire_range, fire_rate = specs
            position = board.turret_positions[name]
            output.append(
                Turret(name, position, fire_rate, fire_range, board.path))
            if fire_rate > self.max_fire_rate:
                self.max_fire_rate = fire_rate

        sorted_output = sorted(output, key=lambda x: x.name)

        return sorted_output
