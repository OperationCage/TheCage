from django.shortcuts import render
from django.http import HttpResponse

def cryptids(request):
    return render(request, './cryptids.html')

def crypids(request):
    return render(request, './polls/crypids.html')

def location(request):
    return render(request, './polls/location.html')

def indicryptids(request):
    return render(request, './indicryptids.html')

def all_cryptids_here(request):
    return render(request, './all_cryptids_here.html')

def cryptid_disc_date(request):
    return render(request, './cryptid_disc_date.html')

def home(request):
    return render(request, './main.html')

def indicrypids(request):
    return render(request, './polls/indicrypids.html')

def all_crypids_here(request):
    return render(request, './polls/all_crypids_here.html')

def crypid_disc_date(request):
    return render(request, './polls/crypid_disc_date.html')
