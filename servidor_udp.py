import socket
import datetime

host = ''
port = 9999

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((host, port))
print(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] *** Se inició el servidor en el puerto {port}")

while True:
    try:
        recv, address = serverSocket.recvfrom(1024)
        print(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] {address}: {recv.decode()}")
        serverSocket.sendto("OK".encode(), address)
    except Exception as e:
        print(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] *** ERROR: {e}")

serverSocket.close()