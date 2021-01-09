from django.shortcuts import render, HttpResponse, redirect #redirect needed for redirect
from django.http import JsonResponse #for JsonResponse

# def index(request):
#     return HttpResponse("YOU ARE LINKED")




def root_method(request):
    return redirect("/blogs")

def another_method(request):
    return redirect("/redirected_route")

def redirected_method(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})

def index(request):
    return HttpResponse("placeholder")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, my_val):
    return HttpResponse(f"<p>placeholder to display blog number: {my_val}</p>")

def edit(request, my_val):
    return HttpResponse(f"<p>placeholder to edit blog {my_val}</p>")

def destroy(request, my_val):
    return redirect("/blogs")

def bonus(request):
    return JsonResponse({"title": "my first blog", "content": "lorem , ipsum dolor"})





def test_view(request):
    return HttpResponse('Welcome')

def one_method(request):
    return HttpResponse("Your bear thing worked.")

#def another_method1(request, my_val):
#    pass

def yet_another(request, name):
    pass

def one_more(request, id, color):
    pass
