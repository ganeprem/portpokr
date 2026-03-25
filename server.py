import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8000))
s.listen()

print("Listening on port 8000")

while True:

    conn, addr = s.accept()

    print(f"Connection from {addr}")
    
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
