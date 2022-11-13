import numpy as np
from numpy import unravel_index
from Utils.mouse_render import mouse_render

mouse_maze = np.array([[0, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, 0, -1, 0], [0, 0, 0, 100, 0], [0, 0, 0, 0, 0]])


class QLearning:
    def __init__(self, mouse_matrix, iterations=500, gamma=0.9):
        self.matrix = mouse_matrix
        self.shape = mouse_matrix.shape
        self.agent_matrix = np.zeros(shape=(self.shape[0]*self.shape[1], self.shape[0]*self.shape[1]))
        self.agent_pos = [0, 0]
        self.environment = np.zeros(shape=(self.shape[0]*self.shape[1], self.shape[0]*self.shape[1]))
        self.gamma = gamma
        self.iterations = iterations
        self.best_path = []

    def create_environment(self):
        row_counter = 0
        for cur_index, cur_value in np.ndenumerate(self.matrix):
            counter = 0
            for i, val in np.ndenumerate(self.matrix):
                if val == 0 or val == 100:
                    value = 1 if val == 0 else 999
                    if i[0] == cur_index[0] and np.absolute(i[1] - cur_index[1]) == 1:
                        self.environment[row_counter][counter] = value
                    if i[1] == cur_index[1] and np.absolute(i[0] - cur_index[0]) == 1:
                        self.environment[row_counter][counter] = value
                counter += 1
            row_counter += 1

    def learn(self):
        for i in range(self.iterations):
            current_state = np.random.randint(0, self.shape[0]*self.shape[1])
            current_actions = list(np.argwhere(self.environment[current_state,] >= 1).flatten())
            next_state = np.random.choice(current_actions)

            self.agent_matrix[current_state, next_state] = self.environment[current_state,next_state] + self.gamma * \
                                                           self.agent_matrix[next_state, np.argmax(self.agent_matrix[next_state,])]

    def find_way(self):
        cheese = list(unravel_index(self.matrix.argmax(), self.matrix.shape))
        current_state = self.agent_pos
        while current_state != cheese:
            row_state = current_state[0]*self.shape[1] + current_state[1]
            max_value = np.max(self.agent_matrix[row_state,])

            next_states = np.argwhere(self.agent_matrix[row_state,] == max_value)
            next_state = np.random.choice(next_states.flatten())

            column = np.mod(next_state, self.shape[1])
            row = int((next_state - column)/self.shape[1])
            current_state = [row, column]
            self.best_path.append(current_state)

            print(current_state)

        return self.best_path


mouse = QLearning(mouse_maze)
mouse.create_environment()
mouse.learn()
path = mouse.find_way()
mouse_render(path, mouse.matrix)
