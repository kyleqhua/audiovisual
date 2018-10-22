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
        #Show mesh in new window
        self.app =  QtGui.QApplication(sys.argv)
        self.view = gl.GLViewWidget()
        self.view.show()
        self.view.setWindowTitle('Mesh')
        #sets grid stuff
        self.grid()
        self.pick_facecolor(0)
        self.offSet = 0
        self.mesh = gl.GLMeshItem(vertexes= self.verts, faces = self.faces, faceColors = self.colors, drawEdges = True, drawFaces = True,  smooth = True)
        self.mesh.setGLOptions("additive")
        self.view.addItem(self.mesh)


    def run(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):QtGui.QApplication.instance().exec_()

    def update(self):
        noise = OpenSimplex()
        self.verts = []
        for i in range(self.grid_len):
            for j in range(self.grid_len):
                constant = np.random.randint(low=1, high=5)
                coord = [[i, j, constant*noise.noise2d(x = i +self.offSet, y = j+self.offSet)]]
                if j % 2:

                    coord = [[i, j,  constant * noise.noise2d(x=i + self.offSet, y=j + self.offSet)]]
                self.verts.append(coord)
        self.verts = np.array(self.verts)
        self.offSet -=  .1
        self.mesh.setMeshData(vertexes=self.verts, faces=self.faces, faceColors=self.colors)
        print(0)


    def animate(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(60)
        Mesh.run()
        self.update()



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
