# PlayScraper - Android Bundle ID Locator
# By jack (oganessium)
# @saucize/@trueyak, github.com/oganessium

from bs4 import BeautifulSoup as bs
import requests
print("=============================")
print("PlayScraper - Android Bundle ID Locator")
print("=============================")

def android(query):
    req = requests.get("https://play.google.com/store/search?q={}&c=apps".format(query.lower().replace(' ', '+')))
    soup = bs(req.text, 'html.parser')
    result = soup.find_all('a', {'class':'title'}, limit=10)
    print("=============================================")
    if result == []:
        print("No results")
        print("=============================")
    for x in result:
        print(x.text[2:])
        print(x['href'].split('?id=')[1])
        print("=============================")
    again = input("Search again? (Y/N): ")
    if again.lower() == "y":
        android(input("App to search: "))
    else:
        print("=============================")
        print("Thank you for using PlayScraper!")
        print("=============================")

android(input("App to search: "))