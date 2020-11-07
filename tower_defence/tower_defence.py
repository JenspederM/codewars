from math import sqrt


def find_start(board, start_symbol='0'):
    for i, line in enumerate(board):
        lookup = line.find(start_symbol)
        if lookup != -1:
            return [i, lookup]


def get_next_pos(last_pos, cur_pos, board, path_id='1'):
    n = len(board) - 1

    i, j = cur_pos

    directions = {
        'left' : [i, j - 1],
        'right': [i, j + 1],
        'up'   : [i - 1, j],
        'down' : [i + 1, j]
    }

    for key, next_pos in directions.items():
        x, y = next_pos
        if 0 <= x <= n and \
                0 <= y <= n and \
                board[x][y] == path_id and \
                next_pos != last_pos:
            return next_pos

    return None  # When there are no possible directions, i.e. the path ends


def find_path(board, path_id='1'):
    start = find_start(board)
    path = [start, get_next_pos(start, start, board, path_id)]

    while True:
        pos = get_next_pos(path[-2], path[-1], board, path_id)
        if pos is not None:
            path.append(pos)
        else:
            break

    return path


def create_turret_data(board, turrets, path):
    data = {}
    for key, value in turrets.items():
        for i, line in enumerate(board):
            lookup = line.find(key)
            if lookup != -1:
                position = [i, lookup]
                fire_range, fire_rate = value
                positions_in_range = []
                for p in path:
                    dist = calculate_euclidean_distance(position, p)
                    if dist <= fire_range:
                        positions_in_range.append(p)
                data[key] = {
                    'position'          : position,
                    'fire_range'        : fire_range,
                    'fire_rate'         : fire_range,
                    'positions_in_range': positions_in_range,
                    'bullets'           : fire_rate
                }
                break
    return data


def create_monster_data(wave):
    data = {}
    for i, health in enumerate(wave):
        data[i] = {'health': health, 'position': None, 'path_idx': None}
    return data


def calculate_euclidean_distance(from_pos, to_pos):
    return sqrt((to_pos[0] - from_pos[0]) ** 2 + (to_pos[1] - from_pos[1]) ** 2)


def start_monster(monsters, path):
    for key, value in monsters.items():
        if value['position'] is None:
            monsters[key]['position'] = path[0]
            monsters[key]['path_idx'] = 0


def move_monsters(monsters, path, t):
    assert t > 0, 'time must be a positive integer'
    i = t - 1
    remaining_health = 0
    for key, value in monsters.items():
        if value['position'] == path[-1]:
            remaining_health += value['health']
        else:
            if value['position'] is None:
                break
            monsters[key]['position'] = path[i]
            monsters[key]['path_idx'] = i
        i -= 1
        if i < 0:
            break
    return remaining_health


def remove_monsters(monsters, path):
    to_remove = []
    for monster, data in monsters.items():
        if data['path_idx'] is None:
            break
        if data['health'] == 0 or data['path_idx'] >= len(path):
            to_remove.append(monster)

    if len(to_remove) > 0:
        for monster in to_remove:
            del monsters[monster]


def fire_turrets(turrets, monsters):
    turret_with_ammo = len(turrets)
    while turret_with_ammo > 0:
        for monster, mdata in monsters.items():
            monster_position = mdata['position']
            if monster_position is None:  # Monster not yet on path
                break

            for turret, tdata in turrets.items():
                if tdata['bullets'] == 0:
                    turret_with_ammo -= 1
                    continue

                if monster_position in tdata['positions_in_range']:
                    turrets[turret]['bullets'] -= 1
                    monsters[monster]['health'] -= 1


def reload_turrets(turrets):
    for turret, data in turrets.items():
        turrets[turret]['bullets'] = turrets[turret]['fire_rate']


def tower_defence(battlefield, turrets, wave):
    path = find_path(battlefield)
    print(f'Monsters will run along {path}')
    turret_data = create_turret_data(battlefield, turrets, path)
    print(f'Turrets: {turret_data}')
    monster_data = create_monster_data(wave)
    t = 0
    remaining_health = 0
    while len(monster_data) > 0:
        t += 1  # increment time
        start_monster(monster_data, path)
        remaining_health += move_monsters(monster_data, path, t)  # move
        fire_turrets(turret_data, monster_data)  # fire
        print(f'Monsters: {monster_data}')
        reload_turrets(turret_data)  # reload
        remove_monsters(monster_data, path)  # remove dead or finished monsters
    return remaining_health
