import requests
import bs4

url = 'https://www.ft.com/?mhq5j=e1'
css = '.o-teaser__heading'

resp = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'})
resp.raise_for_status()

# print(resp.text)
soup = bs4.BeautifulSoup(resp.text, "html.parser")
# print(soup)

# first = set('thing 1', 'thing 2')
# second = set('thing 1', 'thing 2')
#
# if first.difference(second):
#     # new

results = soup.select(css)
for r in results:
    print(r.get_text().strip())

