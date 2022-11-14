import socket
import os

Host = raw_input("Enter a url: ")
try:
    if Host.startswith("http://"):
        hostname = Host.split('/')
        hostname = hostname[2]
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect((hostname, 80))
    elif Host.startswith("https://"):
        hostname = Host.split('/')
        hostname = hostname[2]
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect((hostname, 80))
except:
    print('You have entered an improperly formatted or non-exisent URL - ', Host)
    exit()

cmd = ('GET ' + Host + ' HTTP/1.0\r\n\r\n').encode()
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if (len(data)) < 1:
        break
    print(data.decode())
mysocket.close()
