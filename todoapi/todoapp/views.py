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
from .serializers import getprofile

# Models

from .models import profile
from .models import task

# Views

# View to check if server is running or not
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

# Fetching all the profiles only for testing and development!!
class getallProfiles(APIView):
    def get(self,request):
        pro = profile.objects.all()
        serializer = profileserilizers(pro, many=True)
        return Response(serializer.data)

# View for getting all the task created by user
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

# sending particular profile
class getProfile(APIView):
    def get(self,request,pk):
        profileDetail = profile.objects.filter(username = pk)
        serializer = getprofile(profileDetail,many=True)
        return Response(serializer.data)

class checkLogin(APIView):
    def get(self,request):
        if request.session.has_key("profileusername"):
            xx = True
            yy = request.session["profileusername"]
        else:
            xx = False
            yy = 0
        result = {
            'Results':xx,
            "Profile":yy
        }
        return Response(result)

class profileLogin(APIView):
    def post(self,request):
        result = {
            "Results":False,
            "Profile":0,
            "Username":0
        }
        prof = profile.objects.filter(username=request.data['username'])
        if len(prof) < 2:
            for i in prof:
                if i.password == request.data['password']:
                    request.session["profileusername"]=i.username
                    result = {
                        'Results':True,
                        "Profile":i.username,
                        "Username":0
                    }
                else:
                    result = {
                        'Results':'PasswordError',
                        "Profile":0,
                        "Username":0
                    }
        else:
            result = {
                'Results':False,
                "Profile":0,
                "Username":0
            }
        return Response(result)

class checkUsername(APIView):
    def post(self,request):
        username = request.data
        pro = profile.objects.filter(username = username)
        if len(pro) < 1:
            Users = {
                "Results":True,
                "Username":1
            }
        else:
            Users = {
                "Results":False,
                "Username":0
            }
        return Response(Users)

class Logout(APIView):
    def get(self,request):
        try:
            request.session.flush()
            request.session.modified = True
        except KeyError:
            pass
        return Response({})