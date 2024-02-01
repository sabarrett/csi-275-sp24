import socket

def convert_to_bytestring(string):
    print(f"Received string {string}.")
    byte_string = string.encode('utf-8')
    print(f"Converted to byte string {byte_string}.")
    return byte_string

if __name__ == "__main__":
    convert_to_bytestring("Hello, world!")
    convert_to_bytestring("Hi there 😇")
    # socket.AF_INET  = "Address Family Internet" = IPv4
    #     These are the same strings you verified for
    #     correctness in lab 1.
    #     Ex. "32.115.36.1"
    # socket.AF_INET6 = "Address Family Internet v6" = IPv6
    #     Looks totally different from IPv4, and is very long.

    # socket.SOCK_STREAM or socket.SOCK_DGRAM
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect() takes _one_ argument -- a tuple that contains _two_ items.
    # addr[0] = a hostname; either a URL or an IP address as a string.
    #           e.g., "google.com" or "32.115.36.1".
    # addr[1] = the port to connect to (port 80 = HTTP)
    target_addr = ("google.com", 80)
    connection.connect(target_addr)

    print("Connected successfully!")

    # send() take a ByteString -- notice the b at the
    # beginning of the string.
    n_bytes_sent = connection.send(b'Hi there, google!')

    print(f'Sent {n_bytes_sent} bytes.')

    # recv() takes an int, indicating the maximum number of
    # bytes we're willing to receive.
    # Commented out because google won't reply to us.
    # msg = connection.recv(4096)

    # print(f"google.com says '{msg}'.")

    # Close sockets when you're done, as with files.
    connection.close()
