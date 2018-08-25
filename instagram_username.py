import requests
import random
import itertools

# credit goes to githubgist @tobbbles i believe

passed = input("Instagram name: ")
array = [passed]
if passed.lower() == "4":
    try:
        numb = input("Input number of random 3 letter usernames to scrape: ")
    except EOFError:
        exit()
    if not numb.isdigit():
        numb=1
    letters = "abcdefghijklmnopqrstuvwxyz1234567890"
    letters_sp = "abcdefghijklmnopqrstuvwxyz1234567890._"

    # This is due to no periods and underscores being allowed at beginning/end (afaik).

    array = []
    for _ in itertools.repeat(None, int(numb)):
        query = random.choice(letters) + random.choice(letters_sp) + random.choice(letters_sp) + random.choice(letters)
        array.append(query)

for name in array:
    headers = {
        'origin':'https://www.instagram.com/',
        'accept-encoding' : 'gzip, deflate, br',
        'x-requested-with': 'XMLHttpRequest',
        'x-csrftoken': '111',
        'cookie':'mid=111; ig_pr=2; ig_vw=632; csrftoken=111',
        'x-instagram-ajax':'1',
        'content-type':'application/x-www-form-urlencoded',
        'accept':'*/*',
        'referer':'https://www.instagram.com/',
        'authority':'www.instagram.com',
        'dnt':'1'
    }

    data = {
        'email':'',
        'password':'',
        'username':name,
        'first_name':''
    }

    req=requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/', headers=headers, data=data).json()
    try:
        req['errors']['username']
        print('{}: unavailable'.format(name))
    except Exception:
        print(req)
        print('{}: available'.format(name))