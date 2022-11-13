import numpy as np
from Utils.drawUtils import plot_3D_points

model1 = np.array([[0.00, 0.00, 0.01, 0.00, 0.26, 0.00, 0.00, 0.00, 0.05, 0.00, 0.00, 0.00],
                   [0.20, -0.26, -0.01, 0.23, 0.22, -0.07, 0.07, 0.00, 0.24, 0.00, 0.80, 0.00],
                   [-0.25, 0.28, 0.01, 0.26, 0.24, -0.07, 0.07, 0.00, 0.24, 0.00, 0.22, 0.00],
                   [0.85, 0.04, -0.01, -0.04, 0.85, 0.09, 0.00, 0.08, 0.84, 0.00, 0.80, 0.00]])

model2 = np.array([
    [0.05, 0.00, 0.00, 0.00, 0.60, 0.00, 0.00, 0.00, 0.05, 0.00, 0.00, 0.00],
    [0.45, -0.22, 0.22, 0.22, 0.45, 0.22, -0.22, 0.22, -0.45, 0.00, 1.00, 0.00],
    [-0.45, 0.22, -0.22, 0.22, 0.45, 0.22, 0.22, -0.22, 0.45, 0.00, 1.25, 0.00],
    [0.49, -0.08, 0.08, 0.08, 0.49, 0.08, 0.08, -0.08, 0.49, 0.00, 2.00, 0.00]
])


def create_fractal(model):
    x = 0
    y = 0
    z = 0
    x_axis = []
    y_axis = []
    z_axis = []
    for n in range(10000):
        r1 = model[np.random.choice(model.shape[0])]
        rest = np.array(r1[-3:])
        matrix = np.split(r1[:-3], 3)
        res = np.array(matrix).dot(np.array([x, y, z]))
        res += rest
        x_axis.append(x)
        y_axis.append(y)
        z_axis.append(z)
        x = res[0]
        y = res[1]
        z = res[2]

    plot_3D_points(x_axis, y_axis, z_axis)


create_fractal(model2)
