from tower_defence.tower_defence import tower_defence

if __name__ == '__main__':
    battlefield = [
        '0111111',
        '  A  B1',
        ' 111111',
        ' 1     ',
        ' 1C1111',
        ' 111 D1',
        '      1'
    ]

    turrets = {
        'A': [3, 2],
        'B': [1, 4],
        'C': [2, 2],
        'D': [1, 3]
    }

    wave = [30, 14, 27, 21, 13, 0, 15, 17, 0, 18, 26]

    print(f'Remaining Health: {tower_defence(battlefield, turrets, wave)}')
