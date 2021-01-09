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

    this_user = User.objects.get(id=request.session['uuid'])
    this_user_wishes = this_user.wish_uploaded.all()
    context = {
        'user_object': this_user,
        'all_users_wishes' : this_user_wishes.filter(is_granted=False),
        'all_wishes' : Wish.objects.filter(is_granted=True)
    }
    print("*"*50)
    print(f"User {this_user.first_name} wishes are {this_user.wish_uploaded.all()}")
    return render(request, 'dashboard.html', context)

def new_wish_page(request):
    print("You are about to make a wish")
    context = {
        'this_user': User.objects.get(id=request.session['uuid'])
    }
    return render(request, 'newwish.html', context)

def edit_wish_page(request, wish_id):
    print("You are about to EDIT this wish")
    
    context = {
        'this_user': User.objects.get(id=request.session['uuid']),
        'this_wish' : Wish.objects.get(id=wish_id)
    }
    print("*"*50)
    print(f"This specific wish id is {context['this_wish'].title}")
    return render(request, 'editwish.html', context)



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
        return redirect('/wishes') #WATCH OUT FOR THIS REDIRECT


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
        return redirect('/wishes')
    
def add_wish_logic(request):
    print("Adding wish now...",request.POST)
    errors_dictionary = Wish.objects.wish_validator(request.POST)
    if len(errors_dictionary) > 0:
        print("There are errors")
        for key, value in errors_dictionary.items():
            messages.error(request, value)
        return redirect('/wishes/new')

    this_user = User.objects.get(id=request.session['uuid'])

    created_wish = Wish.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc'],
        uploaded_by = this_user
    )
    return redirect('/wishes')

def edit_wish_logic(request, wish_id):
    print("Editing wish now...", request.POST)
    errors_dictionary = Wish.objects.wish_validator(request.POST)
    if len(errors_dictionary) > 0:
        print("There are errors")
        for key, value in errors_dictionary.items():
            messages.error(request, value)
        return redirect(f'/wishes/edit/{wish_id}')

    this_wish = Wish.objects.get(id=wish_id)
    print(f"This wish is {this_wish.title} id is {this_wish.id}")
    this_wish.title = request.POST['title']
    this_wish.desc = request.POST['desc']
    this_wish.save()
    
    return redirect('/wishes')

def grant_wish_logic(request, wish_id):
    print("granting wish now...")
    this_wish = Wish.objects.get(id=wish_id)
    print(f"This wish is {this_wish.title} was previously granted: {this_wish.is_granted}")
    this_wish.is_granted = True
    this_wish.save()
    return redirect('/wishes')

def add_like_logic(request, wish_id):
    print("#"*30)
    print("You are creating a list of users who liked")
    this_wish = Wish.objects.get(id=wish_id)
    this_user = User.objects.get(id=request.session['uuid'])
    print(f"our wish is {this_wish.title}, our user is {this_user.first_name}")
    this_wish.users_who_liked.add(this_user)
    return redirect('/wishes')