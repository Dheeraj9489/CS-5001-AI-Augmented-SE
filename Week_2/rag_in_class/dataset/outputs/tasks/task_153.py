import cmath
import math

def parabola_vertex(a, b, c):
    x = (-b) / (2 * a)
    y = ((4 * a * c) - (b ** 2)) / (4 * a)
    return (float(x), float(y))
