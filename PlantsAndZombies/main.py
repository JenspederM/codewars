from PlantsAndZombies.drawer.drawer import Drawer
from game.game import Game
from examples import example_tests
from utilities import grab_example

if __name__ == '__main__':
    board, zombies = grab_example(example_tests, 0)
    game = Game(board, zombies)
    drawer = Drawer(game)
    drawer.mainloop()
