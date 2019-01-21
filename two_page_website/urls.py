# coding=utf-8
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="t_home"),
    # url(r'company/$', views.company, name="company"),
    # path('call', views.call, name="call"),
    # path('question', views.question, name="question"),
    path('cond', views.cond, name="cond"),
    path('vent', views.vent, name="vent"),
]
