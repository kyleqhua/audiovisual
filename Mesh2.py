import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import sys
from opensimplex import OpenSimplex
import pyaudio
import struct

class Mesh:
	def __init__(self):
		self.app = QtGui.QApplication(sys.argv)
		self.view = gl.GLViewWidget()
		self.noise = OpenSimplex()
		self.offSet = 0

		self.verts = []
		self.faces = []

		#32 by 32 vertices
		for x in range(32):
			for y in range(32):
				self.verts.append([x, y, self.noise.noise2d(x, y)])
		self.verts = np.array(self.verts)

		#implementing faces
		for i in range(31):
			for j in range(31):
				self.faces.append([i * 32 + j, i *32 + j + 1, i * 32 + j + 32])
				self.faces.append([ i *32 + j + 1, i * 32 + j + 32 + 1, i * 32 + j + 32])
		self.faces = np.array(self.faces)

		#implementing colors for the faces
		self.colors = np.random.rand(len(self.faces), 4)
		self.colors = np.array(self.colors)

		#create mesh
		self.mesh = gl.GLMeshItem(vertexes= self.verts, faces= self.faces, faceColors= self.colors)

		#audio 
		#self.RATE = 44100
		#self.CHUNK = 1024
		#self.audioData = None
		#self.p = pyaudio.PyAudio()
		#self.stream = self.p.open(format=pyaudio.palnt16, channels= 1, rate=self.RATE, input=True, output=True, frames_per_buffer=self.CHUNK)

		#get mesh to show
		self.view.show()
		self.view.setWindowTitle("Mesh")
		self.mesh.setGLOptions("additive")
		self.view.addItem(self.mesh)

	def update(self):
		#update to audio
		#self.audioData = self.stream.read(self.CHUNK, exception_on_overflow=False)
		#struct.unpack()



		verts = []
		faces = []

		#32 by 32 vertices
		for x in range(32):
			for y in range(32):
				verts.append([x, y, self.noise.noise2d(x + self.offSet, y + self.offSet)])
		verts = np.array(verts)

		#implementing faces
		for i in range(31):
			for j in range(31):
				faces.append([i * 32 + j, i *32 + j + 1, i * 32 + j + 32])
				faces.append([ i *32 + j + 1, i * 32 + j + 32 + 1, i * 32 + j + 32])
		faces = np.array(faces)

		#implementing colors for faces
		colors = np.random.rand(len(faces), 4)
		colors = np.array(colors)

		#offset
		self.offSet -= .1
		self.mesh.setMeshData(vertexes= verts, faces= faces, faceColors= colors)

	def run():
		if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
			QtGui.QApplication.instance().exec_()

	def animation(self):
		timer = QtCore.QTimer()
		timer.timeout.connect(self.update)
		timer.start(75)
		self.run()
		self.update()
		

if __name__ == '__main__':
	mesh = Mesh()
	mesh.animation()
