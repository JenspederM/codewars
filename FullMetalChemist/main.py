from FullMetalChemist.Molecule import Molecule

if __name__ == "__main__":
    m = Molecule("").brancher(3).bounder((1, 1, 2, 1))
    m.mutate((2, 1, 'N'))
    m.add((2, 1, 'O'))
    print(m)
