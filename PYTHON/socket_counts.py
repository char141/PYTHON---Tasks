import socket
import os

urlname = raw_input("Enter url: ")
try:
    if urlname.startswith("http://"):
        hostname = urlname.split('/')
        hostname = hostname[2]
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect((hostname, 80))
    elif urlname.startswith("https://"):
        hostname = urlname.split('/')
        hostname = hostname[2]
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect((hostname, 80))
except:
    print("Invalid Input!")
    exit()

mysocket.send(('GET' + urlname + 'HTTP/1.0\r\n\r\n').encode())
counts = 0
while True:
    data = mysocket.recv(512)
    if (len(data)) < 1 or (counts >= 3000):
        break
    print(data.decode())
mysocket.close()
print(counts)
