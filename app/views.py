from django.shortcuts import render
from django.http import HttpResponse
from .models import Lugat
# Create your views here.

def HomePage(request):
    soz = request.GET.get('a','')
    if soz and soz != '':    
        natija = Lugat.objects.filter(english__contains=soz).all()[:3]
    else:
        natija=None
    return render(request, 'home.html', {'a' : soz, 'natija':natija})

def AboutPage(request):
    return render(request, 'about.html')

def ContactUs(request):
    return render(request, 'contactus.html')