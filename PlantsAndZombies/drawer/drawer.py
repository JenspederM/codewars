from tkinter import *

from game.game import Game
from drawer.config import GREEN_COLOR, BLUE_COLOR, RED_COLOR


class Drawer:
    def __init__(self, game: Game, row_height: int = 100, col_width: int = 100, delay: int = 100):
        self.board = game
        self.rows = game.rows
        self.cols = game.cols
        self.row_height = row_height
        self.col_width = col_width
        self.delay = delay

        self.size_of_board = (self.rows * self.row_height,
                              self.cols * self.col_width)

        self.window = Tk()
        self.window.title('Plants Vs Zombies')
        self.header = Frame(self.window)
        self.game_board = Frame(self.window)

        self.__move_str = StringVar(self.header)
        self.__move_str.set(f'Game Started!')
        label = Label(self.header, textvariable=self.__move_str)
        label.pack(side=LEFT)
        self.window.bind('<Button-1>', self.advance_game)
        self.canvas = Canvas(self.game_board, width=self.size_of_board[1], height=self.size_of_board[0],
                             highlightthickness=1, highlightbackground="black")

        self.header.pack()
        self.game_board.pack()
        self.canvas.pack()

        self.game_started = False
        self.game_over = False

        self.initialize_game()

    def advance_game(self, event):
        self.board.advance()
        self.redraw_elements()
        self.__move_str.set(f'Move = {self.board.move}')

    def redraw_elements(self):
        for zombie in self.board.zombies.values():
            if zombie.entry_move <= self.board.move and zombie.hp >= 0:
                tower = self.board.towers.get((zombie.row, zombie.col))

                if tower is not None:
                    self.canvas.delete(tower.tk_obj)
                    self.canvas.delete(tower.tk_txt)

                self.canvas.delete(zombie.tk_obj)
                self.canvas.delete(zombie.tk_txt)

                self.place_element(
                    zombie, shape='oval', fill=RED_COLOR, outline='black', text=zombie.hp)
            else:
                self.canvas.delete(zombie.tk_obj)
                self.canvas.delete(zombie.tk_txt)

    def initialize_game(self):
        rows = self.rows
        cols = self.cols
        row_h = self.row_height
        col_w = self.col_width

        # Draw Rows Lines
        for i in range(rows):
            val = i * row_h
            self.canvas.create_line(0, val, self.size_of_board[1], val)

        # Draw Column Lines
        for i in range(cols):
            val = i * col_w
            self.canvas.create_line(val, 0, val, self.size_of_board[0])

        self.place_towers()

    def place_towers(self):
        for tower in self.board.towers.values():
            if tower.name == 'S':
                color = GREEN_COLOR
            else:
                color = BLUE_COLOR
            self.place_element(tower, shape='rectangle',
                               fill=color, outline='black', text=tower.name)

    def place_element(self, obj, shape, fill, outline, text):
        row = obj.row
        col = obj.col
        row_h = self.row_height
        col_w = self.col_width
        x0 = col * col_w
        y0 = row * row_h
        x1 = x0 + col_w
        y1 = y0 + row_h

        if shape == 'rectangle':
            tk_obj = self.canvas.create_rectangle(
                x0, y0, x1, y1, fill=fill, outline=outline)
        else:
            tk_obj = self.canvas.create_oval(
                x0, y0, x1, y1, fill=fill, outline=outline)

        obj.tk_txt = self.canvas.create_text(
            (x0 + (col_w / 2), y0 + (row_h / 2)), text=text)
        obj.tk_obj = tk_obj
        return tk_obj

    def mainloop(self):
        while not self.board.game_over:
            self.window.update()
