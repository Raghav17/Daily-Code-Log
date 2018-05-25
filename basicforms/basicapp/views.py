from django.shortcuts import render
from . import form
# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    forma = form.FormName()
    return render(request,'basicapp/form_page.html',{'form':forma})

