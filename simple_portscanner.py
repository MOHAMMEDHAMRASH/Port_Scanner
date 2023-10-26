import socket
import sys
from queue import Queue
import threading
from datetime import datetime
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    print('''
      
$$$$$$$\                       $$\                                                                      
$$  __$$\                      $$ |                                                                     
$$ |  $$ | $$$$$$\   $$$$$$\ $$$$$$\          $$$$$$$\  $$$$$$$\ $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\ 
$$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|        $$  _____|$$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$  ____/ $$ /  $$ |$$ |  \__| $$ |          \$$$$$$\  $$ /      $$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |      $$ |  $$ |$$ |       $$ |$$\        \____$$\ $$ |     $$  __$$ |$$ |  $$ |$$   ____|$$ |       
$$ |      \$$$$$$  |$$ |       \$$$$  |      $$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |\$$$$$$$\ $$ |      
\__|       \______/ \__|        \____/       \_______/  \_______|\_______|\__|  \__| \_______|\__|
|                                                                                                |
|--------------------------------------------Coded by HAMRASH--------------------------------------|''')

def get_target_ip():
    return socket.gethostbyname(input("Enter Your IP/Domain: "))

def get_scan_mode():
    print("Select your scan type: ")
    print("[*] Select 1 for 1 to 1024 port scanning")
    print("[*] Select 2 for 1 to 65535 port scanning")
    print("[*] Select 3 for custom port scanning")
    print("[*] Select 4 to exit\n")

    return int(input("[+] Select any option: "))

def get_custom_ports():
    start = int(input("[*] Enter starting port number: "))
    end = int(input("[*] Enter ending port number: "))
    return start, end

def scan_port(host, port):
    s = socket.socket()
    s.settimeout(5)
    result = s.connect_ex((host, port))
    if result == 0:
        try:
            service_name = socket.getservbyport(port)
        except OSError:
            service_name = "Unknown Service"
        print(f"Port {port} ({service_name}) is open")
    s.close()

def worker(queue):
    while not queue.empty():
        port = queue.get()
        scan_port(target_host, port)
        open_ports.append(port)

def run_scanner(threads, mode, target_host, custom_start, custom_end):
    queue = Queue()
    get_ports(queue, mode, custom_start, custom_end)
    thread_list = []

    for _ in range(threads):
        thread = threading.Thread(target=worker, args=(queue,))
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print(f"Scanning complete in: {datetime.now().strftime('%H:%M:%S')}")

def get_ports(queue, mode, custom_start, custom_end):
    if mode == 1:
        print("\n[+] Scanning...\n")
        for port in range(1, 1025):
            queue.put(port)
    elif mode == 2:
        print("\n[+] Scanning...\n")
        for port in range(1, 65536):
            queue.put(port)
    elif mode == 3:
        print("\n[+] Scanning...\n")
        for port in range(custom_start, custom_end + 1):
            queue.put(port)
    elif mode == 4:
        print("[-] Exiting...")
        sys.exit()
    elif mode not in [1, 2, 3, 4]:
        print("Invalid Command")
        sys.exit()

if __name__ == "__main__":
    print_banner()
    target_host = get_target_ip()
    scan_mode = get_scan_mode()

    custom_start, custom_end = 0, 0
    if scan_mode == 3:
        custom_start, custom_end = get_custom_ports()

    open_ports = []
    run_scanner(1021, scan_mode, target_host, custom_start, custom_end)
