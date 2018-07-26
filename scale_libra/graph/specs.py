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