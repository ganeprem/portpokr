import socket
from threading import Thread

def handle_connection(conn, addr):
    print(f"Connected to {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg = data.decode().strip()
        if msg == "exit":
            break
        print(f"Client said: {msg}")
        conn.send(f"Echo: {msg}\n".encode())
    conn.close()
        
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8000))
s.listen()

print("Listening on port 8000")

try:
    while True:    

        conn, addr = s.accept()
        Thread(target = handle_connection, args = (conn, addr), daemon=True).start()
except KeyboardInterrupt:
    print("Exiting...")
    s.close()
        
