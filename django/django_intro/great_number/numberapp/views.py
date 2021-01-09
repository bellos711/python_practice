from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    print("STARTING INDEX")
    if 'randnum' not in request.session:
        request.session['randnum'] = random.randint(1,100)
        print("AFTER IF NOT IN RANDNUM", request.session['randnum'])
    else:
        print("AFTER ELSE NOT IN RANDNUM", request.session['randnum'])
    return render(request, "index.html")

def guess_method(request):
    if int(request.POST['guess']) > request.session['randnum']:
        print("THE GUESS IS TOO HIGH ",int(request.POST['guess']))
        request.session['hint'] = f"TOO HIGH! Your guess: {int(request.POST['guess'])}"
        return redirect("/")
    elif int(request.POST['guess']) < request.session['randnum']:
        print("THE GUESS IS TOO LOW ",int(request.POST['guess']))
        request.session['hint'] = f"TOO LOW! Your guess: {int(request.POST['guess'])}"
        return redirect("/")
    elif int(request.POST['guess']) == int(request.session['randnum']):
        print("THE GUESS IS CORRECT!")
        request.session['hint'] = f"That is correct! The num was: {request.session['randnum']}"
        return redirect("/")
    
# Create your views here.
