import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup

count = 0
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url- ")
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('p')
for tag in tags:
    count += 1
print(count)
