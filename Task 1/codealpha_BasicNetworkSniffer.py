from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

def analyze_packet(packet):
    if IP in packet:
        time = datetime.now().strftime("%H:%M:%S")
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        size = len(packet)

        protocol = "OTHER"
        src_port = "-"
        dst_port = "-"

        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        elif ICMP in packet:
            protocol = "ICMP"

        print(f"\n[{time}] {protocol}")
        print(f"Source IP : {src_ip}:{src_port}")
        print(f"Dest IP   : {dst_ip}:{dst_port}")
        print(f"Packet Size : {size} bytes")

        if Raw in packet:
            payload = packet[Raw].load
            print("Payload:")
            print(payload[:100])   # first 100 bytes only (safe)

print("=== Network Sniffer Started ===")
sniff(prn=analyze_packet, store=False)