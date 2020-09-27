import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_Url = 'http://centslessbooks.com/science-fiction.html'
uClient = uReq(my_Url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
uClient.close()
