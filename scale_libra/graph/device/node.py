import scale_libra.graph.device.ports as ports

#perhaps settings should be a dictionary sorted
def remove_settings(settings):
	del settings['name']
	#del settings['location']
	settings['location'].pop()
	del settings['device_type']

	return settings

class Device: #create a hashable datatype for networkx nodes
	def __init__(self,settings):
		self.name = settings['name'] #need to check for no clashes
		self.device_type = settings['device_type']
		self.location = 'placeholder'
		self.board = ports.Board(settings['dimensions'],settings['ports'])
		self.ports_dimensions = self.board.getDimensions() #settings['ports']

		self.hash = (self.name,self.device_type,
			self.location,self.ports_dimensions)

	def __eq__(self,other):
		if len(self.hash) != len(other.hash):
			return False

		return all(map(lambda x,y : x == y, self.hash,other.hash))

	def __hash__(self):
		return hash(self.hash)

	def _rehash(self):
		self.hash = (self.name,self.device_type,
			self.location,self.ports_dimensions)

	def availableConnections(self,connection):
		return self.board.availableConnections(connection)

	def __repr__(self):
		return self.name

class Server(Device):
	def __init__(self,settings):
		Device.__init__(self,settings)

class Custom(Device):
	def __init__(self,settings):
		Device.__init__(self,settings)
		self.settings = remove_settings(settings)
