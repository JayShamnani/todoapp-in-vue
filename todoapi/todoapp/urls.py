# from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from .views import home, taskDelete, taskUpdate, taskcreate, tasklist
from .views import profileclass
from .views import taskclass

router = routers.DefaultRouter()

urlpatterns = [
    path('home',home.as_view()),
    path('',include(router.urls)),
    path('profile', profileclass.as_view()),
    path('taskcreate',taskcreate.as_view()),
    path('tasks/<str:pk>',taskclass.as_view()),
    path('tasklist',tasklist.as_view()),
    path('taskupdate/<str:id>',taskUpdate.as_view()),
    path('taskdelete/<str:id>',taskDelete.as_view()),
]
