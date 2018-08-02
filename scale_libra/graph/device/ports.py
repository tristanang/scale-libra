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

    def __eq__(self,other): #error probably here
        value = (self.type,self.gender,self.speed)
        return value == other

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
            self.port_type = np.full_like(self.port_type,ports) #as a test case, all ports set to the same type in this iteration
            #print("ports triggered")

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

    def availableConnections(self,connection):
        ports = np.argwhere(self.port_type == connection)
        empty = np.argwhere(self.availability == 0)

        return np.array([x for x in set(tuple(x) for x in ports) & set(tuple(x) for x in empty)])

    def usePort(self,index):
        assert self.availability[index] == 0, "Port is not unused."
        self.availability[index] += 1

    def removePort(self,index):
        assert self.availability[index] == 1, "Port is not used."
        self.availability[index] -= 1
