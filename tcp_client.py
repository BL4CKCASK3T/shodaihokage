 #!/usr/bin/env python 

import socket

try: 
        TCP_IP = "100.115.92.196" 
except NameError:
        TCP_IP = "127.0.0.1"
try:
        TCP_PORT = 80
except NameError:
        TCP_PORT = 5005

BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
print "received data:", data
