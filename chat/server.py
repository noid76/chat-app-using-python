import socket
import threading

clients = []

def handle_client(client, addr, client_id):
    print(f"[Client {client_id}] Bersambung dari {addr}")
    while True:
        try:
            msg = client.recv(1024)
            if not msg:
                break
            print(f"[Client {client_id}] {msg.decode()}")
            # Hantar ke client lain
            for c in clients:
                if c != client:
                    c.send(msg)
        except:
            break

    client.close()
    clients.remove(client)
    print(f"[Client {client_id}] Putus sambungan")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(2)

print("[SERVER] Menunggu 2 client...")

client_id = 1
while len(clients) < 2:
    client, addr = server.accept()
    clients.append(client)
    threading.Thread(target=handle_client, args=(client, addr, client_id)).start()
    client_id += 1