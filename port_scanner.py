import socket
target = input("Target IP: ")
start = int(input("Start Port: "))
end = int(input("End Port: "))

for port in range(start, end + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)

    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    s.close()
