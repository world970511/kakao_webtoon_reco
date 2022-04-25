import pandas as pd
import os
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fout_name = 'wt_data_0-1292_2'

wt_in = [
    'wt_data_0-1292.csv',
    'wt_data_e1_0-109.csv',
    'wt_data_e2_0-2.csv',
]

data_base = pd.read_csv(f'./csv/{wt_in[0]}',sep=';')
data_e1 = pd.read_csv(f'./csv/{wt_in[1]}',sep=';')
data_e2 = pd.read_csv(f'./csv/{wt_in[2]}',sep=';')

for i in range(len(data_e2)):
    id = data_e2['id'][i]
    data_e1[data_e1['id'] == id] = data_e2.loc[i]
    # print(list(data_e2.loc[i]))
    # print(data_e1[data_e1['id'] == id])

for i in range(len(data_e1)):
    id = data_e1['id'][i]
    data_base[data_base['id'] == id] = data_e1.loc[i]


## description 빠진 웹툰 채워넣기
# print(data_base[data_base['desc'] == '0' ])

durl = data_base[data_base['desc'] == '0' ]['url']
dind = data_base.index[data_base['desc'] == '0']
print(dind)


# chromedriver 설정
co = Options()
co.add_experimental_option('debuggerAddress','127.0.0.1:9222')
dr = webdriver.Chrome(options=co)

desc_xp = f'//meta[@name="description"]'

for i in range(len(durl)):
    print(i)
    try:
        descurl = durl.values[i]
        dr.get(descurl)
        WebDriverWait(dr, 100).until(EC.presence_of_element_located((By.XPATH, desc_xp)))
        time.sleep(3)
        desc = dr.find_elements(By.XPATH, desc_xp)[0].get_attribute('content')
        data_base.at[dind[i] ,'desc'] = desc[i].replace("\n", "\m")

    except Exception:
        print(durl[i])

    time.sleep(1)

print(data_base[data_base['desc'] == '0' ])
data_base = data_base.sort_values(by=['id'],axis=0)
data_base = data_base.reset_index(drop=True)
data_base.to_csv('./csv/wt_data.csv',sep=';',index=False)