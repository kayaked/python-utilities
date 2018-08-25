# jailbreak info
# by Yak/oganessium
# github.com/oganessium
# twitter.com/saucize
# Telegram: @communisms (or @y_o_k)
# Discord: Yak#7474
# Mesh: @y
# paypal ETA SON

import requests, re, traceback, sys, os
from bs4 import BeautifulSoup

try:
    sys.argv[1]
    query = " ".join(sys.argv[1:])
except IndexError:
    print("Usage: AJAPI.py [jailbreak]")
    exit()


print("JWI.py - Jailbreak Wiki Info by Yak")

# old scraper

"""info = requests.get("https://www.theiphonewiki.com/wiki/Jailbreak").text

soup = BeautifulSoup(info, 'html.parser')

Tables = soup.find_all('table', {'class':'wikitable'})

jailbreaks = []

for y in Tables:
    Table = y.find('tbody')


    find = [ section.find('a', href=re.compile('/wiki/')) for section in Table.find_all('tr') if section.find('th') == None and "No Tool Available" not in section.text]
    find = [huh for huh in find if huh != None]
    find = [huh.text for huh in find]
    jailbreaks = jailbreaks + find """

# end old scraper

soup = BeautifulSoup(requests.get("https://www.theiphonewiki.com/wiki/Category:Jailbreaks").text, 'html.parser')
jailbreaks = [a.text for a in soup.find('div', {'class':'mw-category'}).find_all('a')]
    
jailbreaks = list(set(jailbreaks))

if query.lower() == "list":
    print(", ".join(jailbreaks))
    exit()

if query.lower() == "greenpois0n":
    query = "Greenpois0n (jailbreak)" # Do not do this in your project. this is horrible hard code.

if query.lower() not in [huh.lower() for huh in jailbreaks]:
    req=requests.get("https://www.theiphonewiki.com/wiki/{}".format(query.lower().title()))
    if req.status_code == 200:
        TempSoup = BeautifulSoup(req.text, 'html.parser')
        S = TempSoup.find("h1", id="firstHeading")
        if S != None:
            query = S.text
            if query.lower() not in [huh.lower() for huh in jailbreaks]:
                print("Jailbreak not found! (not a jailbreak)")
                exit()
        else:
            print("Jailbreak not found! (no header)")
            exit()

        pass
    else:

        print("Jailbreak not found! (404)")
        exit()


indexed = [jb.lower() for jb in jailbreaks].index(query.lower())

query = jailbreaks[indexed]

info = requests.get("https://www.theiphonewiki.com/wiki/{}".format(query))

soup = BeautifulSoup(info.text, 'html.parser')
try:
    soup.find('div', {'class':'hatnote'}).decompose()
except:
    pass
title = soup.find('h1', id="firstHeading")
information = soup.find('div', {'class':'mw-parser-output'}).find_all('p')
authors = soup.find_all('tr')



for author in authors:
    if author != None:
        if author.find('th') == None:
            continue
        if "Developer" in author.find('th').text:
            TempSoup = BeautifulSoup(str(author.find('td')).replace("<br/>", "\n"), 'html.parser')
            author = TempSoup.text.splitlines()
            author.pop(0)
            author = ", ".join(author)
            break
        else:
            last_resort = soup.find('div', {'class':'mw-parser-output'}).find('p').text
            
            try:
                author = "{} (possible match)".format(last_resort.split("by ")[1].split()[0])
            except IndexError:
                last_resort = soup.find('div', {'class':'mw-parser-output'}).find('p').text
                
                try:
                    author = "{} (possible match)".format(last_resort.split("from ")[1].split()[0])
                except IndexError:
                    author = soup.find('a', title=re.compile('User:'))
                    try:
                        author = "{} ({}) (possible match)".format(author.text, author['href'].split("User:")[1])
                    except:
                        author = "Unknown"
else:
    credit = soup.find('div', {'class':'mw-parser-output'}).find('h2', text="Credit")
    if credit != None:
        credit = info.text.split("Credit</span></h2>")[1]
        sip = BeautifulSoup(credit, 'html.parser')
        author = sip.find().text.rstrip()
    else:
        last_resort = soup.find('div', {'class':'mw-parser-output'}).find('p').text
        
        try:
            author = "{} (possible match)".format(last_resort.split("by ")[1].split()[0])
        except IndexError:
            last_resort = soup.find('div', {'class':'mw-parser-output'}).find('p').text
            
            try:
                author = "{} (possible match)".format(last_resort.split("from ")[1].split()[0])
            except IndexError:
                author = soup.find('a', title=re.compile('User:'))
                try:
                    author = "{} ({}) (possible match)".format(author.text, author['href'].split("User:")[1])
                except:
                    author = "Unknown"


            

Kekman = "No info found!"

for p in information:
    if len(p.text) > 20:
        if p.text.count(". ") > 0 or p.text.rstrip().endswith("."):
            Kekman = p.text
            if p.text.rstrip().endswith(":"):
                lisd = soup.find('ul')
                elements = ["- " + li.text for li in lisd.find_all('li')]
                Kekman = p.text + "\n" + "\n".join(elements)

            break

if query.lower()=="purplera1n":
    Kekman = information[3].text + "\nThis info is formatted strangely. If this definition is incorrect, contact @saucize on twitter."

print("----------------------------------------")
print(title.text)
print("---------------------------------------------------")
print('Author: {}'.format(author))
print("----------------------------------------")
print(Kekman)
