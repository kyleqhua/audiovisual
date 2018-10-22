import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
from opensimplex import OpenSimplex
import sys

class Mesh:
    verts = np.array([[0, 0, 0]])
    faces = np.array([[0, 0, 0]])
    colors = np.array([[0, 0, 0, 0]])
    grid_len = 10

    def __init__(self):
        self.app =  QtGui.QApplication(sys.argv)
        self.view = gl.GLViewWidget()
        self.view.show()
        self.view.setWindowTitle('Mesh')
        self.grid()
        self.pick_facecolor(0)
        self.offSet = 0
        self.mesh = gl.GLMeshItem(vertexes= self.verts, faces = self.faces, faceColors = self.colors, drawFaces = True,  smooth = True)
        self.mesh.setGLOptions("additive")
        self.view.addItem(self.mesh)


    def run(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):QtGui.QApplication.instance().exec_()

    def update(self):
        noise = OpenSimplex()
        self.verts = []
        for i in range(self.grid_len):
            for j in range(self.grid_len):
                coord = [[i, j, noise.noise2d(x = i +self.offSet, y = j+self.offSet)]]
                self.verts.append(coord)
        self.verts = np.array(self.verts)
        self.offSet -=  -.1
        self.mesh.setMeshData(vertexes=self.verts, faces=self.faces, faceColors=self.colors)
        print(0)


    def animate(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(10)
        self.run()
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

    def some(self):
        self.verts = np.empty((36, 3, 3), dtype=np.float32)
        self.theta = np.linspace(0, 2 * np.pi, 37)[:-1]
        self.verts[:, 0] = np.vstack([2 * np.cos(theta), 2 * np.sin(theta), [0] * 36]).T
        self.verts[:, 1] = np.vstack([4 * np.cos(theta + 0.2), 4 * np.sin(theta + 0.2), [-1] * 36]).T
        self.verts[:, 2] = np.vstack([4 * np.cos(theta - 0.2), 4 * np.sin(theta - 0.2), [1] * 36]).T
        ## Colors are specified per-vertex
        self.colors = np.random.random(size=(verts.shape[0], 3, 4))


    def grid(self):
        noise = OpenSimplex()
        for i in range(self.grid_len):
            for j in range(self.grid_len):
                coord = np.array([[i, j, noise.noise2d(x = i, y = j)]])
                self.verts = np.append(self.verts, coord, axis=0)
        for i in range(self.grid_len - 1):
            for j in range(self.grid_len - 1):
                cord = np.array([[i * self.grid_len + j, i * self.grid_len + j + 1, i * self.grid_len + j + self.grid_len]])
                cord2 = np.array([[i * self.grid_len + j + 1, i * self.grid_len + j + self.grid_len, i * self.grid_len + j + self.grid_len + 1]])
                self.faces = np.append(self.faces, cord, axis=0)
                self.faces = np.append(self.faces, cord2, axis=0)
        self.verts = np.delete(self.verts, 0, axis=0)
        self.faces = np.delete(self.faces, 0, axis=0)


    def pick_facecolor(self, int):
        # 0 is random
        if int == 0:
            self.colors = np.random.random(size=(self.faces.shape[0], 1, 4))
        # 1 is Blue gradient
        if int == 1:
            for i in range(1, self.grid_len):
                for j in range(1, self.grid_len):
                    c = [[0,0, i/self.grid_len,1]]
                    c2 = [[0,0, j/self.grid_len ,1]]
                    self.colors = np.append(self.colors, c, axis=0)
                    self.colors = np.append(self.colors, c2, axis=0)
            self.colors = np.delete(self.colors, 0, axis=0)
if __name__ == '__main__':
    t = Mesh()
    t.animate()
