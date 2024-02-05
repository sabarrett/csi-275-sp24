import socket

if __name__ == "__main__":
    listen_socket = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM)
    # "0.0.0.0" => accept connections from anywhere
    # "127.0.0.1" => accept connections only from
    #                the same computer
    listen_address = ("0.0.0.0", 12000)

    # Reserve the port for our usage
    listen_socket.bind(listen_address)

    # Open port that we've bound
    # so information can come in
    listen_socket.listen()

    # Now we're ready to receive
    # connections!
    conn_socket, conn_addr = listen_socket.accept()
    print(f'Received connection from {conn_addr}')

    # Now we follow our protocol --
    # receive a message from the client

    # From now on, we ONLY use conn_socket
    # -- listen_socket is JUST for receiving
    # NEW connections
    incoming_msg_b = conn_socket.recv(4096)
    incoming_msg_s = incoming_msg_b.decode('ascii')
    print(f'Received message "{incoming_msg_s}"')

    # Close all connections
    conn_socket.close()
    listen_socket.close()
