from django.shortcuts import render, HttpResponse



# Create your views here.

def home(request):
    return render(request, "core/home.html")

def search(request):
    return render(request, "core/search.html")

def contact(request):
    return render(request, "core/contact.html") 

def about(request):
    return render(request, "core/about.html") 