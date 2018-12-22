import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


ch_driver = webdriver.Chrome('C:\\Python37\\chromedriver.exe')
ch_driver.get('http://www.g2b.go.kr:8100/index.jsp')


search_product = ch_driver.find_element_by_xpath("//*[@id='top-sub-menu2']/li[1]/a")
search_product.click()
#//*[@id="top-sub-menu2"]/li[1]/a

category_input = ch_driver.find_element_by_id("CATE_ID")
category = '30131502'
category_input.send_keys(category)

search_btn = ch_driver.find_element_by_id('Search')
search_btn.click()

#time.sleep(90)

html = ch_driver.page_source
soup = BeautifulSoup(html,'lxml')
trs = soup.find('table',attrs={'class':'tb02'}).tbody.find_all('tr')
image_url_prefix = 'http://www.g2b.go.kr:8097/'

product_dict = dict()

for tr,i in zip(trs,range(len(tds))):
    product_image = image_url_prefix + tr.find_all('td')[0].a['href']
    category_subno = tr.find_all('td')[1].text
    product_no = tr.find_all('td')[2].text
    category_name = tr.find_all('td')[3].text
    product_name = tr.find_all('td')[4].text
    product_type = tr.find_all('td')[5].text
    product_dict[product_no]=dict([(name,eval(name)) for name in 
                                   ["product_image","category_subno","category_name","product_name","product_type"]])

print(product_dict)