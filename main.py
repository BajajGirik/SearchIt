import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import webbrowser
from time import sleep

def searchQuery(str):
    str += '+'
    return str

n = input("What would you like to buy today: ").split()
new_ns = list(map(searchQuery,n))
url = 'https://www.google.com/search?q='

for new_n in new_ns:
    url += new_n

url += 'flipkart'

driver = webdriver.Chrome(executable_path = '/usr/local/bin/chromedriver')
driver.get(url)
googleSearch = driver.page_source
driver.close()

soup = BeautifulSoup(googleSearch, 'html.parser')

url = ''
msg = 'Alas!....Currently Unavailable'
searchResults = soup.find_all(class_ = 'yuRUbf')


# Searching for the link which has desired content
for searchResult in searchResults:
    if searchResult.nextSibling.div != None:
        url = searchResult.a.get('href')
        break  

#if link not found
if url == '':
    url = searchResults[0].a.get('href')
    msg = 'Select the one you like...'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# Use this to view the content of the page nicely
# print(soup.prettify())

# Use this to get the text inside the tags
# print(soup.title.get_text())

# Use this to get values of the entered property (in this case: href)
# anchor = soup.find('a').get('href')
# or
# anchor = soup.find('a')['href']

# To get all links... use soup.find_all('a') 
# This will generate a list of all the a tags

txts = soup.find_all(class_ = '_2KpZ6l')
lists = ['ADD TO CART', 'BUY NOW']
flag = 0

for txt in txts:
    if any(list in txt.get_text() for list in lists) and txt.get('disabled') == None:
        flag = 1
        print("Hurray!....Product is Available")
        sleep(1)
        webbrowser.open(url)
        break

if flag == 0:
    print(msg)
    sleep(1)
    webbrowser.open(url)