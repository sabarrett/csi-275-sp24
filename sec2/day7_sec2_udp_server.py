import socket

if __name__ == "__main__":
    udp_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    )

    our_address = ("0.0.0.0", 4567)
    udp_socket.bind(our_address)

    msg_raw, address = udp_socket.recvfrom(4096)
    msg_str = msg_raw.decode('ascii')

    print(f'Received from {address}: "{msg_str}"')

    rsp_msg_str = f"Hi there, {address}!"
    rsp_msg_raw = rsp_msg_str.encode('ascii')

    len_sent = udp_socket.sendto(rsp_msg_raw, address)
    print(f'Sent {len_sent} bytes.')

    udp_socket.close()
