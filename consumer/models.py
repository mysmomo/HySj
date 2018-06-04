from django.db import models

# Create your models here.
class UserInfo(models.Model):  #视频图片上传
						#关联用户id
    header_url = models.CharField(max_length=200, default='')   #头像地址
    nickname = models.CharField(max_length=200, default='')		#昵称