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
        'user_object': User.objects.get(id=request.session['uuid']),
        'all_books' : Book.objects.all()
    }
    print(f"All books object {context['all_books']}")
    return render(request, 'dashboard.html', context)

def add_book_page(request):
    print("you are about to add a book your id is ", request.session['uuid'])
    context = {
        'all_authors' : Author.objects.all()
    }
    print(f"This is all the authors {Author.objects.all()}")
    return render(request, 'addbook.html', context)

def bookinfo(request, book_id):
    print("You are now in specific book's info")
    book_instance = Book.objects.get(id=book_id)
    first_reviewer_test = book_instance.user_who_reviewed.first()
    print("*"*50)
    print(f"The first reviewer in this specific book id{book_id} is user with name {first_reviewer_test.first_name}")
    context = {
        'this_book' : book_instance,
        'first_reviewer' : first_reviewer_test
    }
    return render(request, 'bookinfo.html', context)



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
    
def add_author_logic(request):
    new_author_to_add = Author.objects.create(
        author_name = request.POST['author_name']
    )
    return redirect('/add')

def addbook_logic(request):
    print("adding book logic, ",request.POST)
    this_user = User.objects.get(id=request.session['uuid'])
    author_instance = Author.objects.get(id=request.POST['author_id'])
    print(f"{this_user.first_name} is adding a book...")
    created_book = Book.objects.create(
        title = request.POST['title'],
        review = request.POST['review'],
        rating = request.POST['rating'],
        author = author_instance
    )

    print(f"We are adding this user {this_user.first_name} as the reviewer for this book {created_book.title}")
    created_book.user_who_reviewed.add(this_user)
    return redirect(f'/books/{created_book.id}')