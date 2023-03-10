

# Create your models here.
from django.db import models
# from admindash.models import Course
# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser
# )
from django.contrib.auth.models import User


# class UserManager(BaseUserManager):
#     def create_user(self, roll, phone, name, password=None):
#         if not roll:
#             raise ValueError('You Dont have Permission to do exam')
#         user = self.model(
#             roll=roll,
#             phone=phone,
#             name=name
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, roll, phone, name, password):
#         user = self.create_user(roll, phone, name, password=password)
#         user.is_admin = True
#         user.is_staff = True
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser):
#     phone = models.CharField(verbose_name='phone number', max_length=12, unique=True)
#     name = models.CharField(max_length=150, null=True)
#     roll = models.CharField(max_length=20, verbose_name='roll', unique=True)
#     course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
#     date_joind = models.DateTimeField(verbose_name='date joind', auto_now_add=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     USERNAME_FIELD = 'roll'
#     REQUIRED_FIELDS = ['name', 'phone']
#     objects = UserManager()

#     def __str__(self):
#         return self.name

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return True

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # course = models.ManyToManyField(Course, null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return (self.user.first_name + ' ' +self.user.last_name)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    username = models.CharField(max_length=100,unique=True,default="notUsed")
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50,null=True)
    email=models.EmailField()
    # course = models.ManyToManyField(Course, null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    is_active = models.BooleanField(default=True)
    REQUIRED_FIELDS = ['username','first_name', 'last_name','email']
    def __str__(self):
        return (self.first_name + ' ' +self.last_name)
