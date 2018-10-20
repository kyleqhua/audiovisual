import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import sys


def grid(grid_len):
    verts = np.array([])

    faces = np.array([])
    for i in range(grid_len):
        for j in range(grid_len):
            coord = [i, j, 0]
            verts = np.append(verts, coord, axis = 0)
    for i in range(grid_len - 1):
        for j in range(grid_len - 1):
            cord = [i * grid_len + j, i * grid_len + 1, i * grid_len + j + grid_len]
            faces = np.append(faces, cord, axis = 0)

    return verts, faces