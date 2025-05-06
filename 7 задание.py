from ipaddress import *
net = ip_network('192.168.108.157/255.255.255.192', strict = False)
host_number = int(ip_address('192.168.108.157')) - int(net.network_address)
print(host_number)