import socket
import struct
from random import randint


def create_icmp_packet():
    type = 8
    code = 0
    chksum = 0
    id = randint(0, 0xFFFF)
    seq = 1
    checksum = calculate_checksum(struct.pack("!BBHHH", type, code, chksum, id, seq))
    packet = struct.pack("!BBHHH", type, code, socket.htons(checksum), id, seq)
    print(packet)
    return packet


def calculate_checksum(packet):
    s = 0
    n = len(packet) % 2
    for i in range(0, len(packet) - n, 2):
        s += packet[i] + (packet[i + 1] << 8)
    if n:
        s += packet[i + 1]
    while s >> 16:
        s = (s & 0xFFFF) + (s >> 16)
    s = ~s & 0xFFFF
    return s


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    s.sendto(create_icmp_packet(), ("172.16.0.111", 80))


if __name__ == "__main__":
   main()
