from TowerDefence.TowerDefence import TowerDefence

example_tests = [
    [
        [
            '0111111',
            '  A  B1',
            ' 111111',
            ' 1     ',
            ' 1C1111',
            ' 111 D1',
            '      1'],
        {'A': [3, 2], 'B': [1, 4], 'C': [2, 2], 'D': [1, 3]},
        [30, 14, 27, 21, 13, 0, 15, 17, 0, 18, 26]
    ],
    [
        [
            '011  1111',
            ' A1  1BC1',
            ' 11  1 11',
            ' 1D  1 1E',
            ' 111 1F11',
            '  G1 1  1',
            ' 111 1 11',
            ' 1H  1 1I',
            ' 11111 11'],
        {
            'A': [1, 4], 'B': [2, 2], 'C': [1, 3], 'D': [1, 3], 'E': [1, 2],
            'F': [3, 3], 'G': [1, 2], 'H': [2, 3], 'I': [2, 3]
        },
        [36, 33, 46, 35, 44, 27, 25, 48, 39, 0, 39, 36, 55, 22, 26]
    ],
    [
        [
            '01111111',
            ' A    B1',
            '11111111',
            '1 C D E ',
            '1 111111',
            '1 1F  G1',
            '1H1 1111',
            '111 1   '],
        {
            'A': [2, 2], 'B': [1, 3], 'C': [3, 3], 'D': [1, 2], 'E': [1, 4],
            'F': [2, 3], 'G': [1, 3], 'H': [2, 2]
        },
        [37, 29, 16, 13, 42, 39, 8, 14, 35, 26, 59, 0, 44, 19, 17, 35, 49, 31,
         0, 43]
    ],
    [
        [
            '1111111111',
            '1A      B1',
            '111C111111',
            '  1 1D    ',
            '011E111111',
            '        F1',
            'G1111111 1',
            '11  H  111',
            '1 I111  J ',
            '1111K11111'],
        {
            'A': [1, 2], 'B': [1, 4], 'C': [1, 3], 'D': [2, 2], 'E': [3, 3],
            'F': [1, 3], 'G': [2, 2], 'H': [1, 3], 'I': [2, 2], 'J': [1, 3],
            'K': [1, 2]
        },
        [36, 27, 19, 35, 0, 60, 0, 80, 35, 18, 49, 53, 0, 47, 0, 62, 0, 34, 26,
         53, 35, 0, 31, 44, 64, 21, 31, 0, 59, 30, 53, 31, 42, 39]
    ],
    [
        [
            '11111111111',
            '1A  B   C 0',
            '111 111111 ',
            ' D1 1E   1 ',
            '111 1 1111 ',
            '1F  1 1    ',
            '1 111 1G111',
            '1 1 H 1 1I1',
            '1J1 111 1 1',
            '111 1K  1 1',
            '    11111 1'],
        {
            'A': [1, 3], 'B': [1, 2], 'C': [2, 2], 'D': [1, 4], 'E': [4, 2],
            'F': [2, 2], 'G': [3, 2], 'H': [1, 2], 'I': [1, 2], 'J': [2, 3],
            'K': [1, 3]
        },
        [50, 40, 25, 54, 26, 0, 64, 21, 36, 35, 0, 24, 38, 0, 69, 32, 56, 24,
         33, 63, 19, 56, 39, 43, 28, 11, 42, 32, 51, 43, 27, 0, 42, 0, 0, 65,
         24, 28, 38, 29, 0, 45, 34, 27, 44]
    ]
]

example_solutions = [[10, [7, 2], [8, 8]],
                     [3, [11, 3]],
                     [12, [15, 12]],
                     [21, [18, 8], [21, 3], [23, 9], [25, 1]],
                     [30, [16, 5], [18, 9], [20, 4], [25, 7], [26, 4], [37, 1]]]

files = [
    './TowerDefence/Monsters/Monster.py',
    './TowerDefence/Turrets/Turret.py',
    './TowerDefence/Monsters/Monsters.py',
    './TowerDefence/Turrets/Turrets.py',
    './TowerDefence/Board/Board.py',
    './TowerDefence/TowerDefence.py',
]

if __name__ == '__main__':
    run_all = False
    run_example = 4

    if run_all:
        for test in example_tests[1]:
            battlefield = test[0]
            turrets = test[1]
            wave = test[2]
            td = TowerDefence(battlefield, turrets, wave)
            td.simulate_wave(debug=True)
    else:
        test = example_tests[run_example]
        solution = example_solutions[run_example]
        battlefield = test[0]
        turrets = test[1]
        wave = test[2]
        td = TowerDefence(battlefield, turrets, wave)
        td.simulate_wave(debug=True)
# for i in range(100): td.simulate_wave(debug=False)
print(td.test_solution(solution))

# write_solution(output_file='test.py', input_files=files)
