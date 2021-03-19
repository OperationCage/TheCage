from django.shortcuts import render
from django.http import HttpResponse
from .models import Cryptid, Location

def cryptid(request, cryptid_id):
    data={"cryptid": Cryptid.objects.get(pk=cryptid_id)}
    return render(request, "polls/indicryptids.html", data)

def cryptids(request):
    data={"cryptids": Cryptid.objects.all()}
    return render(request, 'polls/all_cryptids_here.html', data)

def location(request, location_id):
    location = Location.objects.get(pk=location_id)
    return render(request, 'polls/location.html', {'location':location})

def locations(request):
    locations = Location.objects.all()
    return render(request, 'polls/locations.html', {'locations':locations})

def home(request):
    return render(request, 'polls/cryptids.html')

def all_cryptids_here(request):
    data={"names": Cryptid.objects.all()}
    return render(request, 'polls/all_cryptids_here.html', data)

def cryptid_disc_date(request):
    return render(request, 'polls/cryptid_disc_date.html')
