from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from django.http import request

#Rest Framework

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework import serializers
from rest_framework.views import APIView


# Serializers

from .serializers import profileserilizers
from .serializers import taskserilizers

# Models

from .models import profile
from .models import task

# Views

class home(View):
    template_name = 'home.html'
    def get(self,request):
        return render(request, self.template_name)

class addProfile(APIView):
    def post(self,request):
        userprofile = request.data
        serializer = profileserilizers(data=userprofile)
        if serializer.is_valid():
            serializer.save()
            request.session["profile_username"] = userprofile["username"]

        return Response(serializer.data)

class getallProfiles(APIView):
    def get(self,request):
        pro = profile.objects.all()
        serializer = profileserilizers(pro, many=True)
        return Response(serializer.data)

class taskclass(APIView):
    def get(self,request,pk):
        tasks = task.objects.filter(taskauthor = pk)
        serializer = taskserilizers(tasks, many=True)
        return Response(serializer.data)

class taskcreate(APIView):
    def post(self,request):
        taskdata = request.data
        serializer = taskserilizers(data=taskdata)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

class tasklist(APIView):
    def get(self,request):
        tasks = task.objects.all()
        serializer = taskserilizers(tasks, many=True)
        return Response(serializer.data)


class taskUpdate(APIView):
    def post(self,request,id):
        taskdetail = task.objects.get(taskid= id)
        serializer = taskserilizers(instance=taskdetail,data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

class taskDelete(APIView):
    def delete(self,request,id):
        taskdelete = task.objects.get(taskid=id)
        taskdelete.delete()
        return Response({})

class getProfile(APIView):
    def get(self,request,pk):
        profileDetail = profile.objects.filter(id = pk)
        serializer = profileserilizers(profileDetail,many=True)
        return Response(serializer.data)

class checkLogin(APIView):
    def get(self,request):
        if request.session.has_key("profile_username"):
            requestprofile = request.session["profile_username"]
            print(requestprofile)
            xx = True
        else:
            xx = False
        result = {
            'Results':xx
        }
        print(result)
        return Response(result)