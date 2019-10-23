 #!/usr/bin/env python 

import socket
import os
import ipaddress

try: 
        TCP_IP = input("Enter Destination IP:")
        ipaddress.ip_network('TCP_IP')
except NameError:
        TCP_IP = 127.0.0.1
try:
        TCP_PORT = input("Enter Destination Port:")
except NameError:
        TCP_PORT = 8080

BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
print "received data:", data
