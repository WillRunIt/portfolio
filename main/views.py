from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("<h2>Welcome to the home page</h2>")

def portfolio(request):
    return HttpResponse("<h2>Welcome to my portfolio</h2>")

def about(request):
    return HttpResponse("<h2>Welcome to the About me page</h2>")
def contact(request):
    return HttpResponse("<h2>Welcome to the Contact page</h2>")