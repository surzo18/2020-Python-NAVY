import numpy as np
from Utils.drawUtils import plot_TEA


def iterate(x0, y0, limit, iteration_count):
    i = 0
    x = 0
    y = 0
    while x ** 2 + y ** 2 < limit and i < iteration_count:
        tmp = np.power(x, 2) - np.power(y, 2) + x0
        y = 2 * x * y + y0
        x = tmp
        i += 1
    return i


def tea(x_boundaries=[-2.0, 1], y_boundaries=[-1.3, 1.3],
        size=1000, iteration_count=100, limit=7):
    x_step = abs(x_boundaries[0] - x_boundaries[1]) / size
    y_step = abs(y_boundaries[0] - y_boundaries[1]) / size

    result = np.full((size, size), 255)
    x_pos = x_boundaries[0]
    y_pos = y_boundaries[0]
    x_index = 0
    y_index = 0
    while x_pos < x_boundaries[1] - x_step:
        while y_pos < y_boundaries[1] - y_step:
            result[y_index, x_index] = result[y_index, x_index] - iterate(x_pos, y_pos, limit, iteration_count)
            y_pos += y_step
            y_index += 1
        y_index = 0
        y_pos = y_boundaries[0]
        x_pos += x_step
        x_index += 1

    return result


extent1 = [(-2.0, 1), (-1.3, 1.3)]
extent2 = [(-0.22, -0.219), (-0.7, -0.699)]
extent3 = [(-0.745431, -0.745426), (0.113006, 0.113012)]

result1 = tea(extent1[0], extent1[1])
plot_TEA(result1, extent1[0], extent1[1])
