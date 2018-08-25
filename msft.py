# MSFTScraper - Microsoft Bundle ID Locator
# By jack (oganessium)
# @saucize/@trueyak, github.com/oganessium

from bs4 import BeautifulSoup as bs
import requests
print("=============================")
print("MSFTScraper - Microsoft Bundle ID Locator")
print("=============================")

def micro(query):
    req = requests.get("https://www.microsoft.com/en-us/store/search/apps?q={}".format(query.lower().replace(' ', '+')))
    soup = bs(req.text, 'html.parser')
    result = soup.find_all('section', {'class':'m-product-placement-item'}, limit=10)
    print("=============================================")
    if result == []:
        print("No results")
        print("=============================")
    for x in result:
        a = x.findChild('a', recursive=False)
        name = x.findChild('h3')
        print(name.text)
        try:
            print(a['data-pfns'])
        except KeyError:
            print("(None)")
        print("=============================")

    again = input("Search again? (Y/N): ")
    if again.lower() == "y":
        micro(input("App to search: "))
    else:
        print("=============================")
        print("Thank you for using MSFTScraper!")
        print("=============================")

micro(input("App to search: "))