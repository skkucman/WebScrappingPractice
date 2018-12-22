import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re


ch_driver = webdriver.Chrome('C:\\Python37\\chromedriver.exe')

ch_driver.get('http://www.g2b.go.kr:8097/servlet/sub02/XZMOK_SMOK_MListView')

ch_driver.find_element_by_id('top-sub-menu2').find_element_by_tag_name('a').click()


category_input = ch_driver.find_element_by_id("CATE_ID")
category = '30131502'
category_input.send_keys(category)

search_btn = ch_driver.find_element_by_id('Search')
search_btn.click()


'''
page = ch_driver.find_element_by_class_name('page').find_elements_by_tag_name('a')
page[0].get_attribute('href')

'http://www.g2b.go.kr:8097/servlet/sub02/XZMOK_SMOK_MListView?ischks=N&system=sp&cmd=
&cate_id=&CATE_ID=30131502&PROD_ID=&CATE_NAME=&CERT_CODE=&CATE_NAME_EN=&KN_KNCDNAME=&GB_KNCD=
&sort1=&sort2=&page_size=x3oQQBDo_gO8dzdFYsllyw==&tot=33422isSearch=Y
&pg_no=_VjIvpMrTFDjzXIAEH0JSw=='

page = ch_driver.find_element_by_class_name('page').text
'[1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [다음] [끝]'
'''

p = re.compile(r'\/\d+\]')
str_page = ch_driver.find_element_by_class_name('Right').text
total_page = int(p.search(str_page).group().strip('/[]'))

total_page

'''def get_product_info():
    for item in trs:
        item_dict=dict()
        #url_prefix = 'http://www.g2b.go.kr:8097'
        #product_image = url_prefix + tr.find_all('td')[0].a['href']
        category_subno = item.find_all('td')[1].text
        product_no = item.find_all('td')[2].text
        category_name = item.find_all('td')[3].text
        product_name = item.find_all('td')[4].text
        product_type = item.find_all('td')[5].text
        item_dict[product_no]= dict([(name,eval(name)) for name in _
                                  ["category_subno","category_name","product_name","product_type"]])   

        product_dict.append((item_dict))
'''

product_dict = dict()

for i in range(1,20+1):
    if i == 1:
        pass
    elif i % 10 == 1:
        #print(i)
        ch_driver.find_element_by_link_text('[다음]').click()
    else:
        #print(i)
        ch_driver.find_element_by_link_text(str(i)).click()
        
    html = ch_driver.page_source
    soup = BeautifulSoup(html,'lxml')
    trs = soup.find('table',attrs={'class':'tb02'}).tbody.find_all('tr')
    for item in trs:
        category_subno = item.find_all('td')[1].text
        product_no = item.find_all('td')[2].text
        category_name = item.find_all('td')[3].text
        product_name = item.find_all('td')[4].text
        product_type = item.find_all('td')[5].text
        product_dict[product_no]= dict([(name,eval(name)) for name in 
                                      ["category_subno","category_name","product_name","product_type"]])