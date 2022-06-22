from django.db import models
from cloudinary.models import CloudinaryField

# 이 파일은 데이터베이스의 제약 조건을 명시하는 파일입니다.
class AllData(models.Model):
    id=models.IntegerField(primary_key=True)
    url=models.URLField(max_length=500)
    title=models.CharField(max_length=300)
    genre=models.CharField(max_length=200)
    img=CloudinaryField('image')
    desc=models.TextField(null=True)
    key_word=models.CharField(max_length=300)
    desc_noun=models.CharField(max_length=500,blank=True)



