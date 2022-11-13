import copy

import numpy as np

from Utils.drawUtils import draw_matrix

eight_pattern = np.array([[0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]])
x_pattern = np.array([[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]])
h_pattern = np.array([[0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0]])
broken_eight_pattern = np.array([[0, 0, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 0], [0, 1, 1, 1, 1]])

class Hopfield:
    def __init__(self):
        self.weight = []

    def train(self, pattern):
        pattern[pattern == 0] = -1
        column_vector = pattern.flatten()
        self.weight = np.outer(column_vector, column_vector.T)
        np.fill_diagonal(self.weight, 0)

    def recover_sync(self, broken_pattern):
        flatted_pattern = np.dot(self.weight, broken_pattern.flatten())
        recovered_pattern = np.reshape(flatted_pattern, broken_pattern.shape)
        recovered_pattern = np.sign(recovered_pattern)
        recovered_pattern[recovered_pattern == -1] = 0
        draw_matrix(recovered_pattern, 'recovered')
        return recovered_pattern

    def recover_async(self, broken_pattern):
        pattern_shape = broken_pattern.shape
        flat_broken_patern = broken_pattern.flatten()
        for index, i in enumerate(self.weight.T):
            new_value = np.sign(np.dot(i, flat_broken_patern))
            flat_broken_patern[index] = new_value
        recovered_pattern = np.reshape(flat_broken_patern, pattern_shape)
        recovered_pattern[recovered_pattern == -1] = 0
        draw_matrix(recovered_pattern, 'recovered')
        return recovered_pattern


hopfield = Hopfield()
hopfield.train(eight_pattern)
hopfield.train(x_pattern)
hopfield.train(h_pattern)
# hopfield.recover_sync(broken_eight_pattern)
hopfield.recover_async(broken_eight_pattern)