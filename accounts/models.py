from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    GENDER = (
        ("male", "남성"),
        ("female", "여성")
    )
    email = models.EmailField(unique=True, blank=False, null=False)
    gender = models.CharField(max_length=80, choices=GENDER, blank=True, null=True)
    password = models.CharField(max_length=255, blank=False, null=False)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    introduce = models.TextField(max_length=500, null=True, blank=True)
    birthday = models.DateField(blank=False, null=False)
    nickname = models.CharField(max_length=50,  blank=False, null=False)


    