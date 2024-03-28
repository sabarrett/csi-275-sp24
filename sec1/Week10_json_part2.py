import json
import zlib

example_dict = {'a': 200, 'b': 300, 'c': 20.0}

json_data = json.dumps(example_dict)
json_msg = json_data.encode('utf-8')
compressed_msg = zlib.compress(json_msg)
print(f'Uncompressed len: {len(json_msg)}')
print(f'Compressed len: {len(compressed_msg)}')

# send data via socket
# ...
# get some data back via recv
recv_data = b'{"body": "Hi, client!", "response_code": 200, "time": "2024-03-28"}'
recv_json = recv_data.decode('utf-8')
recv_dict = json.loads(recv_json)
print(recv_dict['body'])


class Bogus:
    def __init__(self):
        self.a = 200
        self.b = 300


class_data = Bogus()
print(f'class_data.a: {class_data.a}')

#  This causes an error -- we can't dump a class
#  as a json string!
#
# class_json_data = json.dumps(class_data)
# print(class_json_data)
