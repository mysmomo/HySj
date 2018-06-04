from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse

from django.contrib.auth import authenticate, login,logout   #用户
from django.contrib.auth.models import User  
from django.contrib.auth.decorators import login_required  #权限控制
from django import forms   #表单
import random   #随机数
import urllib.request
# 登录验证
def loginValidation(request):
    username = request.GET['username']
    password = request.GET['password']
    user = authenticate(username=username, password=password)
    print(user);
    if user is not None:
        login(request,user)
        return HttpResponse('登录成功')
    else:
        return HttpResponse('账号密码错误')
#发送注册验证码
def RegistrationCode(request):
	if request.method == 'GET':
		username = request.GET['username']
		code = random.randint(1000,9000)   #验证码
		url = 'http://118.24.53.130/SUBMAIL_PHP_SDK/SUBMAIL_PHP_SDK/demo/message_xsend_demo.php?phone=%s&code=%s'%(username,code)
		print(url)
		req = urllib.request.Request(url=url)
		res_data = urllib.request.urlopen(req)
		userinfo = User.objects.filter(username = request.GET['username'])
		if len(userinfo)==0:   #用户不存在时直接新建用户 发送验证码  
			user = User.objects.create_user(
			username=username,
			first_name=code,
			password = 'pbkdf2_sha256$100000$go5krpSu9bOA$m2QgM1q0CuYTG7uPcGnJ6+OOTiQSLfX9VvKNSge7LiY='
			)
			return HttpResponse('用户不存在验证码以发送')
		else:                 #用户存在时直接修改验证码  并发送
			userinfo[0].first_name = code
			userinfo[0].save()	
			return HttpResponse('用户存在验证码以发送')
		   	    
# 注册验证
def RegistrationValidation(request):
	if request.method == 'GET':
		username = request.GET['username']
		code = request.GET['code']
		password1 = request.GET['password1']
		password2 = request.GET['password2']
		userinfo = User.objects.filter(username = request.GET['username'])
		if password2!=password1:     
			return HttpResponse('两次输入密码不一致')
		if userinfo[0].first_name == code:  #判断验证码是否正确
			user = authenticate(username=username, password='pbkdf2_sha256$100000$go5krpSu9bOA$m2QgM1q0CuYTG7uPcGnJ6+OOTiQSLfX9VvKNSge7LiY=')
			if user is not None:
				user.set_password(password1)
				user.save() 
			return HttpResponse('注册成功')
		else:
			return HttpResponse('验证码不正确')
		return HttpResponse(random.randint(1000,9000))
# 注销   
def userLogout(request):  
    auth.logout(request)  
    return HttpResponse('注销成功')

# 重置密码
def ResetPassword():
	username = request.GET['username']
	old_password = request.GET['old_password']	
	user = auth.authenticate(username=username, password=old_password)
	if user is not None:
		user.set_password(new_password)
		user.save()  