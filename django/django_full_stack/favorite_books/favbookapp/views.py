from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *

#render urls
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    if 'uuid' not in request.session:
        print("NO SESSION, invalid books dashboard access")
        return redirect('/')

    context = {
        'user_object': User.objects.get(id=request.session['uuid']),
        'all_books': Book.objects.all()
    }
    print(f"Your user object is {User.objects.get(id=request.session['uuid'])}")
    print(f"Uploaded by object field in Book model is {context['all_books'][0].uploaded_by}")
    print(f"this is the query set of all books {Book.objects.all()}")
    return render(request, 'dashboard.html', context)

def view_edit_book(request, book_id):
    print(f"we are either viewing or editing a book of id {book_id}")
    user_instance = User.objects.get(id=request.session['uuid'])
    context = {
        'this_author' : user_instance,
        'this_book' : Book.objects.get(id=book_id),
        
    }
    return render(request, 'vieweditbook.html', context)



#redirect to urls
def register(request):
    print("Register function", request.POST)
    
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
        return redirect('/books') #WATCH OUT FOR THIS REDIRECT


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
        return redirect('/books')


def addbook_logic(request):
    #call the validator for adding book
    errors_dictionary = Book.objects.add_book_validator(request.POST)
    if len(errors_dictionary) > 0:
        print("There are errors")
        for key, value in errors_dictionary.items():
            messages.error(request, value)
        return redirect('/books')

    print("Adding a book")
    #grab user
    print('Our unique user id is', request.session['uuid'])
    this_user = User.objects.get(id=request.session['uuid'])
    print(f"our user object is {this_user} with fname {this_user.first_name}")
    #create a book
    created_book_instance = Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc'],
        uploaded_by = this_user
    )

    print("*"*30)
    print(f"We created your book object {created_book_instance} with title {created_book_instance.title} and uploaded by you {created_book_instance.uploaded_by.first_name}")
    print("We need to make this part of your favs by default.\nDoing that now...")
    created_book_instance.users_who_liked.add(this_user)
    print("As the book is generated, it is added as your favorites or likes")
    print(f"This is the books, total likes for now: {created_book_instance.users_who_liked}")
    return redirect('/books')

def add_fav_logic(request, book_id):
    print("#"*30)
    print("You are adding this book to favorites")
    this_book = Book.objects.get(id=book_id)
    this_user = User.objects.get(id=request.session['uuid'])
    print(f"our book is {this_book.title}, our user is {this_user.first_name}")
    this_book.users_who_liked.add(this_user)
    return redirect('/books')

def unfav_logic(request, book_id):
    print("#"*30)
    print("You are unfavoriting a book")
    this_book = Book.objects.get(id=book_id)
    this_user = User.objects.get(id=request.session['uuid'])
    print(f"our book is {this_book.title}, our user is {this_user.first_name}")
    this_book.users_who_liked.remove(this_user)
    return redirect('/books')

def delete_book_logic(request, book_id):
    print("#"*30)
    print("Deleting this book")
    this_book = Book.objects.get(id=book_id)
    this_book.delete()
    return redirect('/books')

def edit_book_logic(request, book_id):
    print("#"*30)
    print("Editing this book")
    print(request.POST)
    #call the validator for editing book
    errors_dictionary = Book.objects.add_book_validator(request.POST)
    if len(errors_dictionary) > 0:
        print("There are errors")
        for key, value in errors_dictionary.items():
            messages.error(request, value)
        return redirect(f'/books/{book_id}')

    this_book = Book.objects.get(id=book_id)
    this_book.title = request.POST['title']
    this_book.desc = request.POST['desc']
    this_book.save()
    return redirect(f'/books/{book_id}')