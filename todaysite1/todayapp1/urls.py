from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from todayapp1.views import mystudentdata


routers = routers.DefaultRouter()
routers.register(r'student',mystudentdata)

urlpatterns = [
    path('',include(routers.urls))
    
]
