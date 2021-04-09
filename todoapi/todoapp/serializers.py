from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import task

class profileserilizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class taskserilizers(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'

class getprofile(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']