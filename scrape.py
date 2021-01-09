import pandas as pd
from bs4 import BeautifulSoup
import re
from selenium import webdriver
#import chromedriver_binary
import string
pd.options.display.float_format = '{:.0f}'.format

is_link = 'https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL'
driver = webdriver.Safari()
driver.get(is_link)
html = driver.execute_script('return document.body.innerHTML;')
soup = BeautifulSoup(html,'lxml')

#close_price = [entry.text for entry in soup.find_all('span', {'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})]
#mrkt_cap = [entry.text for entry in soup.find_all('td', {'class':'Ta(c) Pstart(10px) Miw(60px) Miw(80px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor'})]
nameList = soup.find_all('td', {'class':'Ta(c) Pstart(10px) Miw(60px) Miw(80px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor'})


'''
ROA
ROE
trail_PE
forward_PE
EV
EBITDA
EV/EBITDA
PBR
'''
print(nameList)


'''
features = soup.find_all('div', class_='D(tbr)')

headers = []
temp_list = []
label_list = []
final = []
index = 0
#create headers
for item in features[0].find_all('div', class_='D(ib)'):
    headers.append(item.text)
#statement contents
while index <= len(features)-1:
    #filter for each line of the statement
    temp = features[index].find_all('div', class_='D(tbc)')
    for line in temp:
        #each item adding to a temporary list
        temp_list.append(line.text)
    #temp_list added to final list
    final.append(temp_list)
    #clear temp_list
    temp_list = []
    index+=1
df = pd.DataFrame(final[1:])
df.columns = headers
'''