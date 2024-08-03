import scapy.all as scapy

def packet_callback(packet):

    if packet.haslayer(scapy.IP):
        source_ip = packet[scapy.IP].src
        destination_ip = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto

        print("Packet Captured:")
        print(f"Source IP: {source_ip}")
        print(f"Destination IP: {destination_ip}")
        print(f"Protocol: {protocol}")

        if packet.haslayer(scapy.Raw):
            payload = packet[scapy.Raw].load
            print(f"Payload: {payload}")

# Start sniffing packets on the specified interface
print("Starting packet sniffer...")
scapy.sniff(iface="eth0", prn=packet_callback, store=False)