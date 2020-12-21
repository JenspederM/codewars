class Tower:
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col
        self.range = []
        self.targets = []
        self.ammo = None
        self.tk_obj = None
        self.tk_txt = None

        self.reload()

    def __repr__(self):
        return f'Tower(name={self.name}, row={self.row}, col={self.col})'

    def set_range(self, rows, cols):
        row = self.row
        col = self.col
        i_up = row
        i_down = row
        for j in range(col + 1, cols):
            self.range.append((row, j))
            if self.name == 'S':
                i_up += 1
                i_down -= 1
                if i_up < rows:
                    self.range.append((i_up, j))
                if i_down >= 0:
                    self.range.append((i_down, j))

    def reload(self):
        if self.name == 'S':
            self.ammo = 3
        else:
            self.ammo = int(self.name)

    def fire(self, zombie):
        zombie.hp -= 1
        self.ammo -= 1
