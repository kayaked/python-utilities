import requests
from bs4 import BeautifulSoup
import random
import itertools

def reddit():
    print("KitsunePornhub - Yet another exact copy of KitsuneReddit")
    sel = input("u for user, b for batch, 3 for 3 letters: ")
    if sel.lower()=="u":
        user = input("input a username: ")
        array = [x for x in user.split(", ")]
    elif sel.lower()=="b":
        bb = input("link for batch data: ")
        data = requests.get(bb).text
        data = data.splitlines()
        array = [line for line in data]
    elif sel.lower() == "3":
        try:
            numb = input("Input number of random 3 letter usernames to scrape: ")
        except EOFError:
            exit()
        if not numb.isdigit():
            numb=1
        letterss = "abcdefghijklmnopqrstuvwxyz1234567890"
        letters = "abcdefghijklmnopqrstuvwxyz1234567890-_"
        array = []
        for _ in itertools.repeat(None, int(numb)):
            query = random.choice(letterss) + random.choice(letters) + random.choice(letterss)
            array.append(query)
    elif sel.lower() == "3l":
        try:
            numb = input("Input number of random 3 letter usernames to scrape: ")
        except EOFError:
            exit()
        if not numb.isdigit():
            numb=1
        letters = "abcdefghijklmnopqrstuvwxyz"
        array = []
        for _ in itertools.repeat(None, int(numb)):
            query = random.choice(letters) + random.choice(letters) + random.choice(letters)
            array.append(query)
    else:
        print("invalid option")
        import os
        os.system('pause')
        exit()
    
    available = []
    unavailable = []
    import os
    for usid in array:
        req = requests.get("https://pornhub.com/users/{}".format(usid))
        if req.status_code==200:
            unavailable.append(usid)
        elif req.status_code==404:
            available.append(usid)
        else:
            pass
        os.system("cls") if os.name=='nt' else os.system("clear")
        print("Available: {}".format(", ".join(available)))
        print("Unavailable: {}".format(", ".join(unavailable)))
    
    chec = input("Add available names to output file? (Y/N): ")
    if chec=="Y":
        g = open("ph_avail.log", 'a')
        with open("ph_avail.log", 'r') as r:
            data = r.read()
        data=data.splitlines()
        for name in available:
            if name in data:
                continue
            g.write("{}\n".format(name))
        g.close()
    else:
        pass
    import os
    os.system('pause')

reddit()