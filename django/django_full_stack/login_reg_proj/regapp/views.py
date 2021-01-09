from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *

#render urls
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    if 'uuid' not in request.session:
        print("NO SESSION, invalid dashboard access")
        return redirect('/')

    context = {
        'user_object': User.objects.get(id=request.session['uuid']) 
    }
    return render(request, 'dashboard.html', context)



#redirect to urls
def register(request):
    print("Register function", request.POST)
    #TODO
    #read post data
    errors = User.objects.basic_validator(request.POST)
    #validate
    if len(errors) > 0:
        print("There are errors")
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        print("No errors")
        #hash pw
        hash_slinging_slasher = bcrypt.hashpw(
            request.POST['password'].encode(), 
            bcrypt.gensalt()
            ).decode()  # create the hash  
        print(f"our hash:  {hash_slinging_slasher}")
        #add user to database
        
        created_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            #password = request.POST['password'] #VERY VERY BAD
            password = hash_slinging_slasher
        )
        print("Our newly registered user pass: ", created_user.password)
        print(f"my newly created user's's id is {created_user.id}")
        #set us up in session
        request.session['uuid'] = created_user.id
        return redirect('/dashboard') #WATCH OUT FOR THIS REDIRECT


def logout(request):
    request.session.flush()
    return redirect('/')


def login(request):
    print(f"our post data is {request.POST}")
    #check password through validator
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        print("There are errors")
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    else:
        #check email in db
        user_list = User.objects.filter(email=request.POST['email'])
        #setup user in session
        request.session['uuid'] = user_list[0].id
        # never render on a post, always redirect!
        return redirect('/dashboard')
    