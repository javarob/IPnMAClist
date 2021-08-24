
import socket
from time import sleep
# must install scapy in pycharm
from scapy.layers.l2 import Ether, ARP
from scapy.all import *

# get localhost / subnet information
def get_details():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    net = ip[0:ip.rfind('.') + 1]
    arp_scanner(net)

# display arp listing
def arp_scanner(net):
    for port in range(255):
        ip = net + str(port)
        arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip,hwdst="ff:ff:ff:ff:ff:ff")
        response = srp1(arp_request, timeout=1, verbose=0)
        if response:
            print("IP: {}, MAC: {}".format(response.psrc,response.hwsrc))
        time.sleep(0.5)

if __name__ == '__main__':
    get_details()