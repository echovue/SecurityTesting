import socket
import struct
from random import randint


def createIcmpPacket():
    type = 8
    code = 0
    chksum = 0
    id = randint(0, 0xFFFF)
    seq = 1
    real_chksum = checksum(struct.pack("!BBHHH", type, code, chksum, id, seq))
    packet = struct.pack("!BBHHH", type, code, socket.htons(real_chksum), id, seq)
    print(packet)
    return packet


def checksum(data):
    s = 0
    n = len(data) % 2
    for i in range(0, len(data) - n, 2):
        s += data[i] + (data[i + 1] << 8)
    if n:
        s += data[i + 1]
    while s >> 16:
        s = (s & 0xFFFF) + (s >> 16)
    s = ~s & 0xFFFF
    return s


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    s.sendto(createIcmpPacket(), ("172.16.0.111", 80))


if __name__ == "__main__":
   main()
