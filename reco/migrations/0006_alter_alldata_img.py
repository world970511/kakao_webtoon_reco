# Generated by Django 4.0.4 on 2022-06-20 08:27

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reco', '0005_alldata_desc_noun'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alldata',
            name='img',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]