# Generated by Django 4.0.4 on 2022-05-18 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reco', '0002_alter_alldata_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alldata',
            name='img',
            field=models.ImageField(blank=True, default='webtoon_img/default_image.jpeg', null=True, upload_to='webtoon_img/'),
        ),
    ]