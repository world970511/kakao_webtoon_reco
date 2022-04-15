#import pandas as pd
#import numpy as np
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import time, os, requests

from urllib.parse import unquote_plus
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

main_url1 = 'https://webtoon.kakao.com/original-webtoon?tab=mon'
main_url2 = 'https://webtoon.kakao.com/original-novel?tab=mon'

dr.get(main_url1)

main_lcl = 'w-full h-full relative'
main_lc_xp = f'//a[contains(@class, "{main_lcl}")]'

WebDriverWait(dr, 100).until(EC.presence_of_element_located((By.XPATH, main_lc_xp)))

wt_url_raw = dr.find_elements(By.XPATH, main_lc_xp)
wt_len = len(wt_url_raw)
wt_url = [0 for i in range(wt_len)]
title = [0 for i in range(wt_len)]
genre = [0 for i in range(wt_len)]
img_url = [0 for i in range(wt_len)]
desc = [0 for i in range(wt_len)]
key_word = [0 for i in range(wt_len)]

for i in range(len(wt_url)):
    url_raw = wt_url_raw[i].get_attribute('href')
    wt_url[i] = unquote_plus(url_raw)

#print(wt_url)
title_cl = 'whitespace-pre-wrap break-all break-words overflow-hidden text-ellipsis !whitespace-nowrap s22-semibold-white leading-33 mb-1'
title_xp = f'//p[contains(@class, "{title_cl}")]'

genre_cl = 'whitespace-pre-wrap break-all break-words s12-regular-white ml-3 opacity-85'
genre_xp = f'//p[contains(@class, "{genre_cl}")]'

img_xp = f'//meta[@property="og:image"]'

desc_xp = f'//meta[@name="description"]'

key_cl = 'whitespace-pre-wrap break-all break-words overflow-hidden text-ellipsis !whitespace-nowrap s14-medium-white'
key_xp = f'//p[contains(@class, "{key_cl}")]'

dr.get(wt_url[0])
WebDriverWait(dr, 100).until(EC.presence_of_element_located((By.XPATH, title_xp)))
title[0] = dr.find_elements(By.XPATH, title_xp)[0].text
genre[0] = dr.find_elements(By.XPATH, genre_xp)[0].text
img_url[0] = dr.find_elements(By.XPATH, img_xp)[0].get_attribute('content')
desc[0] = dr.find_elements(By.XPATH, desc_xp)[0].get_attribute('content')
print(1)
#WebDriverWait(dr, 100).until(EC.presence_of_element_located((By.XPATH, key_xp)))
#print(dr.find_elements(By.XPATH, key_xp))

# urlretrieve(link, f'./img/{}.jpg')


#dr.get_screenshot_as_file('last_screen_headless.png')
#dr.quit()