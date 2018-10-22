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

"""    def cube(self):
        self.verts = np.array([
            [0, 0, 0],
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ])
        self.faces = np.array([
            [0, 1, 4],
            [0, 2, 4],
            [0, 3, 6],
            [0, 1, 6],
            [0, 2, 5],
            [0, 3, 5],
            [3, 6, 7],
            [3, 5, 7],
            [7, 6, 1],
            [7, 4, 1],
            [7, 5, 2],
            [7, 4, 2]

        ])
        self.colors = np.array([
            [1, 0, 0, 0.3],
            [1, 0, 0, 0.3],
            [0, 1, 0, 0.3],
            [0, 1, 0, 0.3],
            [0, 0, 1, 0.3],
            [0, 0, 1, 0.3],
            [1, 1, 0, 0.3],
            [1, 1, 0, 0.3],
            [.2, .1, 0, 0.3],
            [.61, .51, 0, 1],
            [1, 0, .66, 1],
            [1, 0, .3, 1],
        ])

    def some(self):
        self.verts = np.empty((36, 3, 3), dtype=np.float32)
        self.theta = np.linspace(0, 2 * np.pi, 37)[:-1]
        self.verts[:, 0] = np.vstack([2 * np.cos(theta), 2 * np.sin(theta), [0] * 36]).T
        self.verts[:, 1] = np.vstack([4 * np.cos(theta + 0.2), 4 * np.sin(theta + 0.2), [-1] * 36]).T
        self.verts[:, 2] = np.vstack([4 * np.cos(theta - 0.2), 4 * np.sin(theta - 0.2), [1] * 36]).T
        ## Colors are specified per-vertex
        self.colors = np.random.random(size=(verts.shape[0], 3, 4))
"""