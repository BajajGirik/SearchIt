import requests
from bs4 import BeautifulSoup

url = "https://www.geeksforgeeks.org/"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

#Use this to view the content of the page nicely
#print(soup.prettify())

#Use this to get the text inside the tags
#print(soup.title.get_text())

