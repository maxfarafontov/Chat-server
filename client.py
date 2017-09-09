import socket

s_client = socket.socket()

s_client.connect(('localhost',1408))

s_client.send(b'hello, world!')
data = s_client.recv(1024)
s_client.close()

print(data)
