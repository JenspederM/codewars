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
        'left':  [i, j - 1],
        'right': [i, j + 1],
        'up':    [i - 1, j],
        'down':  [i + 1, j]
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
                    'position':           position,
                    'fire_range':         fire_range,
                    'fire_rate':          fire_range,
                    'positions_in_range': positions_in_range,
                    'bullets':            fire_rate
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


def in_range(from_pos, to_pos, limit):
    return calculate_euclidean_distance(from_pos, to_pos) <= limit


def start_monster(monsters, path):
    for key, value in monsters.items():
        if value['position'] is None:
            monsters[key]['position'] = path[0]
            monsters[key]['path_idx'] = 0
            break


def move_monsters(monsters, path):
    for key, value in monsters.items():
        if value['position'] is None:
            break
        monsters[key]['path_idx'] += 1
        monsters[key]['position'] = path[value['path_idx'] - 1]


def remove_monsters(monsters, path):
    to_remove = []
    remaining_health = 0
    for monster, data in monsters.items():
        if data['path_idx'] is None:
            break
        if data['path_idx'] == len(path):
            remaining_health += data['health']
            to_remove.append(monster)
        if data['health'] == 0:
            to_remove.append(monster)

    if len(to_remove) > 0:
        for monster in to_remove:
            del monsters[monster]

    return remaining_health


def turret_monster_pairs(turrets, monsters):
    pairs = []
    for t, td in turrets.items():
        if td['bullets'] == 0:
            continue
        for m, md in monsters.items():
            if md['health'] == 0:
                continue

            t_pos = td['position']
            t_range = td['fire_range']
            m_pos = md['position']

            if m_pos is None:
                break

            if in_range(t_pos, m_pos, t_range):
                pairs.append((t, m))
                break

    if 0 < len(pairs):
        return pairs


def fire_turrets(turrets, monsters):
    done = False
    while done is False:
        pairs = turret_monster_pairs(turrets, monsters)

        if pairs is not None:
            for pair in pairs:
                t, m = pair
                turrets[t]['bullets'] -= 1
                monsters[m]['health'] -= 1
        else:
            done = True


def reload_turrets(turrets):
    for turret, data in turrets.items():
        turrets[turret]['bullets'] = turrets[turret]['fire_rate']


def update_row(battlefield, x, y, mod):
    row = list(battlefield[x])
    row[y] = str(mod)
    return ''.join(row)


def print_battlefield(battlefield, turrets, monsters):
    battlefield = list(battlefield)
    for t, td in turrets.items():
        i, j = td['position']
        battlefield[i] = update_row(battlefield, i, j, t)
        for m, md in monsters.items():
            m_pos = md['position']
            if m_pos is None:
                break
            i, j = m_pos
            health = md['health']
            battlefield[i] = update_row(battlefield, i, j, health)
    print('\n'.join(battlefield))


def tower_defence(battlefield, turrets, wave):
    path = find_path(battlefield)
    print(f'Monsters will run along {path}')
    turret_data = create_turret_data(battlefield, turrets, path)
    print(f'Turrets: {turret_data}')
    monster_data = create_monster_data(wave)
    t = 0
    remaining_health = 0
    incomplete = True
    while incomplete:
        t += 1  # increment time
        print_battlefield(battlefield, turret_data, monster_data)
        move_monsters(monster_data, path)  # move
        start_monster(monster_data, path)
        fire_turrets(turret_data, monster_data)  # fire
        print(f'Monsters: {monster_data}')
        reload_turrets(turret_data)  # reload
        remaining_health += remove_monsters(monster_data,
                                            path)
    return remaining_health
