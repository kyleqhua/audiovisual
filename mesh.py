import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
from opensimplex import OpenSimplex
import pyaudio
import struct
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
        Mesh.grid(self)
        self.pick_facecolor(0)
        self.offSet = 0
        #audio setup
        self.RATE = 44100
        self.CHUNK = 1024
        self.audioData = None
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=self.RATE, input=True, output=True,
                                  frames_per_buffer=self.CHUNK)
        #creating mesh
        self.mesh = gl.GLMeshItem(vertexes= self.verts, faces = self.faces, faceColors = self.colors, drawEdges = True,)
        self.mesh.setGLOptions("additive")
        self.view.addItem(self.mesh)


    def run(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):QtGui.QApplication.instance().exec_()

    def update(self):
        noise = OpenSimplex()
        self.audioData = self.stream.read(self.CHUNK, exception_on_overflow=False)
        new_audio = struct.unpack(str (2 * self.CHUNK) + 'B', self.audioData)
        new_audio = np.array(new_audio, dtype='b')[::2] + 128
        new_audio = np.array(new_audio, dtype='int32') - 128
        new_audio = new_audio * 0.01
        #print(len(new_audio))
        self.verts = []
        for i in range(self.grid_len):
            for j in range(self.grid_len):
                constant = 1 #np.random.randint(low=1, high=3)
                coord = [[i, j, noise.noise2d(x = i +self.offSet, y = j+self.offSet)]]
                #if j % 2:
                    #coord = [[i, j,  constant * noise.noise2d(x=i + self.offSet, y=j + self.offSet)]]
                self.verts.append(coord)
        self.verts = np.array(self.verts)
        for i in range (len(new_audio)):
            self.verts[i][0][2]= self.verts[i][0][2]*new_audio[i]
        self.offSet -=  .1
        self.mesh.setMeshData(vertexes=self.verts, faces=self.faces, faceColors=self.colors)
        #self.pick_facecolor(0)
        #print(0)


    def animate(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(100)
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

    def flat_grid(self):
        for i in range(self.grid_len):
            for j in range(self.grid_len):
                coord = np.array([[i, j, 0]])
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
    #t.run()
