import numpy as np
from Utils.drawUtils import draw_perceptron
from Utils.utils import is_above

dimension = 2


class Point:
    def __init__(self, vector: []):
        self.vector = np.array(vector, dtype=np.float32)
        self.classification = None

    def __str__(self):
        return str(self.vector)


class Perceptron:
    def __init__(self, points: Point([]), threshold=200, learning_rate=0.1, bias=0.5):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.points = points
        self.weight = np.zeros(dimension)
        self.bias = bias

    def iteration(self):
        pass

    def train(self):
        for _ in range(self.threshold):
            changed = False
            for point in self.points:
                guess = np.sign(np.dot(point.vector, self.weight) + self.bias)
                result = is_above(get_result(point.vector[0]), point.vector[1])
                point.classification = result
                if guess == result:
                    continue
                else:
                    error = result - guess
                    self.weight = self.weight + error * point.vector * self.learning_rate
                    self.bias = self.bias + error * self.learning_rate
                    changed = True
            if not changed:
                break

    def test(self, test_points):
        # errors = 0
        for p in test_points:
            guess = np.sign(np.dot(p.vector, self.weight) + self.bias)
            p.classification = guess
            # result = is_above(get_result(p.vector[0]), p.vector[1])
            # if guess != result:
            #     errors += 1
        return test_points


def create_random_points(total_points):
    random_points = [Point([np.random.uniform(-10, 10), np.random.uniform(-40, 40)]) for _ in range(total_points)]
    return random_points


def get_result(x):
    return 4*x - 5


x_line = np.linspace(-10, 10, 1000)
y_line = get_result(x_line)
line = [x_line, y_line]


perceptron = Perceptron(create_random_points(100))
test_set = create_random_points(100)
perceptron.train()
result_test = perceptron.test(test_set)


#draw_perceptron(line, perceptron.points, "X", "Y")
draw_perceptron(line, result_test, "X", "Y")
