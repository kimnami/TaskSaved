from django.db import models
from django.forms import ValidationError
from django.conf import settings



class Account(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.IntegerField() #'1'isMan '2'isWoman
    birthday = models.DateField()


    def __str__(self):
        return self.user.last_name+self.user.first_name
