# tcpclient.py
# -*- coding: utf-8 -*-
import socket
import json

ip = "127.0.0.1"
port = 9999
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
clientSocket.connect((ip,port))				

print("연결 확인됐습니다.")
while True:
    data = clientSocket.recv(1024)
    data=data.decode("utf-8")
    print(data)
    
    # data=json.loads(data)
    
    # try:
    #     json_object = json.loads(data)
    # except ValueError, e:
    #     print("not json")
    #     pass # invalid json
      
    # else:
    #     print("json")
    #     pass # valid json
        

clientSocket.close()						