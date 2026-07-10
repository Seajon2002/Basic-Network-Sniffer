from packet_sniffer import start_sniff
from packet_analyzer import analyze_packet

def main():
    print("=" * 60)
    print("        Basic Network Sniffer")
    print("=" * 60)
    print("Capturing network packets...")
    print("Press Ctrl + C to stop.\n")

    try:
        start_sniff(analyze_packet)
    except KeyboardInterrupt:
        print("\n\nSniffer stopped successfully.")

if __name__ == "__main__":
    main()
