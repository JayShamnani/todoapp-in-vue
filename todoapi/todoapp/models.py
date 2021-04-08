from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class task(models.Model):
    taskid = models.AutoField(primary_key=True,unique=True)
    taskauthor = models.ForeignKey(User,on_delete=CASCADE,related_name='Author')
    taskhead = models.TextField()
    taskbody = models.TextField()
    taskreminder = models.BooleanField(default=False)

    def __str__(self):
        return str(self.taskid)