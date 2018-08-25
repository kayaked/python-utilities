import requests
from bs4 import BeautifulSoup
import random
import itertools

def reddit():
    sel = input("u for user, b for batch, 4 for 4 letters: ")
    if sel.lower()=="u":
        user = input("input a username: ")
        if user.startswith("/u/"):
            user=user[3:]
        if user.startswith("u/"):
            user=user[2:]
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
        letters = "abcdefghijklmnopqrstuvwxyz1234567890-_"
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
        req = requests.get("https://www.reddit.com/api/username_available.json?user={}".format(usid), headers={'User-agent':'kitsunereddit'})
        if req.text == "false":
            """soup = BeautifulSoup(requests.get("https://www.reddit.com/user/{}".format(usid)).text, 'html.parser')
            deleted = soup.find(text='This user has deleted their account.')
            if deleted != None:
                unavailable.append("{} (deleted)".format(usid))
                continue"""
            unavailable.append(usid)
        elif req.text == "true":
            available.append(usid)
        else:
            pass
        os.system("cls") if os.name=='nt' else os.system("clear")
        print("Available: {}".format(", ".join(available)))
        print("Unavailable: {}".format(", ".join(unavailable)))
    
    chec = input("Add available names to output file? (Y/N): ")
    if chec=="Y":
        g = open("avail.log", 'a')
        with open("avail.log", 'r') as r:
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