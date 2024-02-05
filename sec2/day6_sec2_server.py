import socket

if __name__ == "__main__":
    listen_socket = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM
    )

    # "0.0.0.0" => Accept connections
    #           from any device
    # "127.0.0.1" => Accept connections
    #       ONLY from this device.
    listen_addr = ("0.0.0.0", 12000)

    # bind() attempts to reserve
    # the given port number.
    # Fails if port number is already
    # in use.
    listen_socket.bind(listen_addr)

    # Opens up the port so clients
    # can connect
    listen_socket.listen()

    # We're ready to accept connections!
    conn_socket, in_addr = listen_socket.accept()

    print(f'Received connection from "{in_addr}"!')

    # conn_socket represents our connection
    # to the new client.
    # ONLY use recv() and send() on the
    # connection socket -- NOT on the
    # listen socket!!

    in_msg_b = conn_socket.recv(4096)
    in_msg_s = in_msg_b.decode('ascii')
    print(f'Received message "{in_msg_s}"!')

    conn_socket.close()
    listen_socket.close()
