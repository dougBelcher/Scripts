# RSS feed for news
import requests
import pyttsx3
import time
import xmltodict


def init_engine():
    # One time initialization
    engine = pyttsx3.init()  # object creation

    # Set properties _before_ you add things to say
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    return engine


def say(engine, txt):
    engine.say(txt)
    engine.runAndWait()


tts = init_engine()

feeds = {'CNN US News': 'http://rss.cnn.com/rss/cnn_us.rss',
         'CNN Top Stories': 'http://rss.cnn.com/rss/cnn_topstories.rss',
         'Google US News': 'https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en',
         'Reuters VIA Google': 'https://news.google.com/rss/search?q=when:24h+allinurl:reuters.com&ceid=US:en&hl=en-US&gl=US',
         'CNN World News': 'http://rss.cnn.com/rss/cnn_world.rss'}

for feed in feeds:
    print(f'{feed}')
    say(tts, feed)
    time.sleep(2)

    response = requests.get(feeds[feed])
    data = xmltodict.parse(response.content)

    seed = 0
    for datum in data['rss']['channel']['item']:
        title = datum['title']
        print(title)
        say(tts, title)
        time.sleep(1)
        seed = seed + 1
        if seed > 5:
            break
