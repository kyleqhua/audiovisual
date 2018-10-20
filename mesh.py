import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import sys

class Mesh:

    def __init__(self):
        self.app =  QtGui.QApplication(sys.argv)
        self.view = gl.GLViewWidget()
        self.view.show()
        self.view.setWindowTitle('Mesh')
        verts,faces = self.grid()
        self.mesh = gl.GLMeshItem(vertexes= verts, faces = faces)
        self.mesh.setGLOptions("additive")
        self.view.addItem(self.mesh)

    def run(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
	           QtGui.QApplication.instance().exec_()

#if __name__ == '__main__':
    def cube(self):
        verts = np.array([
            [0, 0, 0],
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ])
        faces = np.array([
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
        colors = np.array([
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
        return verts, faces, colors
    def some(self):
        verts = np.empty((36, 3, 3), dtype=np.float32)
        theta = np.linspace(0, 2 * np.pi, 37)[:-1]
        verts[:, 0] = np.vstack([2 * np.cos(theta), 2 * np.sin(theta), [0] * 36]).T
        verts[:, 1] = np.vstack([4 * np.cos(theta + 0.2), 4 * np.sin(theta + 0.2), [-1] * 36]).T
        verts[:, 2] = np.vstack([4 * np.cos(theta - 0.2), 4 * np.sin(theta - 0.2), [1] * 36]).T

        ## Colors are specified per-vertex
        colors = np.random.random(size=(verts.shape[0], 3, 4))

        return verts, theta, colors

    def grid(self):
        verts = np.array([])
        grid_len = 3
        faces = np.array([])
        for i in range(grid_len):
            for j in range(grid_len):
                verts = np.append([[i,j,0]], verts)
        for i in range(grid_len-1):
            for j in range(grid_len-1):
                faces = np.append([[i*grid_len+j,i*grid_len+1, i*grid_len+j+grid_len]], faces)
       
        return verts, faces