import requests, bs4, sys, json
try:
    sys.argv[1]
except:
    exit()
data = requests.get("https://twitter.com/{}".format(sys.argv[1]))

soup = bs4.BeautifulSoup(data.text, 'html.parser')

bloc = json.loads(soup.find('input', id='init-data')['value'])['profile_user']

# bloc = twitter API user equiv

print("{} (@{})".format(bloc['name'], bloc['screen_name']))
print(bloc['description'])
print("--------------------------------")
print("Followers: {}".format(bloc['followers_count']))
print("Following: {}".format(bloc['friends_count']))
print("-----------------")
print("PFP URL: {}".format(bloc['profile_image_url_https'].replace('normal', '400x400')))
try:
    print("Banner URL: {}".format(bloc['profile_banner_url']))
except:
    print("Banner URL: N/A")
print('Verified: {}'.format(bloc['verified']))