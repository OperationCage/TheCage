from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def crypids(request):
    return render(request, './crypids.html')

def location(request):
    return render(request, './location.html')

def indicrypids(request):
    return render(request, './indicrypids.html')

def all_crypids_here(request):
    return render(request, './all_crypids_here.html')

def crypid_disc_date(request):
    return render(request, './crypid_disc_date.html')

def crypid_disc_date(request):
    return render(request, './location')

    
