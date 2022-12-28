from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import CreateTeacherForm,CreateStudentForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')
def register(request):
    if request.method == 'POST':
        if request.POST.get("Student"):
            form = CreateStudentForm(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('first_name')
                messages.success(request, "Account is created successfully " + user + "!")

            return HttpResponse(f"{form.errors}") 

        elif request.POST.get('Teacher'):
            form = CreateTeacherForm(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('first_name')
                messages.success(request, "Account is created successfully " + user + "!")

            return HttpResponse(f"{form.errors}") 
        else:
            print(request.POST.getlist['role'])
    
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

