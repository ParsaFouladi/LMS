from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.template.context_processors import request

from admindash.models import Course
from .forms import CreateStudentForm
from django.contrib import messages
import django.contrib.auth as au
from admindash import models as QMODEL
# Create your views here.

def index(request):
    return render(request, 'index.html')
def register(request):
    form = CreateStudentForm()
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account is created successfully " + user + "!")

        else:
            print('form is not valid somehow')


    context={'form':form}
    return render(request, 'register.html',context)

def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=au.authenticate(request,username=username,password=password)
        if user is not None:
            au.login(request,user)
        #    return redirect('home')
            return HttpResponse('Login successfully')
        else:
            messages.info(request,'User or Password is incorrect!')


    return render(request, 'login.html')


@login_required
def stddashboard(request):
    dict = {
        'total_course': QMODEL.Course.objects.all(),
    }
    return render(request, 'std-dashboard.html', context=dict)