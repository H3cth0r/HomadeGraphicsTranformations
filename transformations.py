import math
import numpy as np
class Point:
	translateMatrix = [[ 1,  0,  0, -1],
			   [ 0,  1,  0, -1],
			   [ 0,  0,  1, -1],
			   [ 0,  0,  0,  1]]
	scaleMatrix	= [[-1,  0,  0,  0],
			   [ 0, -1,  0,  0],
			   [ 0,  0, -1,  0],
			   [ 0,  0,  0,  1]]
	rotateMatrixX	= [[ 1,  0,  0,  0],
			   [ 0, -1, -1,  0],
			   [ 0, -1, -1,  0],
			   [ 0,  0,  0,  1]]
	rotateMatrixZ	= [[-1, -1,  0,  0],
			   [-1, -1,  0,  0],
			   [ 0,  0,  1,  0],
			   [ 0,  0,  0,  1]]
	rotateMatrixY	= [[-1,  0, -1,  0],
			   [ 0,  1,  0,  0],
			   [-1,  0, -1,  0],
			   [ 0,  0,  0,  1]]
	def __init__(self, coords_t):
		self.coords = coords_t

	# Print matrix
	def printMatrix(self, matrx):
		for i in matrx:
			print(i)
	

	def dodprod(self, mat, oldp):
		res = []
		for row in mat:
			counter = 0
			rowSum = 0
			for i in row:
				rowSum += i * oldp[counter][0]
				counter += 1
			res.append(rowSum)
		return res

	

	# Translation operations
	def translate(self, points_t):
		self.translateMatrix[0][3] = points_t[0]
		self.translateMatrix[1][3] = points_t[1]
		self.translateMatrix[2][3] = points_t[2]
		self.printMatrix(self.translateMatrix)
		lcoords = []
		for i in list(self.coords):
			lcoords.append([i])
		lcoords.append([1])
		translateres = self.dodprod(self.translateMatrix, lcoords)
		for i in range(len(translateres)):
			translateres[i] = round(translateres[i], 2)
		self.coords = tuple(translateres[:-1])
		print(self.coords)

	# Scale operations
	def scale(self, points_t):
		self.scaleMatrix[0][0] = points_t[0]
		self.scaleMatrix[1][1] = points_t[1]
		self.scaleMatrix[2][2] = points_t[2]
		lcoords = []
		for i in list(self.coords):
			lcoords.append([i])
		lcoords.append([1])
		scaleres = self.dodprod(self.scaleMatrix, lcoords)
		for i in range(len(scaleres)):
			scaleres[i] = round(scaleres[i], 2)
		self.coords = tuple(scaleres[:-1])
		print(self.coords)
	
	def scaleOnFactor(self, factor):
		factorized_points = (factor, factor, factor)
		self.scale(factorized_points)

	# Rotation operations
	def rotateOnX(self, degs):
		x = lambda a : a *(math.pi/180)
		rads = x(degs)
		self.rotateMatrixX[1][1] =  math.cos(rads)
		self.rotateMatrixX[1][2] = -math.sin(rads)
		self.rotateMatrixX[2][1] =  math.sin(rads)
		self.rotateMatrixX[2][2] =  math.cos(rads)
		lcoords = []
		for i in list(self.coords):
			lcoords.append([i])
		lcoords.append([1])
		rotateXres = self.dodprod(self.rotateMatrixX, lcoords)
		print(self.rotateMatrixX)
		for i in range(len(rotateXres)):
			rotateXres[i] = round(rotateXres[i], 2)
		self.coords = tuple(rotateXres[:-1])
		print(self.coords)
		
		
	def rotateOnY(self, degs):
		x = lambda a : a *(math.pi/180)
		rads = x(degs)
		self.rotateMatrixY[0][0] =  math.cos(rads)
		self.rotateMatrixY[0][2] =  math.sin(rads)
		self.rotateMatrixY[2][0] =  -math.sin(rads)
		self.rotateMatrixY[2][2] =  math.cos(rads)
		lcoords = []
		for i in list(self.coords):
			lcoords.append([i])
		lcoords.append([1])
		rotateYres = self.dodprod(self.rotateMatrixY, lcoords)
		for i in range(len(rotateYres)):
			rotateYres[i] = round(rotateYres[i], 2)
		self.coords = tuple(rotateYres[:-1])
		print(self.coords)

	def rotateOnZ(self, degs):
		x = lambda a : a *(math.pi/180)
		rads = x(degs)
		self.rotateMatrixZ[0][0] =  math.cos(rads)
		self.rotateMatrixZ[0][1] =  -math.sin(rads)
		self.rotateMatrixZ[1][0] =  math.sin(rads)
		self.rotateMatrixZ[1][1] =  math.cos(rads)
		lcoords = []
		for i in list(self.coords):
			lcoords.append([i])
		lcoords.append([1])
		rotateZres = self.dodprod(self.rotateMatrixZ, lcoords)
		for i in range(len(rotateZres)):
			rotateZres[i] = round(rotateZres[i], 2)
		self.coords = tuple(rotateZres[:-1])
		print(self.coords)
	
	def rotateOnPivotX(self, pivot, degs):
		aux_coords = self.coords
		negPivot = list(pivot)
		negPivot[0] *= -1
		negPivot[1] *= -1
		negPivot[2] *= -1
		negPivot = tuple(negPivot)
		self.translate(negPivot)
		self.rotateOnX(degs)
		self.translate(pivot)
	def rotateOnPivotXprof(self, pivot, degs):
		aux_coords = self.coords
		self.translate(pivot)
		self.rotateOnX(degs)
		self.translate(aux_coords)

	def rotateOnPivotY(self, pivot, degs):
		aux_coords = self.coords
		negPivot = list(pivot)
		negPivot[0] *= -1
		negPivot[1] *= -1
		negPivot[2] *= -1 
		negPivot = tuple(negPivot)
		print("TRANSLATE")
		self.translate(negPivot)
		print("ROTATE")
		self.rotateOnY(degs)
		print("TRANSLATE TO PIVOT")
		self.translate(pivot)
	def rotateOnPivotYprof(self, pivot, degs):
		aux_coords = self.coords
		self.translate(pivot)
		self.rotateOnY(degs)
		self.translate(aux_coords)

	def rotateOnPivotZ(self, pivot, degs):
		aux_coords = self.coords
		negPivot = list(pivot)
		negPivot[0] *= -1
		negPivot[1] *= -1
		negPivot[2] *= -1
		negPivot = tuple(negPivot)
		self.translate(negPivot)
		self.rotateOnZ(degs)
		self.translate(pivot)
	def rotateOnPivotZprof(self, pivot, degs):
		aux_coords = self.coords
		self.translate(pivot)
		self.rotateOnZ(degs)
		self.translate(aux_coords)

class Objeto:
	
	centroid = (0, 0, 0)
	vertix = []
	faces  = []

	def rotateOnPivotY(self, pivot, degs):
		for v in self.vertix:
			v.rotateOnPivotY(pivot, degs)	
			print("==========")
	def rotateOnY(self, degs):
		for v in self.vertix:
			v.rotateOnY(degs)

