from scapy.layers.inet import IP, TCP, UDP, ICMP
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Packet Counter
packet_count = 0


def analyze_packet(packet):
    global packet_count
    packet_count += 1

    # Check if packet contains an IP layer
    if packet.haslayer(IP):

        ip_layer = packet[IP]

        source_ip = ip_layer.src
        destination_ip = ip_layer.dst

        protocol = "OTHER"
        source_port = "-"
        destination_port = "-"

        # Check Protocol
        if packet.haslayer(TCP):
            protocol = "TCP"
            source_port = packet[TCP].sport
            destination_port = packet[TCP].dport

        elif packet.haslayer(UDP):
            protocol = "UDP"
            source_port = packet[UDP].sport
            destination_port = packet[UDP].dport

        elif packet.haslayer(ICMP):
            protocol = "ICMP"

        packet_size = len(packet)

        print(Fore.GREEN + "=" * 70)
        print(Fore.CYAN + f"Packet No       : {packet_count}")
        print(Fore.YELLOW + f"Source IP       : {source_ip}")
        print(Fore.YELLOW + f"Destination IP  : {destination_ip}")
        print(Fore.MAGENTA + f"Protocol        : {protocol}")
        print(Fore.BLUE + f"Source Port     : {source_port}")
        print(Fore.BLUE + f"Destination Port: {destination_port}")
        print(Fore.WHITE + f"Packet Size     : {packet_size} bytes")

        # Show Payload (first 64 bytes only)
        if packet.payload:
            payload = bytes(packet.payload)
            print(Fore.LIGHTBLACK_EX + "Payload:")
            print(payload[:64])

        print(Fore.GREEN + "=" * 70 + "\n")
