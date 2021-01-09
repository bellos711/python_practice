from django.shortcuts import render, HttpResponse, redirect
from .models import Users
#from django.db import models

def index(request):
    context = {
        'users': Users.objects.all()
    }
    return render(request,"index.html", context)

def create_user(request):
    print(request.POST)
    print('Creating User')
    user = Users.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email_address=request.POST['email_address'],
        age=request.POST['age']
    )
    print(user)
    return redirect('/')