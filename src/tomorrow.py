import requests
import datetime

t0 = datetime.datetime.now()

url = 'http://consumer_services_api.talkpython.fm/api/blog'
resp = requests.get(url)
data = resp.json()

dt = datetime.datetime.now() - t0

print("Time: {}".format(dt.total_seconds()))
print(data)