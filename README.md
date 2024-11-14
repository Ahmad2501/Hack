# Evasion Techniques to Bypass Snort IDS Detection

This repository demonstrates different evasion techniques using Scapy in Python to bypass Snort IDS detection. The techniques tested include packet fragmentation, timing-based evasion, obfuscating attack payloads, and using ICMP tunneling for covert communication.

## Scripts

1. packet_fragmentation.py
   This script fragments packets to avoid detection by Snort's signature-based rules.

2. timing_based_evasion.py
   This script performs a slow port scan with random delays to avoid Snort's rate-based detection.

3. obfuscating_payloads.py  
   This script embeds malicious payloads inside normal HTTP requests to evade Snort's signature-based detection.

4. icmp_tunneling_sender.py 
   This script uses ICMP Echo Request packets to send covert data to the victim.

5. **`icmp_tunneling_sniffer.py`**  
   This script listens for ICMP packets and extracts the embedded covert data.

## Requirements

- Kali Linux (Attacker)  
- Ubuntu (Victim with Snort installed)  
- Python3  
- Scapy Library  

## Installation

To install the required dependencies, use the following commands:

# On Kali (Attacker)
sudo apt update
sudo apt install python3-scapy

# On Ubuntu (Victim)
sudo apt update
sudo apt install snort
