# Generated by Django 2.0.5 on 2018-05-24 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180524_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='sign',
            field=models.IntegerField(default=-1),
        ),
    ]
