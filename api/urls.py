
from django.contrib import admin
from django.urls import path
from api.views import GetMyInfo

urlpatterns = [
    path("get-my-info/", GetMyInfo.as_view(), name='get')

]
