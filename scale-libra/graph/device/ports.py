import numpy as np

test = {}
test['ports'] = 
#2d matrix
#1s and zeros
#1) Port Availability
#2) Port Type

class Port:
	def __init__(self,type,gender,speed=None):
		self.type = type
		self.gender = gender
		self.speed = speed
		
	def __repr__(self):
		return "Port(%s,%s,%d)" % (self.type,self.gender,self.speed)

	__str__ = __repr__

class Board:
	def __init__(self,settings):





