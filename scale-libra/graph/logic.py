import device
import networkx as nx 

class Graph(nx.Graph):
	_add_node = nx.Graph.add_node 
	_add_edge = nx.Graph.add_edge

	def add_node(self,settings):
		_add_node(device.Device(settings))

	def add_edge(self,first,second,connection): #connection is a type string
		if not connection in #string database:



	

