from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views


urlpatterns=[
    url(r'^login/$',views.login,{'template_name': 'Login.html'}),
    url(r'^register/$',"transport.views.register_page"),
    url(r'^register/$',"transport.views.logout_page"),
    url(r'^$',"transport.views.home")

]