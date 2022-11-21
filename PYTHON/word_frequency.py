import urllib.request
import urllib.parse
import urllib.error

fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
frequency = 0
for line in fhandle:
    words = line.decode()
    frequency = frequency + len(words)
    if frequency < 3000:
        print(line.decode().strip())
print(frequency)
