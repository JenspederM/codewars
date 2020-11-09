class Monster:
    __slots__ = ['health', 'path', 'path_length', 'name', 'position',
                 'path_index', 'is_alive', 'is_done']

    def __init__(self, health, path):
        self.health = health
        self.path = path
        self.path_length = len(self.path)
        self.name = None
        self.position = None
        self.path_index = None
        self.is_alive = False
        self.is_done = False

    def __repr__(self):
        return f'Monster(Name: {self.name}, Health: {self.health}, Position: ' \
               f'{self.position}, Is Alive: {self.is_alive})'

    def set_name(self, name):
        self.name = name

    def spawn(self):
        self.position = self.path[0]
        self.path_index = 0
        if self.health > 0:
            self.is_alive = True

    def move(self):
        self.path_index += 1
        if self.path_index == self.path_length:
            self.is_alive = False
            self.position = None
            self.is_done = True
        else:
            self.position = self.path[self.path_index]

    def afflict_damage(self):
        self.health -= 1
        if self.health == 0:
            self.is_alive = False
