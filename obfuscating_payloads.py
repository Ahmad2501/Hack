from scapy.all import *

# Define destination IP address (victim's IP)
victim_ip = "victim_ip"

# Craft a GET request with a hidden malicious payload
payload = "GET /index.html HTTP/1.1\r\nHost: victim_ip\r\n\r\nmalicious_payload"

# Create a TCP packet with the malicious HTTP payload
pkt = IP(dst=victim_ip) / TCP(dport=80) / Raw(load=payload)

# Send the crafted packet
send(pkt)
