import device
import networkx as nx

class Graph(nx.Graph):
	_add_node = nx.Graph.add_node
	_add_edge = nx.Graph.add_edge

	def add_node(self,settings):
		_add_node(device.Device(settings))

	def add_edge(self,first,second,connection=None): #connection is a type string
		if connection:
			assert type(connection) == type('string')
			assert first.hasAvailableConnection(connection)
			assert second.hasAvailableConnection(connection)

		#if not connection in #string database:
		_add_edge(first,second,connection=connection)
