class Zombie:
    def __init__(self, entry_move, row, hp):
        self.entry_move = entry_move
        self.hp = hp
        self.row = row
        
        self.col = None
        self.tk_obj = None
        self.tk_txt = None

    def __repr__(self):
        return f'Zombie(move={self.entry_move}, row={self.row}, col={self.col}, hp={self.hp})'
