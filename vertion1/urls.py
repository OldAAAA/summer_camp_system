from django.urls import path

from vertion1 import views

urlpatterns = [

    #处理用户的注册
    path('register',views.register),

    #处理信息的提交
    path('submit',views.submit),

    #处理用户信息的更改
    path('change_information',views.changeinfo),

    #测试样例
    path('test_post',views.test_post)
]