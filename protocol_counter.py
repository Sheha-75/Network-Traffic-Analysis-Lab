from scapy.all import rdpcap

packets = rdpcap("day2_capture.pcapng")

print("Total Packets:", len(packets))
