import requests
from bs4 import BeautifulSoup

url = "https://www.geeksforgeeks.org/"

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

