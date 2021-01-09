from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime

# Create your views here.

def test_method(request):
    return HttpResponse("you are linked")

def time(request):
    time_context = {
        "time": strftime("%Y / %B / %d %H:%M %p", localtime())
    }
    return render(request, 'index.htm', time_context)