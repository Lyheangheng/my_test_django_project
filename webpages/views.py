from django.shortcuts import render
from datetime import datetime

def home(request):
    context = {
        'current_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return render(request, 'webpages/home.html', context)

def about(request):
    return render(request, 'webpages/about.html')

# Create your views here.
