import json
import socket
import zlib

example_dict = {'a': 200, 'b': 1000, 'c': 20.5}
json_data = json.dumps(example_dict)
print(json_data)
json_msg = json_data.encode('utf-8')
print(json_msg)
json_compressed = zlib.compress(json_msg)

# send json_msg
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 5000))
conn.sendall(json_compressed)

recv_data = conn.recv(4096)
print(recv_data)
recv_decompressed = zlib.decompress(recv_data)
print(recv_decompressed)
recv_json = recv_decompressed.decode('utf-8')
recv_dict = json.loads(recv_json)
print(recv_dict)
print(recv_dict['body'])
