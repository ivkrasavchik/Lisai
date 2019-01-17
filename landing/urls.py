# coding=utf-8
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'company/$', views.company, name="company"),

    path('prod_serv/<c_id>/', views.prod_serv, name="prod_serv"),
    # url(r'prod_serv/(?P<c_id>\w+)/$', views.prod_serv, name="prod_serv"),
    path('condserv/<serv_id>/', views.condserv, name="condserv"),
    path('production/<cat_id>/', views.production, name="production"),
    path('product/<prod_id>/', views.product, name="product"),
    path('production_brand/<brand_id>/', views.production_brand, name="production_brand"),
    path('brands', views.brands, name="brands"),
    path('brand/<brand_id>/', views.brand, name="brand"),
    path('call', views.call, name="call"),
    path('question', views.question, name="question"),
    # path('single/<int:pk>', views.new_single, name="new_single"),
    # path('filter/<int:pk>', views.news_filter, name="news_filter"),
]
