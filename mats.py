import math
import numpy as np


def rot_matrix_x(angle):
    angle = math.radians(angle)
    y = np.array([
        [1, 0, 0],
        [0, math.cos(angle), math.sin(angle)],
        [0, -math.sin(angle), math.cos(angle)]
    ])
    return y
