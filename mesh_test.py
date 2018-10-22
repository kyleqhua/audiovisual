import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import sys


def grid(grid_len):
    verts = np.array([[0,0,0]])
    faces = np.array([[0,0,0]])
    face_2 = np.array([[0,0,0]])
    for i in range(grid_len):
        for j in range(grid_len):
            coord = np.array([[i, j, 0]])
            verts = np.append(verts, coord, axis = 0)
    for i in range(grid_len -1):
        for j in range(grid_len -1):
            cord = np.array([[i * grid_len + j, i * grid_len  + j + 1, i * grid_len + j + grid_len]])
            cord2 = np.array([[i * grid_len  + j + 1,i * grid_len + j + grid_len,i * grid_len + j + grid_len+1]])
            #print(cord, cord2)
            faces = np.append(faces, cord, axis = 0)
    verts = np.delete(verts, 0, axis =0)
    faces = np.delete(faces, 0, axis = 0)

    pcolors = np.random.random(size=(faces.shape[0], 1, 4))
   # print(pcolors[0])
   # print(len(pcolors), len(faces))
    colors = np.array([[0, 0, 0, 0]])
    for i in range(len(faces)):
        c = np.array([[0, 0, 1, 1]])
        colors = np.append(colors, c, axis=0)
    colors = np.delete(colors, 0, axis=0)
    colors = np.empty((len(faces), 1, 4), dtype=np.float32)
    print(colors)