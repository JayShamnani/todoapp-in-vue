# from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from .views import checkLogin, checkUsername, home, profileLogin, taskDelete, taskUpdate, taskcreate, tasklist
from .views import addProfile
from .views import getallProfiles
from .views import taskclass
from .views import getProfile

router = routers.DefaultRouter()

urlpatterns = [
    path('home',home.as_view()),
    path('',include(router.urls)),
    path('addprofile', addProfile.as_view()),
    path('getallprofile',getallProfiles.as_view()),
    path('getprofile/<int:pk>',getProfile.as_view()),
    path('checkprofile',checkLogin.as_view()),
    path('checkusername',checkUsername.as_view()),
    path('profilelogin',profileLogin.as_view()),
    path('taskcreate',taskcreate.as_view()),
    path('tasks/<str:pk>',taskclass.as_view()),
    path('tasklist',tasklist.as_view()),
    path('taskupdate/<str:id>',taskUpdate.as_view()),
    path('taskdelete/<str:id>',taskDelete.as_view()),
]
