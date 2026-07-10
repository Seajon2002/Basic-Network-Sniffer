from scapy.all import sniff

def start_sniff(packet_handler):
    """
    Starts capturing network packets.

    Args:
        packet_handler: Function that processes each captured packet.
    """

    sniff(
        prn=packet_handler,   # Function called for every captured packet
        store=False           # Do not store packets in memory
    )
