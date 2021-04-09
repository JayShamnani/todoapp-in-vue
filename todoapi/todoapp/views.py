from django.contrib.auth.models import User
from django.core import exceptions


#Rest Framework

from rest_framework.response import Response
from rest_framework.views import APIView

#Rest Framework Token

from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken


# Serializers

from .serializers import profileserilizers
from .serializers import taskserilizers
from .serializers import getprofile

import json
# Models

from .models import task

# Views

class home(APIView):
    permission_classes = (IsAuthenticated,)
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

# Fetching all the profiles only for testing and development!!
class getallProfiles(APIView):
    def get(self,request):
        pro = User.objects.all()
        serializer = profileserilizers(pro, many=True)
        return Response(serializer.data)

# View for getting all the task created by user
class taskclass(APIView):
    def get(self,request,pk):
        users = User.objects.get(username = pk)
        tasks = task.objects.filter(taskauthor = users.id)
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
        profileDetail = User.objects.filter(username = pk)
        serializer = getprofile(profileDetail,many=True)
        return Response(serializer.data)

class checkLogin(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        tokenheader = request.META['HTTP_AUTHORIZATION']
        tok = tokenheader[6:]
        tokenuser = Token.objects.get(key = tok)
        xx = True
        yy = str(tokenuser.user)
        # yy = 'shamnanijay123'
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
                    request.session["profileusername"]=i.username
                    result = {
                        'Results':True,
                        "Profile":i.username,
                        "ProfileID":i.id,
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
class LoginAPI(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        prof = User.objects.filter(username=request.data['username'])
        if len(prof) == 0:
            result = {
                'Results':0,
                "Profile":0,
                "Username":0
            }
        else:
            if serializer.is_valid():
                user = serializer.validated_data['user']
                if user is None:
                    print("no user")
                token, created = Token.objects.get_or_create(user=user)
                result = {
                    'Results':True,
                    'token': token.key,
                    "Profile":user.username,
                    "Username":0
                }
            else:
                result = {
                    'Results':"PasswordError",
                    "Profile":0,
                    "Username":0
                }
        return Response(result)


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

from rest_framework import status
class DrfTokenDelete(APIView):
    def post(self, request):
        data = request.data
        user = User.objects.get(username=data["user"])
        user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)