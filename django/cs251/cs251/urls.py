from django.conf.urls import patterns, include, url
from django.contrib import admin
from rankallocapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cs251.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   
    url(r'^home/',  views.main),
     url(r'^register/',  views.register),
)
