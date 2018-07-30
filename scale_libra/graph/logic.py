import device
import networkx as nx

class Graph(nx.Graph):
	_add_node = nx.Graph.add_node
	_add_edge = nx.Graph.add_edge

	def add_node(self,settings):
		_add_node(device.Device(settings))

	def add_edge(self,first,second,connection): #connection is a type string

		assert type(connection) == type('string')

		first_ports = first.availableConnections(connection)
		second_ports = second.availableConnections(connection)

		assert first_ports and second_ports
		#need to add exception

		first_index = first_ports[0]
		second_index = second_ports[0]

		assert first.board.availability[0]
		assert second.board.availability[0]

		first.board.availability[first_index] += 1
		second.board.availability[second_index] += 1

		_add_edge(first,second,connection=connection)
		#if not connection in #string database:
