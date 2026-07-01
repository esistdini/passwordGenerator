from django.shortcuts import render
from django.http import HttpResponse
from . import password_generator

# Create your views here.
def home(request):
    return render(request,"main.html")

def output(request):
    user_input = request.POST.get("passLength")
    print(user_input)
    a = password_generator.passwordGenerator()
    output = a.operation(user_input)
    return render(request,"output.html",{'output':output})