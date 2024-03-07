import socket

LENGTH = 51


def recvall(sock, length, delimiter, buffer):
    """Receive data until we see a delimiter.

    Example:
    First call receives: b'abcd#efg'
        -> returns "abcd", stores b'efg' in buffer.
    Second call receives: b'h#ijkl#'
        -> returns b'efgh', stores b'ijkl#' in buffer.
    Third call doesn't call receive. Already has a message in the buffer.
        -> returns "ijkl", buffer now is empty.
    """
    # We're going to return a regular string here
    data = ''

    # First, let's examine our buffer
    for char in buffer:
        # If it's the delimiter, we've got a full message
        if char == delimiter:
            print("message in buffer")
            buffer = buffer[buffer.index(delimiter) + 1:]
            return data, buffer
        else:
            # Add the buffered char to the output
            data += char

    # If we got here, the buffer is empty but we still don't
    # have a full message
    while True:
        more = sock.recv(length).decode('ascii')
        if not more:
            raise EOFError('expected %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))

        # Scour the data for the delimiter
        for char in more:
            # If it's the delimiter, we've got a full message
            if char == delimiter:
                # Store any extra data we've got
                print("message in recv")
                buffer = more[more.index(delimiter) + 1:]
                return data, buffer
            else:
                # Add the buffered char to the output
                data += char

        # If we get here, we STILL haven't found the end of
        # a message, so we'll loop back and call recv() again

def start_server():

    # Create our server socket (we'll use TCP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind our server to this socket
    address_tuple = ('localhost', 5000)
    sock.bind(address_tuple)

    # Begin listening for connections!
    sock.listen(1)

    #Outer while loop (accepting loop)
    while True:
        print("Waiting...")
        client_sock, addr = sock.accept()

        # Reset our data counter
        counter = 0

        # Special buffer for data storage
        buffer = ''

        while True:
            try:
                data, buffer = recvall(client_sock, LENGTH, '#', buffer)
            except EOFError:
                # If we don't get anything, the client doesn't
                # have any data left to send
                break

            # If we got something, increment the message counter
            counter = counter + 1
            print(counter)

        # Send our number back to the client
        # (no framing done here)
        client_sock.sendall(str(counter).encode('ascii'))

        #Close the socket and loop back to accept more connections
        client_sock.close()


if __name__ == "__main__":
    start_server()
