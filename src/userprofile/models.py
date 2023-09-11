from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.IntegerField(null = True, blank = True)
    phone_number = models.CharField(max_length=10, null = True, blank = True)
    address = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.user.username
    