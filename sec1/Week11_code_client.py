import threading, socket

def send_message(i):
    """Send a message to our server to see which thread receives it."""
    msg = "Hello world!".encode('ascii')
        
    # Create, connect and send
    cli_sock = socket.socket()  # Default parameters (TCP, IPv4)
    cli_sock.connect(("localhost", 6000))
    cli_sock.sendall(msg)
        
    # Grab the reply and see who handled this request
    reply = cli_sock.recv(4096).decode('ascii')
    print("Connection thread " + str(i) + " was handled by " + reply + "!")
        
    # Close the connection
    cli_sock.close()

if __name__ == '__main__':
    # Create a list of threads (for joining later)
    thread_list = []
    
    # Start ten threads
    for i in range(0, 10):
        thread = threading.Thread(target=send_message, args=(i,))
        thread.start()
        thread_list.append(thread)
        
    # Wait for ten threads
    for i in range(0, 10):
        thread_list[i].join()
    
    print("All done.")
        