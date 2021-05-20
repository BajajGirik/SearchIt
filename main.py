import requests
from bs4 import BeautifulSoup
import webbrowser
from time import sleep

def searchQuery(str):
    str += '+'
    return str

n = input().split()
new_ns = list(map(searchQuery,n[:-1]))
url = 'https://www.google.com/search?q='

for new_n in new_ns:
    url += new_n

url += n[-1]

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
    if any(list in txt for list in lists) and txt.get('disabled') == None:
        flag = 1
        print("Product Available")
        sleep(2)
        webbrowser.open(url)
        break

if flag == 0:
    print("Not Available")