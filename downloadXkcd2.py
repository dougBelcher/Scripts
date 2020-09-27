#! python3
# downloadXfcd2.py Downloads every single XKCD comic.

import requests
from bs4 import BeautifulSoup as bs
import os
import pdb

# starting url
url = 'https://www.xkcd.com'
# print(url)

# download page for parsing
page = requests.get(url)
# print(page)
soup = bs(page.text, 'html.parser')
print(soup)

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for model images
if not os.path.exists('xkcd'):
    # print('Step 1')
    os.makedirs('xkcd')

# move to new directory
os.chdir('xkcd')
# print('Step 2')

# image file name variable
x = 0
# print('Step 3')
# writing images
for image in image_tags:
    try:
        print('Step 1 - ' + image)
        url = image['src']
        print('Step 2 ' + url)
        response = requests.get(url)
        print('Step 1 - ' + response)
        if response.status_code == 200:
            with open('xkcd-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except: pass
