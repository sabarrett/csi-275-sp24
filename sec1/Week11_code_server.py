import threading, socket, random, time

def accept_connections_forever(sock, thread_id):
    """Tell clients who accepted their connection."""
    #Infinite loop
    while True:
        # Create our accept socket
        accept_sock, address = sock.accept()

        # Get data
        message = accept_sock.recv(4096)

        # Wait a random amount of time to mix up the threads
        time.sleep(random.randint(1, 5))

        # We don't care what the data was here, we just
        # tell the client who they spoke with
        reply = f"Thread {thread_id}".encode('ascii')
        accept_sock.sendall(reply)

        # Close the connection and loop back to handle another one
        accept_sock.close()

def thread_handler(sock, thread_id):
    """Accept socket connections."""
    while 1:
        try:
            accept_connections_forever(sock, thread_id)
        except EOFError:  # Catch-all for sockets
            print('Client socket has closed')
        except ConnectionResetError:  # Connection broken
            print('Connection error')


if __name__ == "__main__":
    # Setup the listening socket
    server_sock = socket.socket()  # default params (TCP, IPv4)
    server_sock.bind(("localhost", 6000))
    server_sock.listen(20)

    # Create our threads
    first_thread = threading.Thread(target=thread_handler,
                                   args=(server_sock, 1))
    second_thread = threading.Thread(target=thread_handler,
                                    args=(server_sock, 2))
    third_thread = threading.Thread(target=thread_handler,
                                    args=(server_sock, 3))

    # Start the threads
    first_thread.start()
    second_thread.start()
    third_thread.start()

    # Wait for all the threads to complete
    first_thread.join()
    second_thread.join()
    third_thread.join()