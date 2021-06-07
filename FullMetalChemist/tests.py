import unittest

from FullMetalChemist.Molecule import Molecule, Atom


class ConstructorTests(unittest.TestCase):
    def test_constructor(self):
        m = Molecule()
        self.assertEqual(m.name, '', "Should define the empty string as default name")

        m = Molecule("banana")
        self.assertEqual(m.name, 'banana', "Even if...")

    def test_biotin(self):
        print('-' * 50 + ' Running Biotin Test ' + '-' * 50)
        biotin = Molecule("biotin")

        biotin.brancher(14, 1, 1)
        self.assertEqual(len(biotin._branches), 3)
        self.assertEqual(len(biotin._branches[0]), 14)
        self.assertEqual(len(biotin._branches[1]), 1)
        self.assertEqual(len(biotin._branches[2]), 1)

        for branch in biotin._branches:
            for a in branch:
                self.assertEqual(type(a), Atom)
                self.assertEqual(a.element, 'C')

        biotin.bounder((2, 1, 1, 2), (2, 1, 1, 2),
                       (10, 1, 1, 3), (10, 1, 1, 3),
                       (8, 1, 12, 1), (7, 1, 14, 1))

        self.assertIn(biotin._branches[0][1], biotin._branches[1][0].bonds)
        self.assertIn(biotin._branches[1][0], biotin._branches[0][1].bonds)
        self.assertIn(biotin._branches[0][9], biotin._branches[2][0].bonds)
        self.assertIn(biotin._branches[2][0], biotin._branches[0][9].bonds)
        self.assertIn(biotin._branches[0][7], biotin._branches[0][11].bonds)
        self.assertIn(biotin._branches[0][11], biotin._branches[0][7].bonds)

        print('- Bounder passed all tests')

        biotin.mutate((1, 1, 'O'), (1, 2, 'O'), (1, 3, 'O'),
                      (11, 1, 'N'), (9, 1, 'N'), (14, 1, 'S'))

        self.assertEqual(biotin._branches[0][0].element, 'O')
        self.assertEqual(biotin._branches[1][0].element, 'O')
        self.assertEqual(biotin._branches[2][0].element, 'O')
        self.assertEqual(biotin._branches[0][10].element, 'N')
        self.assertEqual(biotin._branches[0][8].element, 'N')
        self.assertEqual(biotin._branches[0][13].element, 'S')

        biotin.closer()

        self.assertEqual(biotin.formula, "C10N2O3S")

    def test_simple_carbonates(self):
        methane = Molecule("methane").brancher(1).closer()
        self.assertEqual(methane.formula, 'CH4')
        self.assertEqual(methane.molecular_weight, 16)

        octane = Molecule("octane").brancher(8).closer()
        self.assertEqual(octane.formula, 'C8H18')
        self.assertEqual(octane.molecular_weight, 114)


if __name__ == '__main__':
    unittest.main()
