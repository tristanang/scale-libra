import scale_libra.graph.device.ports as ports
import scale_libra.graph.device.node as node

settings = {}
settings['device_type'] = 'server'
settings['dimensions'] = (2,3)

test_port = ports.Port('RJ45','M',100)

settings['ports'] = test_port

def setName(name,settings=settings):
    settings['name'] = name
    return settings
