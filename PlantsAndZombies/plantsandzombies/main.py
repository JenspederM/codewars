# from drawer.drawer import Drawer
from game.game import Game
from examples import grab_example, examples


files = [
    "./PlantsAndZombies/tower/bullet.py",
    "./PlantsAndZombies/tower/tower.py",
    "./PlantsAndZombies/zombie/zombie.py",
    "./PlantsAndZombies/game/game.py",
]

DEBUG = False

if __name__ == "__main__":
    for i in range(len(examples)):
        board, zombies, solution = grab_example(i)
        game = Game(board, zombies)
        print(f"Running example {i + 1}...", game)
        if DEBUG is True:
            drawer = Drawer(game)
            drawer.mainloop()
        else:
            print(
                f"Game finished on move {game.solution}. It should finish on move {solution}"
            )
