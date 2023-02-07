from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "loginapp/index.html")

#the signing requests
def signup(request):
    return render(request, "loginapp/signup.html")

def signin(request):
    return render(request, "loginapp/signin.html")

def signout(request):
    pass