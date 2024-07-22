import numpy as np
import mats



#Cube object coordinates
'''
verts = np.array([(1, 1, 1),(1, 1, -1),(1, -1, 1),(-1, 1, 1),(1, -1, -1),(-1, -1, 1),(-1, -1, -1),(-1, 1, -1)])

faces = np.array([[verts[0], verts[1], verts[4], verts[2]],
          [verts[3], verts[5], verts[6], verts[7]],
          [verts[0], verts[1], verts[7], verts[3]],
          [verts[4], verts[2], verts[5], verts[6]],
          [verts[5], verts[3], verts[0], verts[2]],
          [verts[1], verts[4], verts[6], verts[7]],
             ])
'''

#Pyramid object coordinates
'''
verts = np.array([(0, 1, 0),(1, -1, 1),(1,-1,-1),(-1,-1,-1),(-1,-1,1)])
faces = np.array([[self.verts[0], self.verts[1], self.verts[2]],
              [self.verts[0], self.verts[2], self.verts[3]],
              [self.verts[0], self.verts[3], self.verts[4]],
              [self.verts[0], self.verts[4], self.verts[1]],

])
'''

#Function that reads obj files, return lists
def read_file(file):
    verts, faces = [], []
    with open(file) as f:
        for line in f:
            if line.startswith('v '):
                verts.append([float(i) for i in line.split()[1:]])

            elif line.startswith('f '):
                faces_ = line.split()[1:]
                faces.append([int(face_.split('/')[0]) for face_ in faces_])

    return verts, faces

#Function that converts lists to numpy arrays
def convert(verts, faces):
    verts = np.array(verts)
    #That loop swaps verts numbers with their coordinates
    for i in range(0, len(faces)):
        for a in range(0,4):
            b = faces[i][a]
            faces[i][a] = verts[b-1]
    faces = np.array(faces)
    return verts, faces


class Object3D():
    def __init__(self, name, verts, faces):
        self.name = name
        self.verts = verts
        self.faces = faces

#Self rotation functions
    def rotate_x(self, angle):
        self.verts = self.verts @ mats.rot_matrix_x(angle)
        self.faces = self.faces @ mats.rot_matrix_x(angle)

    def rotate_y(self, angle):
        self.verts = self.verts @ mats.rot_matrix_y(angle)
        self.faces = self.faces @ mats.rot_matrix_y(angle)


    def rotate_z(self, angle):
        self.verts = self.verts @ mats.rot_matrix_z(angle)
        self.faces = self.faces @ mats.rot_matrix_z(angle)
