from django.shortcuts import render, HttpResponse, redirect
from .models import *
# Create your views here.
def index(request):
    context = {
        "all_books" : Books.objects.all()
    }
    return render(request, 'index.html', context)

def authors(request):
    context = {
        "all_authors" : Authors.objects.all()
    }
    return render(request, 'authors.html', context)

def bookinfo(request, book_id):
    print("THIS IS THE BOOK ID FROM THE URL",book_id)
    the_book = Books.objects.get(id=book_id)
    context = {
        "this_book" : the_book,
        "all_authors" : Authors.objects.all()
    }
    print("THIS IS THE BOOK OBJECTS",the_book)
    print("THIS IS THE BOOK OBJECTS",the_book.title)
    return render(request, 'bookinfopage.html', context)

def authorinfo(request, author_id):
    print("THIS IS THE AUTHOR ID FROM THE URL",author_id)
    the_author = Authors.objects.get(id=author_id)
    context = {
        "this_author" : the_author,
        "all_books" : Books.objects.all()
    }
    print("THIS IS THE AUTHOR OBJECTS",the_author)
    print("THIS IS THE AUTHOR OBJECTS",the_author.first_name)
    return render(request, 'authorinfopage.html', context)

def addbook(request):
    book = Books.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc']
    )
    return redirect('/')

def addauthor(request):
    author = Authors.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes']
    )
    return redirect('/authors')

def linkauthor(request, book_id):
    this_book = Books.objects.get(id=book_id)
    #print("This is the books ID from linkauthor ", this_book.id)
    #print("This is the books ID from linkauthor ", this_book.title)
    #selected_author = request.POST['author_select']
    this_author = Authors.objects.get(id=request.POST['author_select'])
    #print("This is the AUTHOR ID from linkauthor ", this_author.id)
    #print("This is the AUTHOR ID from linkauthor ", this_author.first_name)
    this_book.authors.add(this_author)

    return redirect(f'/see_book/{book_id}')

def linkbook(request, author_id):
    this_author = Authors.objects.get(id=author_id)
    print("This is the books ID from linkauthor ", this_author.id)
    print("This is the books ID from linkauthor ", this_author.first_name)
    this_book = Books.objects.get(id=request.POST['book_select'])
    print("This is the AUTHOR ID from linkauthor ", this_book.id)
    print("This is the AUTHOR ID from linkauthor ", this_book.title)
    this_author.book.add(this_book)
    return redirect(f'/see_author/{author_id}')