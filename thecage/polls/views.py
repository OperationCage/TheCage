from django.shortcuts import render
from django.http import HttpResponse

def cryptids(request):
    return render(request, './polls/cryptids.html')

def location(request):
    return render(request, './polls/location.html')

def home(request):
    return render(request, './main.html')

def indicryptids(request):
    return render(request, './polls/indicryptids.html')

def all_cryptids_here(request):
    return render(request, './polls/all_cryptids_here.html')

def cryptid_disc_date(request):
    return render(request, './polls/cryptid_disc_date.html')
