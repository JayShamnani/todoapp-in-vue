# from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework.authtoken import views

from .views import LoginAPI, LogoutAPI
from .views import checkLogin
from .views import checkUsername
from .views import createuser
from .views import home
from .views import profileLogin
from .views import taskDelete
from .views import taskUpdate
from .views import taskcreate
from .views import tasklist
from .views import getallProfiles
from .views import taskclass
from .views import getProfile

router = routers.DefaultRouter()

urlpatterns = [
    path('home',home.as_view()),
    path('',include(router.urls)),
    path('getallprofile',getallProfiles.as_view()),
    path('getprofile/<str:pk>',getProfile.as_view()),
    path('checkprofile',checkLogin.as_view()),
    path('checkusername',checkUsername.as_view()),
    # path('profilelogin',profileLogin.as_view()),
    path('createuser',createuser.as_view()),
    # path('api-token-auth', views.obtain_auth_token),
    path('api-token-auth', LoginAPI.as_view()),
    path('drf-token-delete',LogoutAPI.as_view()),
    path('taskcreate',taskcreate.as_view()),
    path('tasks/<str:pk>',taskclass.as_view()),
    path('tasklist',tasklist.as_view()),
    path('taskupdate/<str:id>',taskUpdate.as_view()),
    path('taskdelete/<str:id>',taskDelete.as_view()),
]
