import socket

# Get Interface name
intefaces = socket.if_nameindex()
# for int in intefaces:
#     print(int)

nameindex = [
    (1, 'lo0'),
    (2, 'gif0'),
    (3, 'stf0'),
    (4, 'anpi0'),
    (5, 'anpi1'),
    (6, 'en0'),
    (7, 'en4'),
    (8, 'en5'),
    (9, 'en2'),
    (10, 'en3'),
    (11, 'bridge0'),
    (12, 'ap1'),
    (13, 'en1'),
    (14, 'awdl0'),
    (15, 'llw0'),
    (16, 'utun0'),
    (17, 'utun1'),
    (18, 'utun2'),
    (19, 'utun3'),
    (20, 'utun4'),
    (21, 'utun5'),
]

# # Get Interface address
# for int in nameindex:
#     # print(socket.if_indextoname(int[0]))
#     # print(socket.if_nameindex(int[1]))


import socket

def get_interface_info(interface_name):
    interfaces = socket.if_nameindex()
    for index, name in interfaces:
        if name == interface_name:
            interface = socket.if_indextoname(index)
            addrs = socket.ifaddresses(interface)
            ip = addrs[socket.AF_INET][0]['addr']
            mac = addrs[socket.AF_LINK][0]['addr']
            status = addrs[socket.AF_INET][0].get('up', 'Down')
            return {'Interface': interface, 'IP': ip, 'MAC': mac, 'Status': status}
    
    return None

# Get information from interface en1
interface_info = get_interface_info('en1')

if interface_info:
    print(f"Interface: {interface_info['Interface']}")
    print(f"IP Address: {interface_info['IP']}")
    print(f"MAC Address: {interface_info['MAC']}")
    print(f"Status: {interface_info['Status']}")
else:
    print("Interface not found")
