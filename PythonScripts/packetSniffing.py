import socket
import struct


def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]


def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()


def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
#    conn.bind(("172.16.0.111", 80))
#    conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
#    conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    while True:
        raw_data, addr = conn.recvfrom(65535)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        if eth_proto == 8:
            print('\nEthernet Frame:')
            print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))
            print(data)


if __name__ == "__main__":
   main()
