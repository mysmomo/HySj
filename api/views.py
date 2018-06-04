from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import *
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
from django.core import serializers
from api.serializers import COSbucketSerializer



def videoindex(request):
	data = COSbucket.objects.all().order_by("-id")
	json_data = COSbucketSerializer(data, many=True)
	return JsonResponse(json_data.data, safe=False)




# Create your views here.
def uploadfile(request):
	vodel =request.FILES.getlist('file')  
	print(vodel);
	for file_video in vodel:
		new_img = IMG(
			vodel =file_video,
			)
		new_img.save()
	COSbucket.objects.create(
	vodel_address = 'https://meizi-1253881240.cos.ap-chengdu.myqcloud.com/%s'%(vodel[1].name),
	image_address = 'https://meizi-1253881240.cos.ap-chengdu.myqcloud.com/%s'%(vodel[0].name ),
	 )

	logging.basicConfig(level=logging.INFO, stream=sys.stdout)
	secret_id = 'AKIDsjf0SkYFLMC9dywOtDYhEHKLgq3Cl1kY'      # 替换为用户的 secretId
	secret_key = 'qZ8asumZYYUGrFi5HIC5zkKnCWgbr383'      # 替换为用户的 secretKey
	region = 'ap-chengdu'     # 替换为用户的 Region
	token = ''                  # 使用临时秘钥需要传入 Token，默认为空，可不填
	config = CosConfig(Secret_id=secret_id, Secret_key=secret_key, Region=region, Token=token)
	# 2. 获取客户端对象
	client = CosS3Client(config)
	for up_cso in vodel:
		file_name =up_cso.name
		file_address ='./media/media/%s'%(file_name)
		with open(file_address, 'rb') as fp:
		    response = client.put_object(
		        Bucket='meizi-1253881240',
		        Body=fp,
		        Key=file_name,
		        StorageClass='STANDARD',
		        ContentType='text/html; charset=utf-8'
		    )
		print(response['ETag'])
	return HttpResponse('z')