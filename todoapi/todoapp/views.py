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

class profileclass(APIView):
    def get(self,request):
        pro = profile.objects.all()
        serializer = profileserilizers(pro, many=True)
        return Response(serializer.data)

    def post(self,request):
        userprofile = request.data
        serializer = profileserilizers(data=userprofile)
        if serializer.is_valid():
            serializer.save()

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