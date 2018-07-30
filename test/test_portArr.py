import scale_libra.graph.device.ports as ports
import scale_libra.graph.logic as logic

import scale_libra.device.node as node

test_port = ports.Port('RJ45','M',100)
test_port2 = ports.Port('RJ45','F',100)

test_board = ports.Board((2,3),test_port)
test_board2 = ports.Board((2,3),test_port)

assert test_board.port_type[0][0] == test_board.port_type[1][1]

print(test_board.availableConnections(test_port2))

g = logic.Graph()
g.add_node

print('tests passed')
