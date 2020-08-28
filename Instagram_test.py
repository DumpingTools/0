import requests
from host import search
import introduction
from Crawling import amount, dot
from brute import user
from stages import commands
import time
print("\n")
# Insert URL here
Website = "https://www.instagram.com"

print("\033[1;32;40m Starting process: \033[1;31;40m {}\n".format(commands[0]))
r = requests.get(Website)
f = open("Site.txt","w+")
f.write(str(r.text))
f.close()
u = 0
d = 7
v = open("valid_url.txt","w+")
f = open("url_list.txt","r+")
for url in f:
    try:
        r = requests.get(Website + url)
        if r.status_code == 200:
            v.write(Website + url)
    except:
        print("")
print("\033[1;31;40m Crawled Links are stored in: valid_url.txt")
time.sleep(2)
print("\033[1;32;40m Grabbing subdomains..\n")
search.whois(Website)
print("\n\033[1;32;40m Starting process: {}".format(commands[1]))
user()
print("\n\033[1;32;40m Starting process: {}".format(commands[2]))

