import test_server
import scale_libra.graph.device.node as node
import scale_libra.graph.logic as logic

import numpy as np

test = node.Device(test_server.setName('test'))
test2 = node.Device(test_server.setName('test2'))

print(np.argwhere(test.board.port_type == test_server.test_port))

print(test.board.port_type)

print(test.board.availableConnections(test_server.test_port))

g = logic.Graph()
g.add_edge(test,test2,test_server.test_port)

print(g.edges(data=True))

print('passed')
