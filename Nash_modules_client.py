import socket 
import threading

def client():
    PORT = 5050
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)
    HEADER = 64
    DISCONNECT_MESSAGE = "!DISCONECTED"
    print(f"[CLIENT : {SERVER} ]")
    FORMAT= "utf-8"
    server = "192.168.137.1"

    client = socket.socket(socket.AF_INET , socket.SOCK_STREAM )
    client.connect(ADDR)

    def send(msg):
        message  = msg.encode(FORMAT)
        msg_lenght = len(message)
        send_lenght = str(msg_lenght).encode(FORMAT)
        send_lenght += b''* (HEADER -  len(send_lenght))
        client.send(send_lenght)
        client.send(message)

    inputw = input("TYPE")
    send(inputw)

