
import requests
import re

# Will be updated in the future to allow input and such
user = "pewdiepie"
url = 'https://www.instagram.com/' + user
r = requests.get(url).text
followers = re.search('"edge_followed_by":{"count":([0-9]+)}',r).group(1)

print(followers)