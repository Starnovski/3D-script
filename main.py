import objects
import mats
import math
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
from PIL import Image
import io



# That code is good

verts, faces = objects.read_file('../lowpoly.obj')
verts, faces = objects.convert(verts, faces)

cube = objects.Object3D("cube", verts, faces)

def rotate_x(a):
    verts, faces = cube.rotate_x(a)
    return verts, faces

def rotate_y(a):
    verts, faces = cube.rotate_y(a)
    return verts, faces

def rotate_z(a):
    verts, faces = cube.rotate_z(a)
    return verts, faces

#---------------------------------------------

b = 90
a = 0


while a <= b:
    verts, faces = rotate_x(a)
    fig = plt.figure(figsize = [10.4, 7.8], dpi= 300)
    ax = fig.add_subplot(111, projection='3d')
    x = verts[:,0]
    y = verts[:,1]
    z = verts[:,2]
    vertices = [list(zip(x,y,z))]
    poly = Poly3DCollection(faces, alpha=0.4, facecolors='green')
    ax.add_collection3d(poly)
    ax.scatter(x, y, z, color='red')
    ax.set_xlim(-12,12)
    ax.set_ylim(-12,12)
    ax.set_zlim(-12,12)
    #img_buf = io.BytesIO()
    plt.savefig(f'images/{a}', dpi=100, format='png')
    #im = Image.open(img_buf)
    #im.show(title="My Image")
    #img_buf.close()
    plt.close()
    print(faces.size)
    a+=1
