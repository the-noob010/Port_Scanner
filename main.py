#!/usr/bin/python3

import socket
import sys
import time

usage = "python3 main.py TARGET START_PORT END_PORT"
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

for port in range(start_port, end_port + 1):
    print("Scanning port:", port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    # sock_stream means TCP ports
    # AF_Inet means address family of Internet and IPv4
    print("Scanning target:", target)
    conn = s.connect_ex((target, port))
    if not conn:
        print("Port {} is OPEN".format(port))
    s.close()
