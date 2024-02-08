import socket

if __name__ == "__main__":

    # UDP -- use SOCK_DGRAM instead
    # of TCP's SOCK_STREAM.
    udp_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    )

    # Don't have to make a connection.

    # Still need to know where to
    # send the data
    srv_address = ("127.0.0.1", 4567)

    # Need to make some data to send
    msg_str = "Hi, server!"
    msg_raw = msg_str.encode('ascii')

    # Need to specify recipient with
    # each sendto() call when using
    # UDP
    len_sent = udp_socket.sendto(msg_raw, srv_address)

    print(f'Sent {len_sent} bytes to {srv_address}')

    # Receive our response:
    srv_msg_raw, from_address = udp_socket.recvfrom(4096)
    srv_msg_str = srv_msg_raw.decode('ascii')

    if from_address != srv_address:
        print('Received message NOT from our server!')
    else:
        print('Received message from our server!')

    print(f'Received from {from_address}: "{srv_msg_str}"')

    udp_socket.close()
