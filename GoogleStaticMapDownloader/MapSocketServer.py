import socket
from MapBuffer import Circular512

BUFFERSIZE = 512
HOST = "127.0.0.1"
PORT = 12345
ADR = (HOST, PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADR)

server.listen(2)

buffer = Circular512()
client, address = server.accept()

while True:
    print ("{}:{} bağlandi".format(*address))
    data = client.recv(BUFFERSIZE).decode("utf-8")
    if data == "quit":
        client.close() 
        break           
    elif data == "eq":
        value = client.recv(BUFFERSIZE).decode()
        buffer.enQueue(int(value))
    elif data == "dq":
        buffer.deQueue()
    elif data == "dp":
        buffer.display()
server.close()