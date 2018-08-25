import requests, bs4, sys, json, re
try:
    sys.argv[1]
except:
    exit()
data = requests.get("https://www.instagram.com/{}".format(sys.argv[1]))

soup = bs4.BeautifulSoup(data.text, 'html.parser')

bloc = json.loads(soup.find('script', text=re.compile('window._sharedData')).text.split("window._sharedData = ")[1][:-1])['entry_data']['ProfilePage'][0]['graphql']['user']
# let me break this down real quick
# "soup" is a BeautifulSoup object, finding stuff in "data", which is basically the HTML code for instagram
# soup.find('script') finds <script> in code, and text=re.compile('window._sharedData') makes sure it's the right one
# then it splits it at where the data is, cuts off the end, then uses "json.loads" which changes the text into an python dictionary.
# the stuff at the end just tells it to go to the right place in the dictionary

# hope this helped



print("{} (@{})".format(bloc['full_name'], bloc['username']))
print(bloc['biography'])
print("--------------------------------")
print("Followers: {}".format(bloc['edge_followed_by']['count']))
print("Following: {}".format(bloc['edge_follow']['count']))
print("Posts: {}".format(bloc['edge_owner_to_timeline_media']['count']))
print("-----------------")
print("PFP URL: {}".format(bloc['profile_pic_url_hd']))
print('Verified: {}'.format(bloc['is_verified']))
print('Private: {}'.format(bloc['is_private']))