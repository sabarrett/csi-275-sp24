import socket

def recv_all(sock, length):
    """Receive specified amount of data from a socket."""
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('expected %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    return data


def fixed_length():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind(("localhost", 30000))
    sock.listen(2)

    while True:
        cli_sock, address = sock.accept()

        data = cli_sock.recv(10)
        print(f"We received {data.decode('ascii')}")
        cli_sock.send((data))
        # cli_sock.sendall("Got it!".encode("ascii"))
        cli_sock.close()


def length_field():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind(("localhost", 30001))
    sock.listen(2)

    while True:
        cli_sock, address = sock.accept()

        # Read first 8 bytes to get message length
        length_field = cli_sock.recv(8)
        length = int.from_bytes(length_field, "big")
        print(f"The message was {length} bytes.")

        # Receive the rest of the message
        message = recv_all(cli_sock, length).decode("ascii")
        print(f"Message: {message}")

        # Send something back
        response = "Got it!".encode("ascii")
        resp_length = len(response).to_bytes(8, "big")
        cli_sock.sendall(resp_length + response)

        cli_sock.close()

def deadlock_demo():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind(("localhost", 30002))
    sock.listen(20)

    while True:
        cli_sock, address = sock.accept()

        # Receive two messages. reply to them
        # ~*~*~ pseudocode to prevent deadlock ~*~*~
        # while we haven't yet received two messages:
        # Recv, and parse to see if we have our '%' delimiter.
        # Once we find two delimiters and extract the messages,
        # we're done!
        request = cli_sock.recv(4096)
        print(f"Received {request.decode('utf-8')}")
        cli_sock.sendall("Got it!".encode("ascii"))
        cli_sock.close()

if __name__ == "__main__":
    # fixed_length()
    # length_field()
    deadlock_demo()