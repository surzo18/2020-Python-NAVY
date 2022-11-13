import random
import numpy as np
from enum import Enum
import copy
from Utils.drawUtils import draw_forest_fire


class State(Enum):
    Empty = 0
    Tree = 1
    Burning = 2


empty_to_tree_p = 0.005
tree_to_burning = 0.0001
total_iterations = 300
forest_size = 100

forest = np.array([np.random.choice(np.arange(0, 2), size=forest_size, p=[0.2, 0.8]) for _ in range(forest_size)])
forest[random.randint(1, forest_size), random.randint(1, forest_size)] = 2

forest_evolving = []


for iteration in range(0, total_iterations):

    copied_forest = copy.deepcopy(forest)
    for i_row in range(0, forest_size):
        for i_column in range(0, forest_size):
            random_number = random.uniform(0, 1)

            # empty space
            if copied_forest[i_row, i_column] == 0:
                if random_number < empty_to_tree_p:
                    forest[i_row, i_column] = 1
                    continue

            # burning
            if copied_forest[i_row, i_column] == 2:
                forest[i_row, i_column] = 0
                continue

            # tree
            if copied_forest[i_row, i_column] == 1:

                # check boundries
                if i_column != 0:
                    if copied_forest[i_row, i_column - 1] == 2:
                        forest[i_row, i_column] = 2
                        continue

                if i_column != forest_size - 1:
                    if copied_forest[i_row, i_column + 1] == 2:
                        forest[i_row, i_column] = 2
                        continue

                if i_row != 0:
                    if copied_forest[i_row - 1, i_column] == 2:
                        forest[i_row, i_column] = 2
                        continue

                if i_row != forest_size -1:
                    if copied_forest[i_row + 1, i_column] == 2:
                        forest[i_row, i_column] = 2
                        continue

                if random_number < tree_to_burning:
                    forest[i_row, i_column] = 2
                    continue

    forest_evolving.append(copy.deepcopy(forest))

draw_forest_fire(forest_evolving, total_iterations)
