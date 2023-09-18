import math
import numpy as np


#Those functions return rotation matrixes
def rot_matrix_x(angle):
    angle = math.radians(angle)
    x = np.array([
        [1, 0, 0],
        [0, math.cos(angle), math.sin(angle)],
        [0, -math.sin(angle), math.cos(angle)]
    ])
    return x


def rot_matrix_y(angle):
    angle = math.radians(angle)
    y = np.array([
        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)]
    ])
    return y


def rot_matrix_z(angle):
    angle = math.radians(angle)
    z = np.array([
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ])
    return z
