from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import user
from AppTwo.forms import NewUserForm
#Create your views here.

def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'help.html',context=helpdict)

def users(request):

    form = NewUserForm()
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        
        else:
            print("Invalid")
    
    return render(request,'users.html',{'form':form}) 
