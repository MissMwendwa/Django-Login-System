from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "loginapp/index.html")

#the signing requests
def signup(request):

    if request.method == POST:
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        
    return render(request, "loginapp/signup.html")

def signin(request):
    return render(request, "loginapp/signin.html")

def signout(request):
    pass