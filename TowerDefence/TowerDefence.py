from TowerDefence.Board.Board import Board
from TowerDefence.Monsters.Monsters import Monsters
from TowerDefence.Turrets.Turrets import Turrets


class TowerDefence:
    def __init__(self, board, turrets, wave,
                 start_symbol='0', path_symbol='1', empty_symbol=' '):
        self.board = Board(board, start_symbol, path_symbol, empty_symbol)
        self.turrets = Turrets(self.board, turrets)
        self.monsters = Monsters(self.board, wave)
        self.steps = len(self.board.path) + len(wave)

    def __repr__(self):
        return f'Board: {self.board.__repr__()} \n' \
               f'Turrets: {self.turrets.__repr__()} \n' \
               f'Monsters: {self.monsters.__repr__()}'

    def step(self, debug=True):
        self.turrets.reset_turrets()
        if debug:
            print('-' * 50)
        if self.monsters.spawn_count < self.monsters.wave_length:
            self.monsters.move_monsters()
            self.monsters.spawn_monster()
        else:
            self.monsters.move_monsters()

        if debug:
            print('')
            self.board.print_updated_board(self.monsters)
            print('')

        self.turrets.fire_turrets(self.monsters, debug=debug)
        if debug:
            print('-' * 50)

    def simulate_wave(self, debug=True):
        if debug:
            print('Simulating waves on:')
            self.board.print_updated_board(self.monsters)
        if debug:
            print('')
            print('')

        for _ in range(self.steps):
            if _ == 23:
                print('')
            if debug:
                print(f'Step: {_}')
            self.step(debug=debug)
        survivors, remaining_health = self.monsters.get_remaining_health()
        if debug:
            print(f'{[[m.name, m.health] for m in survivors]} survived with a '
                  f'total remaining health of {remaining_health}')
        return remaining_health

    def test_solution(self, solution):
        survivors, remaining_health = self.monsters.get_remaining_health()
        outcome = []
        for index, health in solution[1:]:
            monster = self.monsters.list[index + 1]
            outcome.append([[index, health], [index, monster.health]])

        return [remaining_health == solution[0]] + outcome
