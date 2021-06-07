from typing import Optional


class Error(Exception):
    def __init__(self, message=''):
        self.message = message

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.message}'


class InvalidBond(Error):
    pass


class LockedMolecule(Error):
    pass


class EmptyMolecule(Error):
    pass


class UnlockedMolecule(Error):
    pass


class Atom:
    """
    Symbol:           H     B     C     N     O     F    Mg     P     S    Cl    Br
    Valence number:   1     3     4     3     2     1     2     3     2     1     1
    Atomic weight:  1.0  10.8  12.0  14.0  16.0  19.0  24.3  31.0  32.1  35.5  80.0  (in g/mol)
    """
    valid_atoms = {
        'H':  (1, 1.0),
        'B':  (3, 10.8),
        'C':  (4, 12.0),
        'N':  (3, 14.0),
        'O':  (2, 16.0),
        'F':  (1, 19.0),
        'Mg': (2, 24.3),
        'P':  (3, 31.0),
        'S':  (2, 32.1),
        'Cl': (1, 35.5),
        'Br': (1, 80.0),
    }

    def __init__(self, elt, _id):
        atom_details = Atom.valid_atoms.get(elt)
        self._id = _id
        self.element = elt
        self._valence_number = atom_details[0]
        self._weight = atom_details[1]
        self.bonds = []

    def __hash__(self):
        return self.id

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        if len(self.bonds) == 0:
            return f'Atom({self.element}.{self._id})'
        else:
            tmp = []
            for a in self.bonds:
                if a.element != 'H':
                    tmp.append(f'{a.element}{a._id}')
                else:
                    tmp.append(f'{a.element}')
            elements = ','.join(tmp)
            return f'Atom({self.element}.{self._id}: {elements})'

    def __repr__(self):
        return f'Atom({self.element}.{self._id})'

    @property
    def id(self):
        return self._id

    @property
    def weight(self):
        return self._weight

    def add_bond(self, atom):
        if len(self.bonds) > self._valence_number or atom is self:
            raise InvalidBond

        self.bonds.append(atom)
        self.bonds.sort(key=lambda x: x.id)

    def mutate(self, elt):
        atom_details = Atom.valid_atoms.get(elt)
        self.element = elt
        self._valence_number = atom_details[0]
        self._weight = atom_details[1]


