# Generated by Django 4.0.4 on 2022-04-26 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllData',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.URLField(max_length=500)),
                ('title', models.CharField(max_length=300)),
                ('genre', models.CharField(max_length=200)),
                ('img', models.ImageField(default='media/default_image.jpeg', upload_to='')),
                ('desc', models.TextField(null=True)),
                ('key_word', models.CharField(max_length=300)),
            ],
        ),
    ]
