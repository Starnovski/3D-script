import objects
import mats
import math
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from matplotlib import animation
import matplotlib as mpl
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
from PIL import Image
import io

mpl.use('TkAgg')


#Loading file and creating object
verts, faces = objects.read_file('lowpoly.obj')
verts, faces = objects.convert(verts, faces)
cube = objects.Object3D("cube", verts, faces)


#---------------------------------------------


a = 2
fig = plt.figure(dpi= 300)
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-16,16)
ax.set_ylim(-16,16)
ax.set_zlim(-16,16)

def update(a, verts, faces):
    ax.clear()
    ax.set_xlim(-16,16)
    ax.set_ylim(-16,16)
    ax.set_zlim(-16,16)
    cube.rotate_x(a)
    cube.rotate_z(a)
    cube.rotate_y(a)
    x = cube.verts[:,0]
    y = cube.verts[:,1]
    z = cube.verts[:,2]
    vertices = [list(zip(x,y,z))]
    poly = Poly3DCollection(cube.faces, alpha=0.5, facecolors='green')
    ax.add_collection3d(poly)




        #ax.scatter(x, y, z, color='red')

        #img_buf = io.BytesIO()
            #plt.savefig(f'images/{a}', dpi=100, format='png')
        #im = Image.open(img_buf)
        #im.show(title="My Image")
        
   
line_ani = animation.FuncAnimation(fig, update, a, fargs=(cube.verts, cube.faces),
                                   interval=1, blit=False)

plt.show()

            #img_buf.close()
