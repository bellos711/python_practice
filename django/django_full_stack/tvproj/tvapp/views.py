from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def index(request):
    return redirect('/shows')

def showslist(request):
    context = {
        'all_shows' : Shows.objects.all()
    }
    # for show in context['all_shows']:
    #     show.title
    #     print(f"THIS IS WHAT I SHOULD SEE {show.title}")
    return render(request, 'shows.html', context)

def new_show(request):
    return render(request, 'new.html')

def add_show(request):
    print("-------------Adding a new show-----------")
    errors = Shows.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')

    else:
        show = Shows.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            desc = request.POST['desc']
        )
        print(f"my newly created show's id is {show.id}")
        return redirect(f'/shows/{show.id}')
    

def show_info(request, specific_show_id):
    print("THE SPECIFIC SHOW ID IS ",specific_show_id)
    this_show = Shows.objects.get(id=specific_show_id)
    context = {
        'this_show' : this_show
    }
    return render(request, 'showinfo.html', context)


def edit_show(request, specific_show_id):
    print("You are about to edit a show with id ",specific_show_id)
    this_show = Shows.objects.get(id=specific_show_id)
    context = {
        'this_show' : this_show
    }
    return render(request, 'editshow.html', context)

def edit_logic(request, specific_show_id):
    print("You are now editing the show with id ",specific_show_id)
    errors = Shows.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{specific_show_id}/edit')
    
    else:
        this_show = Shows.objects.get(id=specific_show_id)
        this_show.title = request.POST['title']
        this_show.network = request.POST['network']
        this_show.release_date = request.POST['release_date']
        this_show.desc = request.POST['desc']
        this_show.save()
        return redirect(f'/shows/{specific_show_id}')

def delete_logic(request, specific_show_id):
    this_show = Shows.objects.get(id=specific_show_id)
    this_show.delete()
    return redirect('/shows')