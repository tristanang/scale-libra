import device
import networkx as nx 

class Graph(nx.Graph):
	_add_node = nx.Graph.add_node 

	def add_node(self,settings):
		_add_node(device.Device(settings))

	def hi(self):
		print('hi')

	

