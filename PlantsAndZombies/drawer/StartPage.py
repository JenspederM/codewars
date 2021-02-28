import tkinter as tk
from tkinter import ttk

from PlantsAndZombies.examples import grab_example
from PlantsAndZombies.game.game import Game


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        self.tree = None
        self.__n_examples = 5

        self.construct_ui()

    def construct_ui(self):
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.config(background="lavender")

        label = tk.Label(self, text="Start Page", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.tree = ttk.Treeview(self)
        self.tree['columns'] = ('rows', 'cols', 'towers', 'zombies')
        for i in range(self.__n_examples):
            self.add_example(i)
        self.tree.bind('<ButtonRelease-1>', self.select_item)

        button1 = tk.Button(self, text="Start Game", command=lambda: self.controller.show_frame("GamePage"))
        button1.pack(side='bottom')

    def select_item(self, event):
        current_item = self.tree.focus()
        print(self.tree.item(current_item))

    def add_example(self, n):
        example_game = Game(*grab_example(n))
        game_id = f'game_{n}'
        self.tree.insert('', 'end', game_id, text=f'Game {n + 1}')
        self.tree.heading('rows', text='Rows')
        self.tree.heading('cols', text='Cols')
        self.tree.heading('towers', text='Towers')
        self.tree.heading('zombies', text='Zombies')
        self.tree.set(game_id, 'rows', example_game.rows)
        self.tree.set(game_id, 'cols', example_game.cols)
        self.tree.set(game_id, 'towers', len(example_game.towers))
        self.tree.set(game_id, 'zombies', len(example_game.input_zombies))
        self.tree.pack()
