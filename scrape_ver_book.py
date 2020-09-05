from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
#stock 이름만 바꾸면 알아서 긁어온다.

html_stats = urlopen('https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL.html')
bsObj = BS(html_stats.read(), "html.parser")

Current_Price = bsObj.body.find('span', {'class':"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})


#Current column을 다 뽑아와서 생각보다 쓸만하다.
current_column = bsObj.body.find_all('td', {'class':"Ta(c) Pstart(10px) Miw(60px) Miw(80px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor)"} )

ROAEBITDA = bsObj.body.find_all('td', {'class':"Fw(500) Ta(end) Pstart(10px) Miw(60px)", 'data-reactid': {'484','491','533'}} )

html_analysis = urlopen('https://finance.yahoo.com/quote/AAPL/analysis?p=AAPL.html')
bsObj = BS(html_analysis.read(), "html.parser")

test_List = bsObj.body.find_all('span', {'class': "Trsdu(0.3s) " })


#딕셔너리를 사용해서 저장
AAPL = {'Price':Current_Price.get_text(), 'Market_Cap' : current_column[0].get_text(), 'ROA' : ROAEBITDA[0].get_text(), 'ROE' : ROAEBITDA[1].get_text() , 'EPS_this_qtr' : test_List[4].get_text(),'EPS_nxt_qtr' : test_List[5].get_text(),  'EPS_this_yr' : test_List[6].get_text(), 'EPS_nxt_yr' : test_List[7].get_text(),  'Trailing_PE': current_column[2].get_text(), 'Forward_PE' : current_column[3].get_text() , 'PEG' : current_column[4],'Enterprise_Value' : current_column[1].get_text(), 'EBITDA' : ROAEBITDA[2].get_text(),'EV_EBITDA':  current_column[8].get_text(),'PBR' : current_column[6].get_text() }

print(AAPL)



'''
# id 검색 조건을 여러개 달 수 있구나. 
trailing_PE = bsObj.body.find('td', {'class':"Ta(c) Pstart(10px) Miw(60px) Miw(80px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor)", 'data-reactid': '112'} )
print(trailing_PE.get_text())
'''
