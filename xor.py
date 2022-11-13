import numpy as np
from Utils.drawUtils import plot_xor
from Utils.utils import generate_random_points


class XOR:

    def __init__(self, input, output):
        self.learning_rate = 0.1
        self.epochs = 1000
        self.weights_hidden = np.random.rand(2, 2)
        self.weights_output = np.random.rand(2, 1)
        self.bias_hidden = np.random.rand(1, 2)
        self.bias_output = np.random.rand(1, 1)
        self.input = input
        self.output = output

    def sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-x))

    def sigmoid_derivate(self, x):
        return x * (1.0 - x)

    def learn(self):
        for _ in range(self.epochs):
            hidden_layer = self.sigmoid(np.dot(self.input, self.weights_hidden) + self.bias_hidden)
            output_layer = self.sigmoid(np.dot(hidden_layer, self.weights_output) + self.bias_output)

            #back propagation
            error = 0.5 * ((self.output - output_layer) ** 2)
            output_der = error * self.sigmoid_derivate(output_layer)
            hidden_der = np.dot(output_der, self.weights_output.T) * self.sigmoid_derivate(hidden_layer)

            self.weights_output += np.dot(hidden_layer.T, output_der) * self.learning_rate
            self.bias_output += np.sum(output_der) * self.learning_rate
            self.weights_hidden += np.dot(self.input.T, hidden_der) * self.learning_rate
            self.bias_hidden += np.sum(hidden_der) * self.learning_rate

    def test(self, points):
        hidden_res = self.sigmoid(np.dot(points, self.weights_hidden) + self.bias_hidden)
        output_res = self.sigmoid(np.dot(hidden_res, self.weights_output) + self.bias_output)
        return output_res


input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
output = np.array([[0], [1], [1], [0]])

neural = XOR(input, output)
neural.learn()

test_points = generate_random_points(50, (1000, 2))
result = neural.test(test_points)

plot_xor(test_points, result)
