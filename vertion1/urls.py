from django.urls import path

from vertion1 import views

urlpatterns = [
    #处理用户的登录
    path('login',views.login),

    #处理用户的注册
    path('register',views.register),

    #处理信息的提交
    path('submit',views.submit),

    #处理用户信息的更改
    path('change_information',views.changeinfo),

    #处理管理员的审核
    path('audit', views.audit),

    #处理管理员的查看
    path('lookup',views.lookup),

    #测试样例
    path('test_post',views.test_post),

    #处理退出系统
    path('logout',views.log_out),

    #处理忘记密码
    path('forgot',views.forgot)
]