from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=100, default=False)
    USERNAME_FIELD = 'email'


class Image(models.Model):
    image = models.ImageField(blank=True, upload_to="image%Y%m%d")
    create_at = models.DateField(blank=True,  auto_now_add=True)
    updated_at = models.DateField(blank=True, auto_now=True)

    class Meta:
        db_table = 'store'

