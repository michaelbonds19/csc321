def get_interfaces():
      ...:     list = []
      ...:     for i in range(19216817747,0):
      ...:         list.append(i)
      ...:         return list
      ...: a = get_interfaces()
      
def get_mac(interface: str):
   ...:     eth_mac = get_mac(interface = "eth0")
   ...:     win_mac = get_mac(interface = "Ethernet 3")
   ...:     ip_mac = get_mac(ip = "192.168.0.1")
   ...:     ip6_mac = get_mac(ip6="::1")
   ...:     host_mac = get_mac(hostname="localhost")
   ...:     updated_mac = get_mac(ip="10.0.0.1", network_request=True)
   ...:     physical_mac = get_mac(mac = "94-53-30-13-2B-C6")
   ...:     return mac
   ...: print(get_mac)
<function get_mac at 0x058DADF0>

def get_ips(interface: str):
   ...:     d = dict();
   ...:     d ['str'] = dict()
   ...:     ipv4_ips = get_ips(ipv4 = '192.168.0.1')
   ...:     ipv6_ips = get_ips(ipv6 = '2001:db8::1000')
   ...:     eth_ips = get_ips(interface = "eth0")
   ...:     return ips
   ...: print(get_ips)
<function get_ips at 0x054E2DA8>
      
def get_netmask(interface: str):
   ...:     d = dict();
   ...:     d ['str'] = dict()
   ...:     eth_netmask = get_netmask(interface = "eth0")
   ...:     ipv4_netmask = get_netmask(ipv4 = '192.0.2.5/255.255.255.0')
   ...:     ipv6_netmask = get_netmask(ipv6 = '192.0.2.5/255.255.255.0')
   ...:     return netmask
   ...: print(get_netmask)
<function get_netmask at 0x054E2EC8>

 def get_network(interface: str):
   ...:     d = dict();
   ...:     d ['str'] = dict()
   ...:     eth_network = get_network(interface = "eth0")
   ...:     ipv4_network = get_network(ipv4 = '192.168.1.0/0.0.0.255')
   ...:     ipv6_network = get_network(ipv6 = '2001:db00::0/24')
   ...:     return network
   ...: print(get_network)
<function get_network at 0x055B9F10>

  
