import socket


def to_bytestring(string):
    print(f"Received string '{string}'")
    byte_string = string.encode('utf-8')
    print(f'As a byte string, that is "{byte_string}"')
    return byte_string


if __name__ == "__main__":

    # socket.AF_INET  = Address Family "Internet" = IPv4
    # socket.AF_INET6 = Address Family "Internet v6" = IPv6

    # socket.SOCK_STREAM = "active connection" = TCP
    connection = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM)

    # First item can be a hostname (i.e., "google.com") OR an IP address
    # (i.e., "68.183.63.165"). Note that, in either case, it's a string.
    address = ("127.0.0.1", 12000)

    # connect() takes _one_ argument -- a _tuple_ of two items.
    print("connecting to localhost")
    connection.connect(address)

    print("Connected!")
    print("Sending to localhost")
    # send() takes a ByteString (notice the b before the quotes)
    connection.sendall(b"Hello, localhost!")

    print("Sent!")

    # recv() takes a number -- the maximum number of bytes
    # to recv at once.
    # However, google doesn't want to reply to us
    # because we're not following the HTTP protocol!
    # reply = connection.recv(4096)

    # print(f'Received reply from google.com: "{reply}"')

    # always close connections when done!
    connection.close()

