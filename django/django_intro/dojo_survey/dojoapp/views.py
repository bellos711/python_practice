from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def result(request):
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    comment = request.POST['comment']
    context = {
        "result_name" : name,
        "result_location" : location,
        "result_language" : language,
        "result_comment" : comment
    }
    return render(request, "result.html", context)