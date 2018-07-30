class Device: #create a hashable datatype for networkx nodes
	def __init__(self,settings='test'):
		self.name = 'placeholder' #need to check for no clashes




		if settings == 'test':
			self.device_type = 'switch'
			self.C14 = 2
			self.ethernet = 48

		self.hash = (self.device_type,self.C14,self.ethernet)

	def __eq__(self,other):

		return all(map(lambda x,y : x == y, self.hash,other.hash))

	def __hash__(self):
		return hash(self.hash)

	def _rehash(self):
		self.hash = (self.device_type,self.C14,self.ethernet)
