import pandas as pd
#import numpy as np
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import time, os

from urllib.parse import unquote_plus
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Input URL csv file
csv_fpath = './csv/wt_url.csv'

csv_file = pd.read_csv(csv_fpath)
wt_url = csv_file['url'].values.tolist()
wt_id = csv_file['id'].values.tolist()
wtl = len(wt_url)

# 이미지 저장 폴더
img_folder = './img'

# chromedriver 설정
co = Options()
co.add_experimental_option('debuggerAddress','127.0.0.1:9222')
dr = webdriver.Chrome(options=co)

# 가져올 자료들의 속성과 xpath들
title_cl = 'whitespace-pre-wrap break-all break-words overflow-hidden text-ellipsis !whitespace-nowrap s22-semibold-white leading-33 mb-1'
title_xp = f'//p[contains(@class, "{title_cl}")]'

genre_cl = 'whitespace-pre-wrap break-all break-words s12-regular-white ml-3 opacity-85'
genre_xp = f'//p[contains(@class, "{genre_cl}")]'

img_xp = f'//meta[@property="og:image"]'

desc_xp = f'//meta[@name="description"]'

key_cl = 'whitespace-pre-wrap break-all break-words overflow-hidden text-ellipsis !whitespace-nowrap s14-medium-white'
key_xp = f'//p[contains(@class, "{key_cl}")]'

# 자료들을 넣을 리스트 생성
title = [0 for i in range(wtl)]
genre = [0 for i in range(wtl)]
img_url = [0 for i in range(wtl)]
desc = [0 for i in range(wtl)]
desc1 = [0 for i in range(wtl)]
key_word = [0 for i in range(wtl)]

# 에러 발생하는 url 수집
error_url = []

sind = 1248
#ii = 0
for ii in range(wtl):
#for ii in range(165,wtl):
#for ii in range(230,wtl):
#for ii in range(383,wtl):
#for ii in range(407,wtl):
#for ii in range(422,wtl):
#for ii in range(460,wtl):
#for ii in range(812,wtl):
#for ii in range(1248,wtl):
    print(ii)
    try:
        dr.get(wt_url[ii])
        WebDriverWait(dr, 100).until(EC.presence_of_element_located((By.XPATH, title_xp)))
        time.sleep(3)

        title[ii] = dr.find_elements(By.XPATH, title_xp)[0].text
        genre[ii] = dr.find_elements(By.XPATH, genre_xp)[0].text
        img_url[ii] = dr.find_elements(By.XPATH, img_xp)[0].get_attribute('content')
        desc[ii] = dr.find_elements(By.XPATH, desc_xp)[0].get_attribute('content')

        click_cl = 'whitespace-pre-wrap break-all break-words overflow-hidden text-ellipsis !whitespace-nowrap s12-regular-white -mt-3 opacity-85 leading-21 h-21'

        click_xp = f'//p[contains(@class, "{click_cl}")]'
        click_el = dr.find_element(By.XPATH, click_xp)
        click_el.click()

    except Exception as error:
        print(error)
        error_url.append(wt_url[ii])
        print(error_url)

    time.sleep(3)
    key_cl = 'whitespace-pre-wrap break-all break-words overflow-hidden text-ellipsis !whitespace-nowrap s14-medium-white'
    key_xp = f'//p[contains(@class, "{key_cl}")]'
    key_el = dr.find_elements(By.XPATH,key_xp)
    kw = [0 for j in range(len(key_el))]

    for j in range(len(key_el)):
        kw[j] = key_el[j].text
    print(kw)
    key_word[ii] = kw
    time.sleep(3)

find = ii
for i in range(sind, find):
    desc1[i] = desc[i].replace("\n", "\m")
csv_file['title'] = title
csv_file['genre'] = genre
csv_file['img_url'] = img_url
csv_file['desc'] = desc1
csv_file['key_word'] = key_word
ncsv = csv_file.loc[sind:find,:]
ncsv.to_csv(f'./csv/wt_data_{sind}-{find}.csv', sep=';',index=False)

error_df = pd.DataFrame(error_url)
error_df.to_csv(f'./csv/error_url_{sind}-{find}.csv', index=False)


# for i in range(sind,find):
#     try:
#         desc1[i] = desc[i].replace("\n","\m")
#     except AttributeError:
#         pass