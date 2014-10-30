from django.conf.urls import patterns, include, url
from django.contrib import admin
from rankallocapp import views

urlpatterns = patterns('', 
    url(r'^home/',  views.main),
    url(r'^register/',  views.register),
)
