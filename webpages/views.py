from django.shortcuts import render

def home(request):
    return render(request, 'webpages/home.html')

def about(request):
    return render(request, 'webpages/about.html')

# Create your views here.
