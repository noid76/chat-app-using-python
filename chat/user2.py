import socket
import threading

def terima(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            print(f"\nAiman: {msg}")
        except:
            print("Putus sambungan.")
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

threading.Thread(target=terima, args=(client,)).start()

while True:
    msg = input("Aiman: ")
    client.send(msg.encode())