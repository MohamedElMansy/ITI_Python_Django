from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_custom(models.Model):
    user = models.OneToOneField(User)
    user_img = models.ImageField(default="default.jpeg")