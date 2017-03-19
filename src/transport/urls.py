from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views


urlpatterns=[
    url(r'^login/$',views.login,{'template_name': 'login.html'}),
    url(r'^register/$',"transport.views.register_page",name='register'),
    url(r'^logout/$',"transport.views.logout_page",name='logout'),
    url(r'^$',"transport.views.home",name='home')

]