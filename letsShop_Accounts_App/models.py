from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    auth_token  = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_on  = models.DateTimeField(auto_now_add=True)

class Address(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Address')
    company     = models.CharField(max_length=30)
    country     = models.CharField(max_length=20)
    city        = models.CharField(max_length=20)
    phone       = models.TextField(max_length=15)

    def __str__(self):
        return str(self.user.username)