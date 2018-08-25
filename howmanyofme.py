import sys, requests, re
from bs4 import BeautifulSoup


try:
    sys.argv[1]
    name = sys.argv[1:]
except Exception:
    print("Usage: howmanyofme.py \"firstname\" \"lastname\"")
    exit()

if len(name) > 2:
    name[1] = " ".join(name[1:])
    name = name[:1]

fname = name[0]
lname = name[1]

data=requests.post("http://howmanyofme.com/search/", data={'given':fname,'sur':lname,'ofage':'yes'})

soup = BeautifulSoup(data.text, 'html.parser')

li = soup.find_all('li')
li = [el for el in li if "in the U.S. named" in el.text]

li = li[0]



tex = li.find('span', {'class':'popnum'}).text

if "or fewer" in li.text:
    tex = tex + " (or fewer)"

print(tex)