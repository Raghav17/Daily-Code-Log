from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import user
#Create your views here.

def index(request):
    return HttpResponse("<em>My Second App</em>")
def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'help.html',context=helpdict)
def users(request):
    user_list = user.objects.order_by('first_name')
    user_dict = {"users": user_list}
    return render(request,'users.html',context=user_dict)
