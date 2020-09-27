#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
from typing import List, Any

import requests, os, bs4
from bs4 import BeautifulSoup
from requests import Response

url = 'https://xkcd.com'  # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd
while not url.endswith('#'):
    # Download the page.
    print(f'Downloading page {url}...')
    res: Response = requests.get(url)
    res.raise_for_status()

    soup: BeautifulSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    # Find the URL of the comic image.
    comicElem: List[Any] = soup.select('#comic img')
    if not comicElem:
        print(f'Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')
        # Download the image.
        print(f'Downloading image https: {comicUrl}')
        # 2067 - 2018 midterm challenger map
        # 2198 - throw calculator (the keys to successfully throwing a party are location, planning
        #           , and one of those aircraft carrier steam catapults)
        # 1880 - Eclipse Review ()
        # 1663 - garden (relax)
        # 1608 - hoverboard game ()
        # 1525 - Emojic 8ball ()
        # 1416 - pixels (it's turtles all the way down)
        # 1350 - lorenz (every choice, no matter how small, begins a new story)
        # 1331 - frequency (est avg freq events happen)
        if ("2067" not in url) \
                and ("1525" not in url) \
                and ("1880" not in url) \
                and ("1331" not in url)\
                and ("2198" not in url):
            res = requests.get('https:' + comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print(f'Done.')
