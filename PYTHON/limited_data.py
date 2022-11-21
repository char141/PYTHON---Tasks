import socket
import os
import re

user_url = raw_input("Enter URL: ")
try:
    if user_url.startswith("http://"):
        hostname = user_url.split('/')
        hostname = hostname[2]
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect((hostname, 80))
    elif user_url.startswith("https://"):
        hostname = user_url.split('/')
        hostname = hostname[2]
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect((hostname, 80))
except:
    print("Invalid or non-existent url")
    exit()

cmd = ('GET' + user_url + ' HTTP/1.0\r\n\r\n').encode()
mysocket.send(cmd)

data = mysocket.recv(512)
message = data.decode()
header_end_position = message.find('\r\n\r\n') + 4
print(message[header_end_position:])

while True:
    data = mysocket.recv(512)
    if not data:
        break
    print(data.decode())
mysocket.close()
