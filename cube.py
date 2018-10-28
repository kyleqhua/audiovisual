import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
from opensimplex import OpenSimplex
import sys


class Mesh:
    verts = np.array([[0, 0, 0]])
    faces = np.array([[0, 0, 0]])
    colors = np.array([[0, 0, 0, 0]])
    grid_len = 32

    def __init__(self):
        # Show mesh in new window
        self.app = QtGui.QApplication(sys.argv)
        self.view = gl.GLViewWidget()
        self.view.show()
        self.view.setWindowTitle('Mesh')
        # sets grid stuff
        self.cube()
        self.pick_facecolor(1)
        self.offSet = 0
        self.mesh = gl.GLMeshItem(vertexes=self.verts, faces=self.faces, faceColors=self.colors, drawEdges=True, )
        self.mesh.setGLOptions("additive")
        self.view.addItem(self.mesh)

    def run(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'): QtGui.QApplication.instance().exec_()

    def update(self):
        noise = OpenSimplex()
        self.verts = np.array([
                [0, noise.noise2d(x = 0, y = 0), 0],
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
                [1, 1, 0],
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 1]])
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


    def animate(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(60)
        Mesh.run()
        self.update()

    def cube(self):
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



    def pick_facecolor(self, int):
        # 0 is random
        if int == 0:
            self.colors = np.random.random(size=(self.faces.shape[0], 1, 4))
        # 1 is Blue gradient
        if int == 1:
            self.colors = []
            for i in range(1, self.grid_len):
                for j in range(1, self.grid_len):
                    if i % 2:
                        c = [[1, .7, .6, 1]]
                        c2 = [[1, .7, .6, 1]]
                    self.colors.append(c)
                    self.colors.append(c2)
            self.colors = np.array(self.colors)


if __name__ == '__main__':
    t = Mesh()
    t.animate()
    # t.run()
