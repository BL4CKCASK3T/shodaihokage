 #!/usr/bin/env python 

import socket
import os
from time import sleep

try: 
        TCP_IP = input("Enter Destination IP:")
try:
        TCP_PORT = input("Enter Destination Port:")

BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
print "received data:", data
