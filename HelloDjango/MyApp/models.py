from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=20)
    userPwd = models.CharField(max_length=20)
    userAddress = models.CharField(max_length=50)

    @classmethod
    def createUser(cls,username,userpwd,useraddress):
        user = cls(userName=username,userPwd=userpwd,userAddress=useraddress)
        return user