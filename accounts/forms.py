from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Teacher,Student
from django.db import models

class CreateTeacherForm(UserCreationForm):
    # name=models.CharField(max_length=50)
    # surname=models.CharField(max_length=50,null=True)
    class Meta:
        model=User
        fields=['email','first_name', 'last_name','password1','password2']
    
    def save(self, commit=True):
        user = super().save(commit=commit)
        Teacher.objects.create(user=user)
        return user

class CreateStudentForm(UserCreationForm):
    # name=models.CharField(max_length=50)
    # surname=models.CharField(max_length=50,null=True)
    class Meta:
        model=User
        fields=['email','first_name', 'last_name','password1','password2']
    
    def save(self, commit=True):
        user = super().save(commit=commit)
        Teacher.objects.create(user=user)
        return user

