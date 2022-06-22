import csv
import os
import django
import sys
import cloudinary 
import cloudinary.uploader 
import cloudinary.api
from decouple import config


# 현재 디렉토리 경로 표시
os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

# 프로젝트명.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

cloudinary.config( 
    cloud_name = 'naeun', 
    api_key = '575825474987513', 
    api_secret = config('api_secret')
)


from reco.models import AllData
# csv 파일 경로
CSV_PATH = './data_kakao.csv'	

# encoding 설정 필요
with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:	
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        ImgUrl='./media/img/'+row['img']
        #cloudinary.uploader.upload(ImgUrl,public_id='kakao/'+row['img'].split('.jpg')[0])
        AllData.objects.create(
            id=row['id'],
            url = row['url'],
            title = row['title'],
            genre = row['genre'],
            img ='v1655882873/kakao/'+row['img'].split('.jpg')[0],
            desc = row['desc'],
            key_word = row['key_word'],  
            desc_noun = row['desc_noun']      
        )

