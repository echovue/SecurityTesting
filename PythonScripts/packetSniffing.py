import socket
import struct


def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return format_mac_addr(dest_mac), format_mac_addr(src_mac), socket.htons(proto), data[14:]


def format_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()


def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, addr = conn.recvfrom(65535)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        if eth_proto == 8:
            print('\nEthernet Frame:')
            print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))
            print(data)


if __name__ == "__main__":
   main()
