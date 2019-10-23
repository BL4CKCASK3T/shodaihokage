#!/usr/bin/env python

import socket
import os
import ipaddress

try: 
        TCP_IP = input("Enter Bind IP:")
        ipaddress.ip_network(TCP_IP)
except NameError:
        TCP_IP = "0.0.0.0"
try:
        TCP_PORT = int(input("Enter Bind Port:"))
except NameError:
        TCP_PORT = 8080
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data)
    conn.send(data)  # echo
conn.close()
