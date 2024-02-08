import socket

if __name__ == "__main__":
    udp_sock = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_DGRAM
    )

    our_address = ("0.0.0.0", 9998)
    udp_sock.bind(our_address)

    print(f'Waiting for datagram...')
    msg_raw, address = udp_sock.recvfrom(4096)
    msg_str = msg_raw.decode('ascii')

    print(f'Received datagram from \
{address}: "{msg_str}"')

    send_msg_str = 'Hi client! :)'
    send_msg_raw = send_msg_str.encode('ascii')

    # udp_sock.sendto(send_msg_raw, address)
