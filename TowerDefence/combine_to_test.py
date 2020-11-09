from typing import List


def write_solution(output_file: str, input_files: List):
    o = open(output_file, 'w')
    for file in input_files:
        f = open(file, 'r')

        fl = f.readlines()
        for line in fl:
            if line.startswith('from TowerDefence'):
                continue
            o.write(line)

        o.write('\n')

        f.close()
    o.close()
