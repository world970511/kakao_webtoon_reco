from urllib.request import urlretrieve
import pandas as pd
import os, time

csv_fpath = './csv/wt_data.csv'

wt_data = pd.read_csv(csv_fpath, sep=';')

wt_id = wt_data['id'].values
wt_iurl = wt_data['img_url'].values

wlen = len(wt_id)

img_folder = './img'

if not os.path.isdir(img_folder):
    os.mkdir(img_folder)

for i in range(wlen):
    urlretrieve(wt_iurl[i], f'./img/{wt_id[i]}.jpg')
    time.sleep(1)