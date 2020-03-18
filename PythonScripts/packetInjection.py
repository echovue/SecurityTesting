# ICMP Echo request

import socket
import struct
from random import randint


def icmp():
    type = 8
    code = 0
    chksum = 0
    id = randint(0, 0xFFFF)
    seq = 1
    data = struct.pack("!BBHHH", type, code, chksum, id, seq)
    print('Data: {}'.format(data))
    real_chksum = checksum(data)
    icmp_pkt = struct.pack("!BBHHH", type, code, socket.htson(real_chksum), id, seq)
    return icmp_pkt


def checksum(data):
    s = 0
    n = len(data) % 2
    for i in range(0, len(data) - n, 2):
        s += data[i] + (data[i + 1] << 8)
    if n:
        s += ord(data[i + 1])
    while s >> 16:
        s = (s & 0xFFFF) + (s >> 16)
    s = ~s & 0xFFFF
    return s


def main():
    packet = icmp()
    print(packet);
    s = socket.socker(socket.AFF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    s.sendto(packet, ("172.16.0.111", 80))
    print('Sent')


if __name__ == "__main__":
   main()
