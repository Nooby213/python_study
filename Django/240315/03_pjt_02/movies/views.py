from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, '01-home.html')

def community(request):
    return render(request, '02-community.html')