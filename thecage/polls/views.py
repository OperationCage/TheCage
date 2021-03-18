from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def cryptids(request):
    return render(request, './cryptids.html')

def location(request):
    return render(request, './location.html')

def indicryptids(request):
    return render(request, './indicryptids.html')

def all_cryptids_here(request):
    return render(request, './all_cryptids_here.html')

def cryptid_disc_date(request):
    return render(request, './cryptid_disc_date.html')

def home(request):
    return render(request, './main.html')


    
