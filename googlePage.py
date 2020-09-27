from selenium import webdriver

# Old way of doing things that works with Firefox
#driver = webdriver.Firefox()
#driver.get("http:google.com")

chromedriver = "P:\chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("http:google.com")
