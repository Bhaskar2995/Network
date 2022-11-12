from operator import mod
from re import T
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def _create_user(self,email,password,first_name,last_name,**extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password is not provided")
        
        user = self.model(
            email = self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email,password,first_name,last_name,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,first_name,last_name,password,**extra_fields)

    def create_superuser(self,email,password,first_name,last_name,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,password,first_name,last_name,password,**extra_fields)

    
    
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True,max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=250)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='cars')
    dob = models.DateField()
    age = models.IntegerField()

class Restaurant(models.Model):
    city = models.CharField(max_length=50)
    Area = models.CharField(max_length=50)

class Person(models.Model):
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

