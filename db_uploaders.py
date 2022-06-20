import csv
import os
import django
import sys


# 현재 디렉토리 경로 표시
os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

# 프로젝트명.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


from reco.models import AllData
# csv 파일 경로
CSV_PATH = './data_kakao.csv'	

# encoding 설정 필요
with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:	
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        AllData.objects.create(
            id=row['id'],
            url = row['url'],
            title = row['title'],
            genre = row['genre'],
            img = 'img/'+row['img'],
            desc = row['desc'],
            key_word = row['key_word'],  
            desc_noun = row['desc_noun']      
        )

