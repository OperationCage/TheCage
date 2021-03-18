from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def crypids(request):
    return render(request, './polls/crypids.html')

def location(request):
    return render(request, './polls/location.html')

def indicrypids(request):
    return render(request, './polls/indicrypids.html')

def all_crypids_here(request):
    return render(request, './polls/all_crypids_here.html')

def crypid_disc_date(request):
    return render(request, './polls/crypid_disc_date.html')
