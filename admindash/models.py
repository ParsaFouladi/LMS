from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from accounts.models import Student,Teacher


class Course(models.Model):
    code = models.CharField(max_length=150 , unique=True)
    name=models.CharField(max_length=150)

    student = models.ManyToManyField(Student, null=True)
    Teacher = models.ManyToManyField(Teacher, null=True)

    def __str__(self):
        return self.code


class Exam(models.Model):
    exam = models.CharField(max_length=100)

    def __str__(self):
        return self.exam


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    questions = models.TextField()
    answers = models.CharField(max_length=20)
    option_a = models.TextField()
    option_b = models.TextField()
    option_c = models.TextField()
    option_d = models.TextField()

    def __str__(self):
        return self.questions


class Answer(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer
