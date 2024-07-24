import socket
import json 

BUFFERSIZE = 512
HOST = "127.0.0.1"
PORT = 12345
ADR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADR)

while True:
    command = input("Commands eq-dq-dp-quit Enter the command: ")
    
    if command == "quit":
        client.send(bytes(command, "utf-8"))
        break

    elif command == "eq":
        client.send(bytes(command, "utf-8"))
        data = input("Enter the value for enqueue: ")
        client.send(bytes(data, "utf-8"))

    elif command == "dq":
        client.send(bytes(command, "utf-8"))

    elif command == "dp":
        client.send(bytes(command, "utf-8"))

    else:
        print("Invalid Operation. Try again eq-dq-dp-quit")

client.close()