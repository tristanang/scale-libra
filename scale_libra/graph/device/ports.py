import numpy as np

test = {}
#2d matrix
#1s and zeros
#1) Port Availability
#2) Port Type

class Port:
	def __init__(self,type,gender,speed = None):
		self.type = type
		self.gender = gender
		self.speed = speed

	def __repr__(self):
		return "Port(%s,%s,%d)" % (self.type,self.gender,self.speed)

	#__str__ = __repr__

class Board:
	def __init__(self,dimensions,ports = None): #dimensions is len 2 tuple rows,columns
		assert len(dimensions) == 2
		self.availability = np.zeros(dimensions,dtype=int)
		self.port_type = np.zeros(dimensions,dtype=bool)

		if ports:
			self.port_type = np.zeros(dimensions,dtype=Port)
			print("ports triggered")

	def quickAdd(self):
		dim = self.availability.shape
		rows = dim[0]
		columns = dim[1]

		for i in range(rows):
			for j in range(columns):
				if self.availability[i,j] == 0:
					self.availability[i,j] += 1
					return

	def getDimensions(self):
		return self.availability.shape
