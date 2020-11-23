from TowerDefence.Monsters.Monsters import Monsters
from TowerDefence.Turrets.Turret import Turret


class Turrets:
    def __init__(self, board, turrets):
        self.max_ammo = 0
        self.list = self.create_turrets(board, turrets)

    def __repr__(self):
        return f'Turrets({[t.name for t in self.list]})'

    def reset_turrets(self):
        for turret in self.list:
            turret.reset()

    def fire_turrets(self, monsters: Monsters, debug=False):
        monster_list = monsters.list[monsters.done_count:monsters.spawn_count]
        for i in range(self.max_ammo):
            for turret in self.list:
                if i == 0:
                    turret.ammo = turret.fire_rate
                if turret.ammo == 0:
                    continue
                for monster in monster_list:
                    alive = monster.is_alive
                    in_range = monster.position in turret.positions_in_range
                    if alive and in_range:
                        turret.fire(monster, debug=debug)
                        break

    def set_targets(self, monsters):
        monster_list = monsters.list[monsters.done_count:monsters.spawn_count]
        for turret in self.list:
            push = turret.targets.append
            for monster in monster_list:
                alive = monster.is_alive
                in_range = monster.position in turret.positions_in_range
                if alive and in_range:
                    push(monster)

    def create_turrets(self, board, turrets):
        output = []

        for name, specs in turrets.items():
            fire_range, fire_rate = specs
            position = board.turret_positions[name]
            output.append(
                Turret(name, position, fire_rate, fire_range, board.path))
            if fire_rate > self.max_ammo:
                self.max_ammo = fire_rate

        sorted_output = sorted(output, key=lambda x: x.name)

        return sorted_output
