#!/usr/bin/python
import socket
import time
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("172.22.198.200",9090))
time.sleep(2)
sock.send("1")
print sock.recv(1024)
time.sleep(2)
sock.close()
