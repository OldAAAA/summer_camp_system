import json
from copy import copy

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from vertion1 import models

from django.contrib.auth import get_user_model, logout
from django.contrib.auth import authenticate
from django.contrib import auth
import smtplib
from email.mime.text import MIMEText

User = get_user_model()

def login(request):
    if request.method == "POST":
        # 前端 变量名称为email_username
        email_username = request.POST['email']
        if(not '@' in email_username):
            information = {"information":"User name is incorrectly formatted"}
            return render(request, "login.html", information)
        # 前端 变量名称为pw
        password = request.POST['password']

        hasUser =  User.objects.filter(email=email_username)
        if len(password) < 6:
            information = {"information": "Password is not less than six digits"}
            return render(request, "login.html", information)
        if hasUser:
            user = auth.authenticate(email=email_username, password=password)
            if user is not None:
                auth.login(request, user)
                if request.user.is_admin:
                    return redirect("/audit")
                else:
                    return redirect("/submit")
            else:
                information = {"information":"Wrong user name or password"}
                return render(request,"login.html",information)
        else:
            information = {"information":"User name does not exist"}
            return render(request, "login.html", information)
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        # 前端 变量名称为email_username
        email = request.POST['email']

        # 前端 变量名称为password
        password = request.POST['password']

        password_confirm = request.POST['password_confirm']

        hasUser = User.objects.filter(email=email)
        if not hasUser:  # User Exists
            if (not '@' in email):
                information = {"information": "There is an error in the user name format"}
                return render(request,"register.html",information)
            if password != password_confirm:
                information = {"information": "Password inconsistency"}
                return render(request,"register.html",information)
            if len(password) < 6:
                information = {"information": "Password is not less than six digits"}
                return render(request,"register.html",information)
            # insert into database
            else:
                information = {"information": "Registered successfully"}
                User.objects.create_user(email=email, password=password)
                return redirect("/login")
        else:
            information = {"information":"Username is already registered"}
            return render(request,"register.html",information)
    else:
       return render(request, 'register.html')

def submit(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "submit.html",{"email":request.user.email})
        if request.method == "POST":
            #返回的信息
            information = {"result": "true", "information": "注册成功"}
            #拿到提交的表单
            form  = copy(request.POST)
            print(form)

            # #判断是否所有的信息都填写了
            # for element in form:
            #     if form[element] == "":
            #         information["result"]  = "False"
            #         information["information"] = "填写必填信息"
            #         return HttpResponse(json.dumps(information), content_type='application/json', charset='utf-8')
            #

            form["email"] = request.user.email
            form["submit_status"] = "Pending approval"
            form["sex"] = "f"
            s =models.User_info.objects.create(**form)
            s.save()
            return HttpResponse(json.dumps(information), content_type='application/json', charset='utf-8')
    else:
        return redirect("/login")

def changeinfo(request):
    # 返回的信息
    information = {"result": "true", "information": "注册成功"}

    # 拿到提交的表单
    form = request.POST

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

def audit(request):
    if request.user.is_authenticated and request.user.is_admin:
        if request.method == "GET":
            return render(request, "audit.html")
    else:
        return redirect("/login")

def lookup(request):
    if request.user.is_authenticated and request.user.is_admin:
        if request.method == "GET":
            return render(request,"lookup.html")
    else:
        return redirect("/login")

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/login")
    else:
        return redirect("/login")

def forgot(request):
    if request.method == "GET":
        return render(request,"forgot.html")
    if request.method == "POST":
        email=request.POST["email"]

        user = User.objects.get(email = email)
        # 发送纯文本格式的邮件
        text = "You password is:"+user.password
        msg = MIMEText(text,'plain','utf-8')
        #发送邮箱地址
        sender = '13031170798@163.com'
        #邮箱授权码，非登陆密码
        password = 'zxc89473324'
        #收件箱地址
        receiver = email
        #smtp服务器
        smtp_server = 'smtp.163.com'
        #发送邮箱地址
        msg['From'] = sender
        #收件箱地址
        msg['To'] = receiver
        #主题
        msg['Subject'] = 'from IMYalost'
        server = smtplib.SMTP(smtp_server,25)
        server.login(sender,password)
        server.sendmail(sender,receiver,msg.as_string())
        server.quit()
        return render(request,"login.html")