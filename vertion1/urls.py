from django.urls import path

from vertion1 import views

urlpatterns = [
    path('register',views.register)
]