#import pandas as pd
#import numpy as np
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import time, os, requests

from urllib.parse import unquote_plus
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

img_folder = './img'

if not os.path.isdir(img_folder):
    os.mkdir(img_folder)

co = Options()
#co.add_argument('headless')
#co.add_argument('disable-gpu')
co.add_experimental_option('debuggerAddress','127.0.0.1:9222')
dr = webdriver.Chrome(options=co)

sec1 = ['mon','complete'] # ii
sec2 = ['mon','tue','wed','thu','fri','sat','sun'] # ii
typ = ['webtoon','novel'] # jj

title_cl = 'whitespace-pre-wrap break-all break-words overflow-hidden text-ellipsis !whitespace-nowrap s22-semibold-white leading-33 mb-1'
title_xp = f'//p[contains(@class, "{title_cl}")]'

genre_cl = 'whitespace-pre-wrap break-all break-words s12-regular-white ml-3 opacity-85'
genre_xp = f'//p[contains(@class, "{genre_cl}")]'

img_xp = f'//meta[@property="og:image"]'

desc_xp = f'//meta[@name="description"]'

key_cl = 'whitespace-pre-wrap break-all break-words overflow-hidden text-ellipsis !whitespace-nowrap s14-medium-white'
key_xp = f'//p[contains(@class, "{key_cl}")]'


wt_url = [] # 각 웹툰의 링크들
title = [] # 각 웹툰의 제목(느낌표 등도 포함되므로, 파일 제목으론 적절하지 않음)
genre = [] # 각 웹툰의 장르
img_url = [] # 각 웹툰의 메인 이미지 url
desc = [] # 각 웹툰의 줄거리
key_word = [] # 각 웹툰의 키워드

# 작은 칸의 웹툰들 (월-일)
main_lcl1 = 'w-full h-full relative' # 웹툰의 클릭 이미지 class
main_lc_xp1 = f'//a[contains(@class, "{main_lcl1}")]' # 웹툰의 클릭 이미지 xpath

"""
ii = 0
for jj in range(len(typ)):
    main_url1 = f'https://webtoon.kakao.com/original-{typ[jj]}?tab={sec1[ii]}'
    # 여기서 sec1의 index는 무조건 0이어야 함

    dr.get(main_url1) # url로 접속

    WebDriverWait(dr, 100).until(EC.presence_of_element_located((By.XPATH, main_lc_xp1))) # 웹툰 클릭 이미지가 뜰 때까지 기다리기

    wt_url_e_raw = dr.find_elements(By.XPATH, main_lc_xp1) # 웹툰 클릭 이미지 tag 찾기
    wt_len_e = len(wt_url_e_raw)
    wt_url_e = [0 for i in range(wt_len_e)]

    for i in range(len(wt_url_e)):
        url_raw = wt_url_e_raw[i].get_attribute('href') # 클릭 이미지에서 웹툰 url 추출
        wt_url_e[i] = unquote_plus(url_raw) # 문자를 한글로 변환
    print(len(wt_url_e))
    print(wt_url_e[0])
    print(wt_url_e[-1])
#        print()
    wt_url += wt_url_e
    
print(len(wt_url))
#        urlretrieve(wt_url_e[i], f'./img/{}.jpg')

"""
# 완결 웹툰 

wt_url2 = []
main_lcl2 = 'h-full relative' # 완결 웹툰의 큰 클릭 이미지 class
main_lc_xp2 = f'//a[contains(@class, "{main_lcl2}")]'  # 완결 웹툰의 큰 클릭 이미지 xpath
# -> 이걸로도 작은 이미지들조차도 크롤링이 되는 듯! 이걸로 스크롤 내려서 시도해보자.
ii = 1
for jj in range(len(typ)):
    main_url1 = f'https://webtoon.kakao.com/original-{typ[jj]}?tab={sec1[ii]}'
    # 여기서 sec1의 index는 무조건 0이어야 함

    dr.get(main_url1) # url로 접속

    prev_height = dr.execute_script("return document.body.scrollHeight")
    body_tag = dr.find_element(By.CSS_SELECTOR,"body")
    # while True:
    #     body_tag.click()
    #     if main_url1 == dr.current_url:
    #         break
    #     else:
    #         dr.execute_script("window.history.go(-1)")
    # time.sleep(0.1)

    while True:
        dr.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
        curr_height = dr.execute_script("return document.body.scrollHeight")

        if curr_height == prev_height:
            break
        else:
            prev_height = dr.execute_script("return document.body.scrollHeight")

    WebDriverWait(dr, 100).until(EC.presence_of_element_located((By.XPATH, main_lc_xp2))) # 웹툰 클릭 이미지가 뜰 때까지 기다리기

    wt_url_e_raw = dr.find_elements(By.XPATH, main_lc_xp2) # 웹툰 클릭 이미지 tag 찾기
    wt_len_e = len(wt_url_e_raw)
    wt_url_e = [0 for i in range(wt_len_e)]

    for i in range(len(wt_url_e)):
        url_raw = wt_url_e_raw[i].get_attribute('href') # 클릭 이미지에서 웹툰 url 추출
        wt_url_e[i] = unquote_plus(url_raw) # 문자를 한글로 변환
    print(len(wt_url_e))
    print(wt_url_e[0])
    print(wt_url_e[-1])
#        print()
    wt_url2 += wt_url_e
print(len(wt_url2))

# 큰 칸의 웹툰들
# ii, jj = 0, 0
# main_url1 = f'https://webtoon.kakao.com/original-{typ[jj]}?tab={sec1[ii]}' # 여긴 무조건 0이어야 함

# dr.get(main_url1)

# lon_cl = 'w-full h-full object-cover object-top'
# lon_xp = f'//video[contains(@class,"{lon_cl}")]'

# img_url_lon = [0 for i in range(7)]

# lon_el = dr.find_element(By.XPATH, lon_xp).click()

# #print(lon_el)
# #print(wt_url_e)
# img_xp = f'//meta[@property="og:image"]'


#dr.get(wt_url_e[0])
#WebDriverWait(dr, 100).until(EC.presence_of_element_located((By.XPATH, title_xp)))
# wt_url[0] = dr.find_elements(By.XPATH, img_xp)[0].

#dr.get_screenshot_as_file('last_screen_headless.png')
#dr.quit()