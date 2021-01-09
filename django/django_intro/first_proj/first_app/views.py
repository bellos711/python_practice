from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

#def first_view(request):
#    return HttpResponse("This is the first-app from first route in proj folder inner urls, calling the first view")

#def second_view(request):
#    return HttpResponse("This is the first-app from first route in proj folder inner urls, calling the second view")

