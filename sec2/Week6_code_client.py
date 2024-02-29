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
    """Send data in fixed-length segments to the server.

    Actually tries to send extra data just to see what happens.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect(("localhost", 30000))

    # Sending more than 10 characters here
    sock.sendall("abcdefghijklmnop".encode("ascii"))

    # Receive the response
    print(sock.recv(10).decode("ascii"))
    sock.close()


def length_field():
    """Use length fields to tell the server how much data is being sent."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect(("localhost", 30001))

    # Prepare and encode our message
    message = "On my business card, I am a corporate president. " \
              "In my mind, I am a game developer. " \
              "But in my heart, I am a gamer. -Satoru Iwata".encode("ascii")

    # Prepare the length field using big-endian ordering
    length = len(message)
    length_field = length.to_bytes(8, "big")

    # Prep and send the message
    data_to_send = length_field + message
    sock.sendall(data_to_send)

    # Receive the response
    reply_len = int.from_bytes(sock.recv(8), 'big')
    print(f"The reply was {reply_len} bytes.")
    reply = recv_all(sock, reply_len)
    print(reply.decode("ascii"))
    sock.close()


def deadlock_demo():
    """Don't worry about this until Friday."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect(("localhost", 30002))

    # Send two messages
    sock.sendall("Hello world!%".encode("utf-8"))
    sock.sendall("Hello again!%".encode("utf-8"))
    print(sock.recv(4096).decode("utf-8"))

    sock.close()

if __name__ == "__main__":
    # fixed_length()
    # length_field()
    deadlock_demo()