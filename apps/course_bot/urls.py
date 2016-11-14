from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add, name='add'),
    # url(r'^usercourse$', views.usercourse, name='usercourse'),
    url(r'^confirm/(?P<id>\d+)$', views.confirm, name ='confirm'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name ='destroy')
]
