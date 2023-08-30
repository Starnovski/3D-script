import numpy as np
import mats


class Cube():
    def __init__(self, name):
        self.name = name
        self.verts = np.array([(1, 1, 1),(1, 1, -1),(1, -1, 1),(-1, 1, 1),(1, -1, -1),(-1, -1, 1),(-1, -1, -1),(-1, 1, -1)])
        self.faces = np.array([[self.verts[0], self.verts[1], self.verts[4], self.verts[2]],
                  [self.verts[3], self.verts[5], self.verts[6], self.verts[7]],
                  [self.verts[0], self.verts[1], self.verts[7], self.verts[3]],
                  [self.verts[4], self.verts[2], self.verts[5], self.verts[6]],
                  [self.verts[5], self.verts[3], self.verts[0], self.verts[2]],
                  [self.verts[1], self.verts[4], self.verts[6], self.verts[7]],
                     ])


    def rotate_x(self, angle):
        x = self.verts @ mats.rot_matrix_x(angle)
        y = self.faces @ mats.rot_matrix_x(angle)
        return x, y


class Pyramid():
    def __init__(self, name):
        self.name = name
        self.verts = np.array([(0, 1, 0),(1, -1, 1),(1,-1,-1),(-1,-1,-1),(-1,-1,1)])
        self.faces = np.array([[self.verts[0], self.verts[1], self.verts[2]],
                      [self.verts[0], self.verts[2], self.verts[3]],
                      [self.verts[0], self.verts[3], self.verts[4]],
                      [self.verts[0], self.verts[4], self.verts[1]],

        ])

    def rotate_x(self, angle):
        x = self.verts @ mats.rot_matrix_x(angle)
        y = self.faces @ mats.rot_matrix_x(angle)
        return x, y
