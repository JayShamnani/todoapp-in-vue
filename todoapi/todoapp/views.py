from django.contrib.auth.models import User


#Rest Framework

from rest_framework.response import Response
from rest_framework.views import APIView



# Serializers

from .serializers import profileserilizers
from .serializers import taskserilizers
from .serializers import getprofile

import json
# Models

from .models import task

# Views

class home(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self,request):
        content = {'message': 'Hello, World!'}
        return Response(content)

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
        pro = User.objects.all()
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
        profileDetail = User.objects.filter(username = pk)
        serializer = getprofile(profileDetail,many=True)
        return Response(serializer.data)

class checkLogin(APIView):
    def get(self,request):
        if request.session.has_key("profile_username"):
            xx = True
            yy = request.session["profile_username"]
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
        prof = User.objects.filter(username=request.data['username'])
        if len(prof) < 2:
            for i in prof:
                if i.password == request.data['password']:
                    request.session["profile_username"]=i.username
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
        pro = User.objects.filter(username = username)
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
class createuser(APIView):
    def post(self,request):
        userprofile = request.data
        try:
            user = User.objects.create_user(userprofile['username'],userprofile['email'],userprofile['password'])
            user.save()
            result = {
                "Results" : True,
                "Profile" : userprofile['username'],
                "Username" : 0
            }
        except:
            result = {
                "Results" : False,
                "Profile" : 0,
                "Username" : 0
            }
        return Response(result)