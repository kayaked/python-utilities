import requests, json, sys
from bs4 import BeautifulSoup as bs

print("IGDB Scraper - ANOTHER God damn scraper")
print("------------------------------------------")
game = input("Game: ")

print("got input")

soup = bs(requests.get("https://www.igdb.com/search?utf8=%E2%9C%93&type=1&q={}".format(game)).text, 'html.parser')

print("requested igdb data")

api = json.loads(soup.find('div', id='results_json')['data-json'])

print("got results_json")

games = [ [x['data']['name'], x['data']['url'] ] for x in api ]

print("got game list")

for x in games:
    print("[{}] {}".format(games.index(x)+1, x[0]))
num = input("Select game by number: ")

if not num.isdigit():
    print("must input number value!")
    exit()

print("got game")

data = requests.get("https://www.igdb.com{}".format(games[int(num)-1][1]))

print("requested igdb data")

soup = bs(data.text, 'html.parser')

print("interpreted html")

jso = json.loads(soup.find('div', {'data-react-class':'GamePageHeader'})['data-react-props'])

# Print just the jso variable here for a nice JSON igdb API (Taken directly from their source too!)

try:
    if sys.argv[1] == "--json":
        print(jso)
        exit()
except Exception:
    pass

print(jso['name'])
print("----------------------------")
print("Developer(s): {}".format(", ".join([dev[0] for dev in jso['developers']])))
print("Released originally {}, for platforms {}".format(jso['release_date'], ", ".join(list(reversed([dev[0] for dev in jso['platforms']])))))
print("Genres: {}".format(", ".join([dev['name'] for dev in jso['genres']])))
print("----------------------------")
print(jso['summary'].replace("</p>", "").replace("<p>", "").replace("<br />", ""))