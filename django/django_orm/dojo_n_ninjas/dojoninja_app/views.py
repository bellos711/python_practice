from django.shortcuts import render, redirect
from .models import Dojos, Ninjas

def index(request):
    context = {
        'dojos' : Dojos.objects.all()
    }
    return render(request, "index.html", context)

def add_ninja(request):
    print(request.POST)
    print('Creating ninja')
    #get dojo instance
    dojo_instance = Dojos.objects.get(id=request.POST['dojo_id'])
    ninja = Ninjas.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        dojo = dojo_instance
    )
    print(ninja)
    return redirect('/')


def add_dojo(request):
    print(request.POST)
    print('Creating dojo')
    dojo = Dojos.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state']
    )
    print(dojon)
    return redirect('/')
