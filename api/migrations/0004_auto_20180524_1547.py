# Generated by Django 2.0.5 on 2018-05-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_img_sign'),
    ]

    operations = [
        migrations.CreateModel(
            name='COSbucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign', models.IntegerField(default=-1)),
                ('vodel_address', models.CharField(default='', max_length=200)),
                ('image_address', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='img',
            name='image_address',
        ),
        migrations.RemoveField(
            model_name='img',
            name='vodel_address',
        ),
    ]
