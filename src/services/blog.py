import requests
import time


def beep():
    import winsound  # for sound
    import time  # for sleep

    winsound.Beep(440, 100)  # frequency, duration
    winsound.Beep(540, 100)  # frequency, duration
    winsound.Beep(640, 100)  # frequency, duration
    time.sleep(0.3)

url = 'http://consumer_services_api.talkpython.fm/api/blog'

title_count = -1

while True:
    resp = requests.get(url)
    resp.raise_for_status()

    data = resp.json()

    if title_count >= 0 and title_count != len(data):
        print("******** NEW POST *************")
        print("**** " + data[0].get('title'))
        beep()

    title_count = len(data)

    for d in data:
        print(d.get('title'))
    print()

    time.sleep(10.0)

