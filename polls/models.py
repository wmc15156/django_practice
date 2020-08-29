from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class User(AbstractBaseUser):
    username = None
    email = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=100, default=False)

    USERNAME_FIELD = 'email'

