import socket
import sys
import json

HOST, PORT = "127.0.0.1", 9999


json_object = {"name": "han1222", "vel": 10} # a real dict.

json_string = json.dumps(json_object, indent=2)
print(json_string)

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()
client_socket, addr = sock.accept()


while True:

    client_socket.sendall(bytes(json_string,encoding="utf-8"))
    # print ("Sent:{}".format(data))

sock.close()
client_socket.close()

