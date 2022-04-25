import pandas as pd

csv_fpath = './csv/wt_url_raw.csv'
csv_outpath = './csv/wt_url.csv'
csv_file = pd.read_csv(csv_fpath,encoding='CP949', header=None)

wt_url = csv_file[1]
wt_id = [0 for i in range(len(wt_url))]
for i in range(len(wt_url)):
    wt_id[i] = int(wt_url[i].split('/')[5])

csv_file[2] = wt_id
ncsv = csv_file.sort_values(by=[2],axis=0)
ncsv = ncsv.drop_duplicates([2])
ncsv = ncsv.drop([0],axis=1)
ncsv = ncsv.reset_index(drop=True)
ncsv = ncsv[[2,1]]
ncsv = ncsv.rename(columns={2:'id',1:'url'})

ncsv.to_csv(csv_outpath,index=False)