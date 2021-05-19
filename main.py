import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/sony-playstation-5-cfi-1008a01r-825-gb-astro-s-playroom/p/itma0201bdea62fa"
url2 = "https://www.flipkart.com/msks-144-tc-cotton-double-printed-bedsheet/p/itm04a52ea36a410?pid=BDSGF8YRZEYGEDXV&lid=LSTBDSGF8YRZEYGEDXVNGMHS1&marketplace=FLIPKART&store=jra%2Fknw%2Fqcw&srno=b_1_1&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_4.dealCard.OMU_PD9WSIRXSPA4_3&otracker1=hp_omu_SECTIONED_manualRanking_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_3&fm=neo%2Fmerchandising&iid=en_WvWUDpE4cg6%2BbTWo39j8d%2FUB8fmGSkMyLZW5UjqoJXurphmxdX3q%2BZSklwLr%2B6h12IrxNew8UN5k8hrDPCz3TQ%3D%3D&ppt=browse&ppn=browse&ssid=k0fgkllltc0000001621439178255"

r = requests.get(url2)
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
