# Generated by Django 3.1.7 on 2021-03-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20210319_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='photo',
            field=models.ImageField(default='None', upload_to='upload/'),
        ),
    ]
