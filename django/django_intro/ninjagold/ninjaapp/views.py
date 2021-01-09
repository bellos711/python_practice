from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
import random


def index(request):
    if 'my_gold' not in request.session:
        request.session['my_gold'] = 0
        # request.session['my_activity'] = "\nYour gold digging session has started..."
        request.session['my_activity'] = []
    else:
        print("YOU ARE IN THE SESSION, DAWG")
    return render(request, "index.html")
    
    
def process(request):
    location = request.POST['gold_spot']
    time = strftime("%Y/%m/%d %H:%M %p", localtime())

    print("GOLD LOCATION IS", location)
    if(location == 'farm'):
        gold = random.randint(10,20)
        print("If statement in", location, "\ngold received is: ", gold)
        request.session['my_gold'] += gold
        # request.session['my_activity'] += (f'\nYou have received {gold} gold from the {location} at {time}')
        request.session['my_activity'].append(f"<p class='correct'>You have received {gold} gold from the {location} at {time}</p>")
    if(location == 'cave'):
        gold = random.randint(5,10)
        print("If statement in", location, "\ngold received is: ", gold)
        request.session['my_gold'] += gold
        # request.session['my_activity'] += (f"\nYou have received {gold} gold from the {location} at {time}")
        request.session['my_activity'].append(f"<p class='correct'>You have received {gold} gold from the {location} at {time}</p>")
    if(location == 'house'):
        gold = random.randint(2,5)
        print("If statement in", location, "\ngold received is: ", gold)
        request.session['my_gold'] += gold
        # request.session['my_activity'] += (f"\nYou have received {gold} gold from the {location} at {time}")
        request.session['my_activity'].append(f"<p class='correct'>You have received {gold} gold from the {location} at {time}</p>")
    if(location == 'casino'):
        gold = random.randint(-50,50)
        if(gold < 0):
            print("If statement in", location, "\ngold received is: ", gold)
            request.session['my_gold'] += gold
            # request.session['my_activity'] += (f"\nYou have lost {gold} gold from the {location} at {time}... ouch")
            request.session['my_activity'].append(f"<p class='incorrect'>You have lost {gold} gold from the {location} at {time}... ouch</p>")
        else:
            print("If statement in", location, "\ngold received is: ", gold)
            request.session['my_gold'] += gold
            # request.session['my_activity'] += (f"\nYou have received {gold} gold from the {location} at {time}")
            request.session['my_activity'].append(f"<p class='correct'>You have received {gold} gold from the {location} at {time}</p>")            
    request.session.save()
    return redirect("/")
# Create your views here.

