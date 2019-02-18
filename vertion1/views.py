import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, "test.html",{"test_info":"登录界面","result":"返回成功"})
    if request.method == 'POST':
        information  = {"result":"true","information":"注册成功"}
        return HttpResponse(json.dumps(information),content_type='application/json', charset='utf-8')





'''
登录

1、request.method == GET
        返回的是登录的页面
2、request.method  == POST
        request.form = ["username":"123","password":"123456"]
        首先你要检查这个东西在数据库里面有没有这个用户，
        然后密码有没有正确，如果不存在用户，information：用户名不存在,如果用户的密码输错了：第二种情况
        返回的是登录的结果["result":"true","information":"用户名不存在/用户名或者密码错误"]
'''


'''
注册
1、request.method == GET
        返回的是注册的页面
        return render
2、request.method  == POST
        request.form = ["username":"123","password":"123456"]
        首先检查存不存在这个用户，数据库里面找user，看有没有，如果没有：info：注册成功，如果有：info:用户名已经存在
        返回的是注册的结果{"result":"true","infomation":""}
        renturn HttpResponse()
'''