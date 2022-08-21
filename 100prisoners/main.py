## 100 Prisoners Problem
##
## To describe the strategy, not only the prisoners, but also the drawers, are numbered from 1 to 100;
## for example, row by row starting with the top left drawer. The strategy is now as follows:[3]
##
## 1. Each prisoner first opens the drawer labeled with his own number.
## 2. If this drawer contains his number, he is done and was successful.
## 3. Otherwise, the drawer contains the number of another prisoner, and he next opens the drawer labeled with this number.
## 4. The prisoner repeats steps 2 and 3 until he finds his own number or has opened fifty drawers.

# Graph ?

# Prisoner
## Part of strategy

# Boxes
## Boxes contain slips of paper with
## Box ID is the number on the box
## Slip is the number on the note within the box
import random
import math

import networkx as nx

import matplotlib.pyplot as plt


class Map:
    """Map
    Map contains boxes
    """

    def __init__(self, n: int = 100) -> None:
        self.map_size = n
        values = list(range(1, n + 1))
        random.shuffle(values)
        self.boxes = [(i, values[i - 1]) for i in range(1, n + 1)]
        random.shuffle(self.boxes)

    def print_overlay(self) -> None:
        print(self._get_map(0))

    def print_content(self) -> None:
        print(self._get_map(1))

    def _get_map(self, type=0) -> str:
        s = "Boxes\n\n" if type == 0 else "Slips\n\n"
        ncol = math.floor(math.sqrt(self.map_size))

        for idx, box in enumerate(self.boxes):
            s += f"{box[type]:<4}"
            if (idx + 1) % ncol == 0:
                s += "\n"

        return s


if __name__ == "__main__":
    n = 100
    G = nx.Graph()
    G.add_nodes_from(range(1, n + 1))
    G.add_edges_from([(i, i) for i in range(1, n + 1)])
    nx.draw(G, with_labels=True)
    print(G)
