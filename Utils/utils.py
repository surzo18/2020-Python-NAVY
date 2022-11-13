import random
import numpy as np


def get_random_point(dimension, limits):
    point = []
    for i in range(dimension - 1):
        point.append(random.uniform(limits[0], limits[1]))
    return point


def is_above(y, point_y):
    if point_y == y:
        return 0
    if point_y > y:
        return 1
    if point_y < y:
        return -1


def generate_random_points(limit, size):
    return np.random.randint(-limit, limit, size=size)
