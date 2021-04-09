# from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import Logout, checkLogin, checkUsername, createuser, home, profileLogin, taskDelete, taskUpdate, taskcreate, tasklist
# from .views import addProfile
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
    path('profilelogin',profileLogin.as_view()),
    path('taskcreate',taskcreate.as_view()),
    path('createuser',createuser.as_view()),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout',Logout.as_view()),
    path('tasks/<str:pk>',taskclass.as_view()),
    path('tasklist',tasklist.as_view()),
    path('taskupdate/<str:id>',taskUpdate.as_view()),
    path('taskdelete/<str:id>',taskDelete.as_view()),
]
