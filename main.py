import requests
from bs4 import BeautifulSoup
import webbrowser
from time import sleep

# The first url is the one we check the product availability
# The rest three are for testing purposes only

url = "https://www.flipkart.com/sony-playstation-5-cfi-1008a01r-825-gb-astro-s-playroom/p/itma0201bdea62fa"
url2 = "https://www.flipkart.com/msks-144-tc-cotton-double-printed-bedsheet/p/itm04a52ea36a410?pid=BDSGF8YRZEYGEDXV&lid=LSTBDSGF8YRZEYGEDXVNGMHS1&marketplace=FLIPKART&store=jra%2Fknw%2Fqcw&srno=b_1_1&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_4.dealCard.OMU_PD9WSIRXSPA4_3&otracker1=hp_omu_SECTIONED_manualRanking_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_3&fm=neo%2Fmerchandising&iid=en_WvWUDpE4cg6%2BbTWo39j8d%2FUB8fmGSkMyLZW5UjqoJXurphmxdX3q%2BZSklwLr%2B6h12IrxNew8UN5k8hrDPCz3TQ%3D%3D&ppt=browse&ppn=browse&ssid=k0fgkllltc0000001621439178255"
url3 = "https://www.flipkart.com/tabaret-sup-400-1-games-retro-game-box-console-8-gb-fifa-14/p/itm1efae0ce157b7?pid=GMCFKG7UUNW7TF3S&lid=LSTGMCFKG7UUNW7TF3SW0CMNE&marketplace=FLIPKART&q=ps4&store=4rr%2Fx1m%2Fwym&srno=s_1_3&otracker=search&otracker1=search&fm=SEARCH&iid=c53fba62-b775-4d9e-aaf3-c1a8a169a919.GMCFKG7UUNW7TF3S.SEARCH&ppt=sp&ppn=sp&ssid=vww7veh05c0000001621445712344&qH=0e740342f31e9aa6"
url4 = "https://www.flipkart.com/airtel-amf-311ww-data-card/p/itm74cfab0443198?pid=DATFUKXTCGXQUC3Y&lid=LSTDATFUKXTCGXQUC3YEQYRYT&marketplace=FLIPKART&store=6bo%2Fo47&srno=b_1_1&otracker=hp_omu_Top%2BDeals%2Bon%2BElectronics_2_10.dealCard.OMU_72KF9YP4INE7_6&otracker1=hp_omu_WHITELISTED_neon%2Fmerchandising_Top%2BDeals%2Bon%2BElectronics_NA_dealCard_cc_2_NA_view-all_6&fm=neon%2Fmerchandising&iid=2f63bbc7-f2e2-43c1-ae17-d253a4535653.DATFUKXTCGXQUC3Y.SEARCH&ppt=hp&ppn=homepage&ssid=wicfiw88gw0000001621447286257"

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
    if any(list in txt.get_text() for list in lists) and not txt.get('disabled') == None:
        flag = 1
        print("Product Available")
        sleep(2)
        webbrowser.open(url)
        break

if flag == 0:
    print("Not Available")
