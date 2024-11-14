import time
from scapy.all import *

# Define destination IP address (victim's IP)
victim_ip = "victim_ip"

# Perform a port scan from ports 20 to 25 with delays between packets
for port in range(20, 25):
    # Create a TCP SYN packet for each port
    pkt = IP(dst=victim_ip) / TCP(dport=port, flags="S")
    
    # Send the packet
    send(pkt)
    
    # Introduce a random delay between packets (e.g., 2 seconds)
    time.sleep(2)
