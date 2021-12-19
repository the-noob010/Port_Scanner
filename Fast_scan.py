#!/usr/bin/python3

import socket
import sys
import time
import threading

usage = "python3 main.py TARGET START_PORT END_PORT"

# only for style
print("-" * 70)
print()
print("Simple Python Port Scanner")
print()
print("-" * 70)

if len(sys.argv) != 4:
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:  # gai means *get address info*
    print("Name resolution error")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])
print("Scanning target:", target)


def scan_port(port):
    #print("Scanning port:", port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    # sock_stream means TCP ports
    # AF_Inet means address family of Internet and IPv4
    conn = s.connect_ex((target, port))
    if not conn:
        print("Port {} is OPEN".format(port))
    s.close()


for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()