class Molecule:
    def __init__(self, name: Optional[str] = ''):
        self._id = 1
        self._name = name
        self.atoms = []
        self._branches = []
        self._locked = False

    def __repr__(self):
        return f'Molecule({self._branches})'

    @property
    def formula(self):
        if not self._locked:
            raise UnlockedMolecule

        counts = {}
        for a in self.atoms:
            if a.element in counts:
                counts[a.element] += 1
            else:
                counts[a.element] = 1

        formula = ''
        for name, count in counts.items():
            if count == 1:
                formula += name
            else:
                formula += f'{name}{count}'

        return formula

    @property
    def molecular_weight(self):
        if not self._locked:
            raise UnlockedMolecule

        return sum(a.weight for a in self.atoms)

    @property
    def name(self):
        return self._name

    def create_atom(self, elt):
        a = Atom(elt, self._id)
        self.atoms.append(a)
        self._id += 1
        return a

    def brancher(self, *args):
        """
        m.brancher(x, y, z, ...)

        Adds new "branches" of carbons, to the current molecule.
        All carbons of one branch are bounded together (chained).
        Each argument gives the number of carbons of one branch.
        There can be any number of arguments.
        All branches have to be created in the provided order.
        """
        if self._locked:
            raise LockedMolecule

        for arg in args:
            branch = []
            prev_atom = None

            for a in range(arg):
                curr_atom = self.create_atom('C')
                if prev_atom is None:
                    prev_atom = curr_atom
                    branch.append(curr_atom)
                else:
                    try:
                        prev_atom.add_bond(curr_atom)
                        curr_atom.add_bond(prev_atom)
                    except InvalidBond:
                        break

                    branch.append(curr_atom)

                    prev_atom = curr_atom

            self._branches.append(branch)

        return self

    def bounder(self, *args):
        """
        m.bounder((c1,b1,c2,b2), ...)

        Creates new bonds between two atoms of already existing branches.
        Each argument is a tuple of four integers giving:
        c1 & b1: carbon and branch number of the first atom
        c2 & b2: carbon and branch number of the second atom
        All numbers are 1-indexed, meaning (1,1,5,3) will bound the first carbon of the first branch with the fifth of the third branch.
        Only positive numbers will be used.
        :param args: tuple(c1, b1, c2, b2)
        """
        if self._locked:
            raise LockedMolecule

        assert all(n > 0 for arg in args for n in arg), 'All numbers must be positive'

        for arg in args:
            c1, b1, c2, b2 = arg

            try:
                a1 = self._branches[b1 - 1][c1 - 1]
                a2 = self._branches[b2 - 1][c2 - 1]
                a1.add_bond(a2)
                a2.add_bond(a1)
            except (InvalidBond, IndexError):
                break

        return self

    def mutate(self, *args):
        """
        m.mutate((nc,nb,elt), ...)

        Mutates the carbon numbered `nc` in the branch numbered `nb` to the chemical element `elt`, as a string.
        Don't forget that carbons and branches are 1-indexed
        This is mutation: the id number of the Atom instance stays the same. See the Atom class specs about that.
        :param args: tuple(nc, nb, elt)
        """
        if self._locked:
            raise LockedMolecule

        for arg in args:
            nc, nb, elt = arg
            try:
                a = self._branches[nb - 1][nc - 1]
                a.mutate(elt)
            except IndexError:
                break

        return self

    def add(self, *args):
        """
        m.add((nc,nb,elt), ...)

        Adds a new Atom of kind elt (string) on the carbon number nc in the branch nb.
        Atoms added this way are not considered as being part of the branch they are bounded to.
        :param args: tuple(nc, nb, elt)
        """
        if self._locked:
            raise LockedMolecule

        for arg in args:
            nc, nb, elt = arg
            try:
                a = self._branches[nb - 1][nc - 1]
            except IndexError:
                break

            na = self.create_atom(elt)
            a.add_bond(na)

        return self

    def add_chaining(self, *args):
        """
        m.add_chaining(nc, nb, elt1, elt2, ...)

        Adds all the elements provided as arguments one after the other, starting from the carbon nc in the branch nb.
        Meaning: m.add_chaining(2, 5, "C", "C", "C", "Mg", "Br") will add the chain ...-C-C-C-Mg-Br to the atom number 2 in the branch 5.
        As for the add method, this chain is not considered as a new branch of the molecule.
        :param args:
        """
        if self._locked:
            raise LockedMolecule

        nc, nb = args[:2]
        try:
            a = self._branches[nb - 1][nc - 1]
        except IndexError:
            return

        tmp = [a]
        for elt in args[2:]:
            a = self.create_atom(elt)
            tmp.append(a)

        for a1, a2 in zip(tmp[1:], tmp[:-1]):
            a1.add_bond(a2)
            a2.add_bond(a1)

        return self

    def closer(self):
        """
        Finalizes the molecule instance, adding missing hydrogens everywhere and locking the object (see behaviors part below).
        """
        if self._locked:
            raise LockedMolecule
        atoms = self.atoms.copy()
        hydrogens = []
        for a in atoms:
            remaining_slots = a._valence_number - len(a.bonds)

            if remaining_slots != 0:
                for _ in range(remaining_slots):
                    h = self.create_atom('H')
                    a.add_bond(h)
                    h.add_bond(a)
                    hydrogens.append(h)

            hydrogens = []

        self.atoms.extend(hydrogens)
        self._locked = not self._locked

        return self

    def unlock(self):
        """
        Makes the molecule mutable again.
        Hydrogens should be removed, as well as any empty branch you might encounter during the operation.
        After unlocking a molecule, if by any (bad...) luck it does not have any branch left,
        throw an EmptyMolecule exception.
        The id numbers of the remaining atoms are to be modified so that they are continuous (beginning at 1),
        keeping the order they had before unlocking the molecule.
        If when removing hydrogens you end up with some atoms that aren't connected in any way to the branches of the
         unlocked molecule, keep them anyway in the Molecule instance (for the sake of simplicity...).
        Once unlocked, the molecule has to be modifiable again, in any way.
        :return:
        """
        if not self._locked:
            raise UnlockedMolecule

        self._locked = not self._locked
