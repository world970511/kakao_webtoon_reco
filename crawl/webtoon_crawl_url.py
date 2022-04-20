#import pandas as pd
#import numpy as np
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import time, csv

from urllib.parse import unquote_plus
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Output File
csv_fpath = './csv/wt_url_raw.csv'

co = Options()
co.add_experimental_option('debuggerAddress','127.0.0.1:9222')
dr = webdriver.Chrome(options=co)

sec1 = ['mon','complete'] # ii
sec2 = ['mon','tue','wed','thu','fri','sat','sun'] # ii
typ = ['webtoon','novel'] # jj

wt_url1 = [] # 각 웹툰의 링크들

# 작은 칸의 웹툰들 (월-일)
main_lcl1 = 'w-full h-full relative' # 웹툰의 클릭 이미지 class
main_lc_xp1 = f'//a[contains(@class, "{main_lcl1}")]' # 웹툰의 클릭 이미지 xpath

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
    wt_url1 += wt_url_e
    
print(len(wt_url1))
#        urlretrieve(wt_url_e[i], f'./img/{}.jpg')


# 완결 웹툰 

wt_url2 = []
main_lcl2 = 'h-full relative' # 완결 웹툰의 큰 클릭 이미지 class
main_lc_xp2 = f'//a[contains(@class, "{main_lcl2}")]'  # 완결 웹툰의 큰 클릭 이미지 xpath

# -> 이걸로도 작은 이미지들조차도 크롤링이 되는 듯! 이걸로 스크롤 내려서 시도해보자.
ii = 1
nn = 20 # 화면을 몇 번 스크롤 다운할 지. 화면 비율 25%로 맞췄을 때 17번 정도면 됐음. 그때그때 조정하기

for jj in range(len(typ)):
    main_url1 = f'https://webtoon.kakao.com/original-{typ[jj]}?tab={sec1[ii]}'
    # 여기서 sec1의 index는 무조건 0이어야 함

    dr.get(main_url1) # url로 접속

    body_tag = dr.find_element(By.CSS_SELECTOR,"body")

    print("검은 화면을 클릭해줘")
    time.sleep(10)
    # 이 이후 직접 클릭
    print("start scrolling")
    if jj == 0:
        for i in range(nn):
            body_tag.send_keys(Keys.PAGE_DOWN)
            time.sleep(3)
    else:
        body_tag.send_keys(Keys.END)
    print("last sleep")
    time.sleep(10)

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

# 월-일 웹툰 중 큰 칸의 웹툰들 (14개 뿐이라 직접 입력)

wt_url3 = [
    'https://webtoon.kakao.com/content/스위치/2683',
    'https://webtoon.kakao.com/content/우리집이거든요/1673',
    'https://webtoon.kakao.com/content/도토리-문화센터/2557',
    'https://webtoon.kakao.com/content/우리-동네-삐-/2681',
    'https://webtoon.kakao.com/content/열무와-알타리/1855',
    'https://webtoon.kakao.com/content/샤크/2308',
    'https://webtoon.kakao.com/content/질투유발자들/2024',
    'https://webtoon.kakao.com/content/이번-생은-가주가-되겠습니다/2473',
    'https://webtoon.kakao.com/content/도굴왕/2340',
    'https://webtoon.kakao.com/content/당신의-이해를-돕기-위하여/2480',
    'https://webtoon.kakao.com/content/마탄의-사수/2470',
    'https://webtoon.kakao.com/content/백작가의-망나니가-되었다/2414',
    'https://webtoon.kakao.com/content/나-홀로-로그인/2366',
    'https://webtoon.kakao.com/content/닳고닳은-뉴비/2446',
]

wt_url = wt_url1 + wt_url2 + wt_url3

# csv 파일로 url들 내보내기
f = open(csv_fpath,'w',newline='')
wr = csv.writer(f)
for i in range(len(wt_url)):
    wr.writerow([i, wt_url[i]])
f.close()
