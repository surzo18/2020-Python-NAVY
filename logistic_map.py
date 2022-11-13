from random import randint
from Utils.drawUtils import plot_bifurcation_diag

r_boundaries = [1.0, 4.0]
generations = 100
start_population = 0.5
step = 0.0001
radius = 5

r_values = []
x_values = []


# n...kolikatou generaci vezmu jako vysledek
def get_growth_factor(max_generation, x_n, r):
    for i in range(1, max_generation):
        x_n = x_n * r * (1 - x_n)
    return x_n


r = r_boundaries[0]
while r < r_boundaries[1]:
    random = randint(generations - radius, generations + radius)
    result = get_growth_factor(random, start_population, r)
    r_values.append(r)
    x_values.append(result)
    r += step

plot_bifurcation_diag(r_values, x_values)
