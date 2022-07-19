from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Names(models.Model):
    title = models.CharField(max_length = 255)
    level = models.CharField(max_length=255)
    description = models.TextField()
    user = models.OneToOneField(User,on_delete= models.CASCADE)

    def __str__(self):
        return self.title





class Spares(models.Model):
    username = models.CharField(max_length=255)
    mode = models.CharField(max_length=255)
    states = models.CharField(max_length=255)
    parts = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add = True)
    score = models.IntegerField()

    def __str__(self):
        return self.username