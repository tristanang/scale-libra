__device_info_dict = {}
__device_lst = ('pdu','switch','server')
__ports = ('ethernet_port','power_port')
__power_type = ('C14','C20')
__ethernet_type = (1,10)

for device in __device_lst:
	__device_info_dict[device] = {}
	for port in __ports:
		__device_info_dict[device][port] = {}
		if port == __ports[1]:
			for c in __power_type:
				__device_info_dict[device][port][c] = 0
		if port == __ports[0]:
			for c in __ethernet_type:
				__device_info_dict[device][port][c] = 0

__device_info_dict['pdu']['power_port']['C14'] = 21
__device_info_dict['pdu']['power_port']['C20'] = 3

__device_info_dict['server']['power_port']['C14'] = 2


class Device: #create a hashable datatype for networkx nodes
	def __init__(self,settings='test'):

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