from scapy.all import sniff
from database import save_packet
from alert import check_anomaly

def process_packet(packet):
    try:
        src = packet[0][1].src
        dst = packet[0][1].dst
        proto = packet[0][1].proto
        length = len(packet)
        save_packet(src, dst, proto, length)
        check_anomaly(src)
    except:
        pass

print("Sniffing started...")
def main_sniff():
    print("Sniffing started...")
    sniff(prn=process_packet, store=0)
