from django.conf.urls import url
from django.contrib import admin

from .views import user

urlpatterns=[
    url(r'^$',"transport.views.transport_home")
]