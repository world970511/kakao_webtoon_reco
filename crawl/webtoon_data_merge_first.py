import pandas as pd
import os, chardet

fout_name = 'wt_data_0-1292.csv'
ferror_name = 'error_url_0-1292.csv'

csv_list = os.listdir('./csv')
#print(csv_list)

wt_list = []
error_list = []

for i in range(len(csv_list)):
    if csv_list[i].split('_')[0] == 'wt' and csv_list[i].split('_')[1] == 'data':
        wt_list.append(csv_list[i])
    elif csv_list[i].split('_')[0] == 'error':
        error_list.append(csv_list[i])

#print(wt_list)
#print(error_list)

df_wt_data = pd.DataFrame()
df_error_url = pd.DataFrame()

for i in range(len(wt_list)):
    csv_path = f'./csv/{wt_list[i]}'
    # encoding 확인용 코드
    # print(csv_path)
    # rawdata = open(csv_path,'rb').read()
    # result = chardet.detect(rawdata)
    # charenc = result['encoding']
    # print(charenc) 
    df = pd.read_csv(csv_path,sep=';',encoding='UTF8')
    df_wt_data = pd.concat([df_wt_data, df])

for i in range(len(error_list)):
    csv_path = f'./csv/{error_list[i]}'
    df = pd.read_csv(csv_path,sep=';',encoding='UTF8')
    df_error_url = pd.concat([df_error_url, df])

df_wt_data = df_wt_data.reset_index(drop=True)
df_error_url = df_error_url.reset_index(drop=True)

error_id = [0 for i in range(len(df_error_url))]


for i in range(len(df_error_url)):
    error_id[i] = df_error_url['0'].values[i].split('/')[5]

df_error_url[1] = error_id
df_error_url = df_error_url[[1,'0']]
df_error_url = df_error_url.rename(columns={1:'id','0':'url'})
df_error_url = df_error_url.sort_values(by=['id'],axis=0)
df_error_url = df_error_url.reset_index(drop=True)

print(df_error_url)

df_wt_data.to_csv(f'./csv/{fout_name}',sep=';',index=False)
df_error_url.to_csv(f'./csv/{ferror_name}',sep=';',index=False)