import socket
import zlib

listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_sock.bind(("127.0.0.1", 5000))
listen_sock.listen()

while True:
    conn, _ = listen_sock.accept()

    msg = conn.recv(4096)
    json_msg = b'{"body": "Hello, client!", "status": 200, "date": "2024-03-28"}'
    msg_compressed = zlib.compress(json_msg)
    conn.sendall(msg_compressed)
