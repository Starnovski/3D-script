import objects
import mats
import math
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
from PIL import Image
import io




cube = objects.Cube('cobe')
verts = cube.verts
faces = cube.faces
verts, faces = cube.rotate_x(30)

print(verts)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


x = verts[:,0]
y = verts[:,1]
z = verts[:,2]

vertices = [list(zip(x,y,z))]


poly = Poly3DCollection(faces, alpha=0.4, facecolors='green')
ax.add_collection3d(poly)
ax.scatter(x, y, z, color='red')
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_zlim(-2,2)

#Creating a buffer and displaying image
img_buf = io.BytesIO()
plt.savefig(img_buf, format='png')
im = Image.open(img_buf)
im.show(title="My Image")
img_buf.close()
