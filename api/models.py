from django.db import models

# Create your models here.
class IMG(models.Model):  #视频图片上传
    vodel = models.FileField(upload_to='media')


class COSbucket(models.Model):   #腾讯云存储图片和视频地址
    vodel_address = models.CharField(max_length=200, default='')
    image_address = models.CharField(max_length=200, default='')
