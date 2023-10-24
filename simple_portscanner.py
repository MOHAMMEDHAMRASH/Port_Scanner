import socket

def scan_ports(ip, ports):
    open_ports = []
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)  # Adjust the timeout as needed

        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    return open_ports

def main():
    target_ip = input("Enter the target IP address: ")
    target_ports = range(1, 1025)  # Scan common ports (1-1024)

    open_ports = scan_ports(target_ip, target_ports)

    if open_ports:
        print("Open ports on", target_ip, "are:", open_ports)
    else:
        print("No open ports found on", target_ip)

if __name__ == "__main__":
    main()
