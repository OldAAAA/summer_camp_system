import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from vertion1 import models

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




'''
前端返回的json数据
{
    "email":"1@qq.com"
    "First_Name":"Long"
    "Last_Name" :"Qiwei"
    "Chinese_Name" : "龙淇伟"
    "Sex" : "f"
    "Nationality" : "China"
    "Date_Of_Birth" : "1998.8.15"
    "Place_of_Birth" : "jiangxi jian"
    "Mather_Tongue" : "Chinese"
    "Religion" : "无"
    "Health_Condition" : "Good"
    "Name_Of_Institution" : "Beijing JiaoTong University"
    "Highest_Education" : "phd"
    "Email" : "1@qq.com"
    "Phone_Number" : "18801119875"
    "Emergency_Name" : "lalaal"
    "Emergency_Relationship" : "lala"
    "Emergency_Phone" : "ads"
    "Emergency_email" : "adsd"
    "Name_Of_Sponsor" : "guojiajijingwei"
    "Sponsor_Relationship" : "sidjisd"
    "Sponsor_Phone" : "sdfsf"
    "Sponsor_Email" : "23r"
    "Mail_Recipient" : "12323"
    "Mail_Phone" : "123213"
    "Mail_Address" : "1234324"
    "Mail_City" : "12323132"
    "Mail_Country" : "fdsfds"
    "Mail_Postcode" :"123123"
}
'''

def submit(request):
    if request.method == "GET":
        return render(request, "test.html", {"test_info": "提交详细信息界面", "result": "返回成功"})
    if request.method == "POST":
        #返回的信息
        information = {"result": "true", "information": "注册成功"}
        #拿到提交的表单
        form  = request.POST
        # form = {
        #         "First_Name":"Long",
        #         "Last_Name" :"Qiwei",
        #         "Chinese_Name" : "龙淇伟",
        #         "Sex" : "f",
        #         "Nationality" : "China",
        #         "Date_Of_Birth" : "1998.8.15",
        #         "Place_of_Birth" : "jiangxi jian",
        #         "Mather_Tongue" : "Chinese",
        #         "Religion" : "无",
        #         "Health_Condition" : "Good",
        #         "Name_Of_Institution" : "Beijing JiaoTong University",
        #         "Highest_Education" : "phd",
        #         "Email" : "1@qq.com",
        #         "Phone_Number" : "18801119875",
        #         "Emergency_Name" : "lalaal",
        #         "Emergency_Relationship" : "lala",
        #         "Emergency_Phone" : "ads",
        #         "Emergency_email" : "adsd",
        #         "Name_Of_Sponsor" : "guojiajijingwei",
        #         "Sponsor_Relationship" : "sidjisd",
        #         "Sponsor_Phone" : "sdfsf",
        #         "Sponsor_Email" : "23r",
        #         "Mail_Recipient" : "12323",
        #         "Mail_Phone" : "123213",
        #         "Mail_Address" : "1234324",
        #         "Mail_City" : "12323132",
        #         "Mail_Country" : "fdsfds",
        #         "Mail_Postcode" :"123123",
        #         }

        #判断是否所有的信息都填写了
        for element in form:
            if form[element] == "":
                information["result"]  = "False"
                information["information"] = "填写必填信息"
                return HttpResponse(json.dumps(information), content_type='application/json', charset='utf-8')


        user =models.User.objects.get(email = "1@qq.com")
        form["email"] = user
        form["submit_status"] = "Pending approval"
        s =models.User_info.objects.create(**form)
        s.save()
        return HttpResponse(json.dumps(information), content_type='application/json', charset='utf-8')


def changeinfo(request):
    # 返回的信息
    information = {"result": "true", "information": "注册成功"}
    # 拿到提交的表单
    form = request.POST
    # form = {
    #         "First_Name":"Long",
    #         "Last_Name" :"Qiwei",
    #         "Chinese_Name" : "龙淇伟",
    #         "Sex" : "f",
    #         "Nationality" : "China",
    #         "Date_Of_Birth" : "1998.8.15",
    #         "Place_of_Birth" : "jiangxi jian",
    #         "Mather_Tongue" : "Chinese",
    #         "Religion" : "无",
    #         "Health_Condition" : "Good",
    #         "Name_Of_Institution" : "Beijing JiaoTong University",
    #         "Highest_Education" : "phd",
    #         "Email" : "1@qq.com",
    #         "Phone_Number" : "18801119875",
    #         "Emergency_Name" : "lalaal",
    #         "Emergency_Relationship" : "lala",
    #         "Emergency_Phone" : "ads",
    #         "Emergency_email" : "adsd",
    #         "Name_Of_Sponsor" : "guojiajijingwei",
    #         "Sponsor_Relationship" : "sidjisd",
    #         "Sponsor_Phone" : "sdfsf",
    #         "Sponsor_Email" : "23r",
    #         "Mail_Recipient" : "12323",
    #         "Mail_Phone" : "123213",
    #         "Mail_Address" : "1234324",
    #         "Mail_City" : "12323132",
    #         "Mail_Country" : "fdsfds",
    #         "Mail_Postcode" :"123123",
    #         }

    #获取当前的登录用户
    user = models.User.objects.get(email="1@qq.com")

    models.User_info.objects.get(email = user.email)
    models.User_info.delete()

    form["email"] = user
    form["submit_status"] = "Pending approval"
    s = models.User_info.objects.create(**form)
    s.save()

    return HttpResponse("这是更改页面")

def test_post(request):
    if request.method == "GET":
        return render(request,"test_post.html")
    else:
        form = request.POST
        print(request.POST)
        info = {}
        info["result"] = form["email"]
        return JsonResponse(info)
