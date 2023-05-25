from django.shortcuts import render,HttpResponse

# Create your views here.

def Home(request): 
    return render(request,"home.html") 

def app1(request): 
    return render(request,"app1.html") 
