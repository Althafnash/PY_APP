import socket 
import threading

def server():
    PORT = 5050
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)
    HEADER = 64
    DISCONNECT_MESSAGE = "!DISCONECTED"
    print(f"[HOST : {SERVER} ]")
    FORMAT= "utf-8"

    server = socket.socket(socket.AF_INET , socket.SOCK_STREAM )
    server.bind(ADDR)

    def handel_client(conn ,addr):
        print(f"[NEW CONNECTION] {addr} connected")

        connected =True
        while connected:
            msg_lenght = conn.recv(HEADER).decode(FORMAT)
            if msg_lenght:
                msg_lenght = int(msg_lenght)
                msg = conn.recv(msg_lenght).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False

                print(f"[{addr}] [{msg}]")

        conn.close()

    def start():
        server.listen()
        while True :
            conn ,addr = server.accept()
            thread = threading.Thread(target=handel_client , args=(conn,addr))
            thread.start()
            print(f"[ACTIVE CCONECTION]:{threading.activeCount() -1}")

    print("[NASH SERVER] starting nash server")
    start()

server()