settings = {}
settings['device_type'] = 'server'
settings['dimensions'] = (2,3)
settings['ports'] = None

def setName(name,settings=settings):
    settings['name'] = name
    return settings
