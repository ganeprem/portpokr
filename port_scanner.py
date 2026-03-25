import socket
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

def scan(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(0.3)

        result = s.connect_ex((target, port))
        if result == 0:
            try:   
                s.send(b"HEAD / HTTP/1.0\r\n\r\n")
                banner = s.recv(1024).decode(errors="ignore")
                if not banner:
                    banner = "[no response]"
            except:
                    banner = "[no response]"

            print(f"{port} | {banner}")
    except:
        pass
    finally:
        s.close()

def make_scanner(target):
    def scan_port(port):
        scan(target, port)
    return scan_port

if __name__ == "__main__":
    target = input("Target IP: ")
    start = int(input("Start Port: "))
    end = int(input("End Port: "))

    scanner = make_scanner(target)

    print("Scanning...")
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(scanner, range(start, end + 1))
    print("Done...")



