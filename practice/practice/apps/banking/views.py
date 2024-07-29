from django.shortcuts import render
from .forms import RegisterForm

def home(request):
    return render(request, 'banking/index.html')

def register(request):
    form = RegisterForm()

    return render(request, 'banking/register.html', {'form':form})

