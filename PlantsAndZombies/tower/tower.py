from tower.bullet import Bullet


class Tower:
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col
        self.range = []
        self.bullets = []
        self.is_destroyed = False
        self.tk_obj = None
        self.tk_txt = None

    def __repr__(self):
        return f'Tower(name={self.name}, row={self.row}, col={self.col})'

    def add_bullets(self, rows, cols):
        if self.name == 'S':
            directions = ['diag_up', 'straight', 'diag_down']
        else:
            directions = ['straight'] * int(self.name)

        for direction in directions:
            bullet = Bullet((self.row, self.col), direction, rows, cols)
            self.range.extend(bullet.path)
            self.bullets.append(bullet)

    def fire(self, zombie):
        zombie.hp -= 1
