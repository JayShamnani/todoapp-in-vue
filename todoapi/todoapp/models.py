from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class profile(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=500)
    password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.username)

class task(models.Model):
    taskid = models.AutoField(primary_key=True,unique=True)
    taskauthor = models.ForeignKey(profile,on_delete=CASCADE)
    taskhead = models.TextField()
    taskbody = models.TextField()
    taskreminder = models.BooleanField(default=False)

    def __str__(self):
        return str(self.taskid)