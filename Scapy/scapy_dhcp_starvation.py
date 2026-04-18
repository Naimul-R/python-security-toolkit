# DHCP-Starvation
# Import Scapy
from scapy.all import *

#conf.checkIPaddr needs to be set to false
#when conf.checkIPaddr the response IP isn't checked
#against sending IP address don't need to match
conf.checkIPaddr = False