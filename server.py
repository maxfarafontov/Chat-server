import asyncio
import socket

s_server = socket.socket()

s_server.bind(('', 1408))

s_server.listen(10)

connect, adress = s_server.accept()

while True:
    data = connect.recv(1024)
    if not data:
        break
    connect.send(data.upper())
    print(data)

connect.close()
