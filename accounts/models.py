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


class Score(models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    mode = models.CharField(max_length = 255)
    training_score = models.IntegerField()
    marks = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user
