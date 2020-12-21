class Bullet:
    def __init__(self, tower_position, direction, max_rows, max_cols):
        assert direction in ['straight', 'diag_up', 'diag_down']
        self.direction = direction
        self.path = self.__set_path(tower_position, max_rows, max_cols)
        self.fired = False

    def __repr__(self):
        return f'Bullet({self.direction}, {self.path})'

    def __set_path(self, tower_position, max_rows, max_cols):
        row = tower_position[0]
        col = tower_position[1]

        path = []
        for j in range(col, max_cols):
            if self.direction == 'straight':
                path.append((row, j))
            elif self.direction == 'diag_up':
                row += 1
                if row < max_rows:
                    path.append((row, j))
            else:
                row -= 1
                if row >= 0:
                    path.append((row, j))

        return path
