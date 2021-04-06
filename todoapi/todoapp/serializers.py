from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import profile
from .models import task

class profileserilizers(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = '__all__'

class taskserilizers(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'

class getprofile(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = ['username','name']