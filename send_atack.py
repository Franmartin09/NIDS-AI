from scapy.all import *

# target_ip = "192.168.1.1"
target_ip = "172.20.145.52"
ports = [22,80,443]

def port_scan(ip, port):
    src_port = RandShort()
    syn_pkt = IP(dst=ip)/TCP(sport = src_port,dport=port,flags='S')
    syn_ack_pkt = sr1(syn_pkt, timeout=1, verbose=0)
    if syn_ack_pkt and syn_ack_pkt.haslayer(TCP):
        print(f"Puerto {port} esta abierto")
    else:
        print(f"Puerto {port} no esta abierto")

for port in ports:
    port_scan(target_ip, port)