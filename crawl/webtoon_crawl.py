#import pandas as pd
#import numpy as np
import time
import os

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=1920x1080')
#options.add_argument('disable-gpu')

dr = webdriver.Chrome('chromedriver',chrome_options=options)
url = 'https://webtoon.kakao.com/original-webtoon?tab=mon'

dr.get(url)

# 메뉴 url 누르기
dr.find_element(by=By.XPATH, value='//*[@id="root"]/main/div/div/div[1]/div[2]/div[2]/div/a[2]').click()

#dr.get_screenshot_as_file('screen_1_headless.png')


# login url 누르기
try:
    click_but = WebDriverWait(dr,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/main/div/div/div[2]/div[2]/div[1]/a')))
    click_but.click()
except Exception as e:
    print('error: ',e)
    
# '카카오 계정 직접 입력' 버튼 누르기
try:
    click_but = WebDriverWait(dr,10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div/div[1]/div[1]/div/div/button')))
#    click_but.click()
    click_but.send_keys(Keys.ENTER)
except Exception as e:
    print('error: ',e)

# time.sleep(10)
# elements = dr.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/div[1]/div/div/button')
# print(elements.is_enabled())

# dr.find_element()

#loginid = driver.find_element()

#html_source = dr.page_source

#soup = BeautifulSoup(html_source, 'html.parser')
time.sleep(6)

dr.get_screenshot_as_file('last_screen_headless.png')
dr.quit()