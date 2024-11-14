from scapy.all import *

# Define a function to extract ICMP data
def extract_icmp(pkt):
    if pkt.haslayer(ICMP):
        data = pkt[Raw].load
        print("Extracted Data:", data)

# Start sniffing for ICMP packets
sniff(filter="icmp", prn=extract_icmp)
