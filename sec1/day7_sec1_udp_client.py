import socket

if __name__ == "__main__":
    udp_sock = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_DGRAM
    )

    # establish an address to
    # send our data to
    address = ("127.0.0.1", 9998)

    # create our message, first
    # as a string and then as a
    # byte string
    msg_str = "Hi there, server!"
    msg = msg_str.encode('ascii')

    # use sendto() for UDP sockets
    len_sent = udp_sock.sendto(
        msg,
        address
    )

    print(f'Sent {len_sent} bytes \
to {address}')

    srv_msg_raw, srv_address = udp_sock.recvfrom(4096)
    if srv_address != address:
        print(f'Received a message not from the server!  Came from: {srv_address}')
    else:
        print(f'Message verified to be from server.')
    srv_msg_str = srv_msg_raw.decode('ascii')
    print(f'Received message "{srv_msg_str}"')


