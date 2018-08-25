import requests
from bs4 import BeautifulSoup
import random
import itertools

def reddit():
    sel = input("u for user, b for batch, 5 for 5 letters: ")
    if sel.lower()=="u":
        user = input("input a username: ")
        array = [x for x in user.split(", ")]
    elif sel.lower()=="b":
        bb = input("link for batch data: ")
        data = requests.get(bb).text
        data = data.splitlines()
        array = [line for line in data]
    elif sel.lower() == "6":
        try:
            numb = input("Input number of random 6 letter usernames to scrape: ")
        except EOFError:
            exit()
        if not numb.isdigit():
            numb=1
        letters = "abcdefghijklmnopqrstuvwxyz1234567890_"
        array = []
        for _ in itertools.repeat(None, int(numb)):
            query = random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters)
            array.append(query)
    elif sel.lower() == "6l":
        try:
            numb = input("Input number of random 6 letter usernames to scrape: ")
        except EOFError:
            exit()
        if not numb.isdigit():
            numb=1
        letters = "abcdefghijklmnopqrstuvwxyz_"
        array = []
        for _ in itertools.repeat(None, int(numb)):
            query = random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters)
            array.append(query)
    elif sel.lower() == "d":
        try:
            numb = input("Input number of words to scrape: ")
        except EOFError:
            exit()
        if not numb.isdigit():
            numb=1
        array = []
        for _ in itertools.repeat(None, int(numb)):
            req = requests.get("https://randomword.com/").text
            soup = BeautifulSoup(req, 'html.parser')
            word = soup.find('div', id='random_word')
            array.append(word.text)
    else:
        print("invalid option")
        import os
        os.system('pause')
        exit()
    
    available = []
    unavailable = []
    import os
    for usid in array:
        req = requests.get("https://mail.google.com/mail/gxlu?email={}".format(usid), headers={'User-agent':'kitsunereddit'}).headers
        try:
            req['Set-Cookie']
            unavailable.append(usid)
        except KeyError:
            if len(usid)<6:
                unavailable.append(usid)
            else:
                available.append(usid)
        else:
            pass
        os.system("cls") if os.name=='nt' else os.system("clear")
        print("Available: {}".format(", ".join(available)))
        print("Unavailable: {}".format(", ".join(unavailable)))
    
    chec = input("Add available names to output file? (Y/N): ")
    if chec=="Y":
        g = open("gavail.log", 'a')
        with open("gavail.log", 'r') as r:
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

print("As of August 25, 2018, this does not appear to work. Google likely added some kinda password thing")
reddit()