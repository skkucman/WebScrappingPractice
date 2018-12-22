'''
To Do : 서울시 홈페이지 뉴스내용을 1~10페이지의 각 뉴스ID, 제목, 업데이트일시, 주제, 
        텍스트를 가져오기
최종 데이터 셋 형태 {'News ID':[제목, 업데이트일시, 주제, 텍스트]}
'''

import requests
from bs4 import BeautifulSoup
#import selenium
from selenium import webdriver
import time
#from datetime import datetime


ch_driver = webdriver.Chrome('C:\\Python37\\chromedriver.exe')

ch_driver.get('http://www.seoul.go.kr/main/index.jsp')

link = ch_driver.find_element_by_link_text('전체보기')
link.click()

news_dict = dict()

for i in range(1,10+1):
    fnpage = 'javascript:fnPagingMove(' + str(i) + ');'
    ch_driver.execute_script(fnpage)
    time.sleep(5)
    items = ch_driver.find_elements_by_class_name('item')

    for item in items:
        news_id = item.find_element_by_class_name('subject').text[1:6]
        news_subject = item.find_element_by_class_name('subject').text[7:].strip(' ')
        news_link = item.find_element_by_tag_name('a').get_attribute('href')
        news_update_dt = item.find_element_by_class_name('date').text[:19]
        news_category = item.find_element_by_class_name('date').text[20:].strip('[]')
        news_txt = item.find_element_by_class_name('txt').text.replace('\n','')
        news_dict[news_id]= dict([(name,eval(name)) for name in 
                                  ["news_subject","news_link","news_update_dt","news_category","news_txt"]])   

news_dict