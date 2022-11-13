import matplotlib.pyplot as plt
import matplotlib.animation as anim


def draw_perceptron(line, points, title, x_name="X", y_name="Y"):
    plt.plot(line[0], line[1])
    plt.title(title)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.grid()
    for p in points:
        if p.classification == 1:
            plt.scatter(p.vector[0], p.vector[1], c='blue')
        else:
            plt.scatter(p.vector[0], p.vector[1], c='red')
    plt.show()


def draw_matrix(matrix, name):
    fig, ax = plt.subplots()
    ax.matshow(matrix, cmap="Blues")
    ax.set_title(name)
    plt.show()


def plot_xor(points, results):
    plt.grid()
    x, y = zip(*points)
    plt.scatter(x, y, c=results)
    plt.xlim(-50, 50)
    plt.ylim(-50, 50)
    plt.show()


def plot_3D_points(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c='b', marker='.')
    plt.show()


def plot_bifurcation_diag(x, y, xlim=(1, 4), ylim=(0, 1)):
    plt.scatter(x, y, s=.01)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.show()


def plot_TEA(matrix, x_boundaries, y_boundaries):
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.imshow(matrix, cmap="inferno",
              extent=[x_boundaries[0], x_boundaries[1], y_boundaries[0], y_boundaries[1]])
    plt.show()


def draw_forest_fire(matrices, iterations):
    def update(i):
        M = matrices[i]
        matrice.set_array(M)

    fig, ax = plt.subplots()
    matrice = ax.matshow(matrices[0])

    ani = anim.FuncAnimation(fig, update, interval=iterations)
    plt.show()
