from django.shortcuts import render
from .models import Cryptid

def cryptids(request):
    data={"cryptids": Cryptid.objects.all()}
    return render(request, 'polls/all_cryptids_here.html', data)

def cryptid(request, cryptid_id):
    data={"cryptid": Cryptid.objects.get(pk=cryptid_id)}
    return render(request, "polls/indicryptids.html", data)

def location(request):
    return render(request, 'polls/location.html')

def home(request):
    return render(request, './main.html')

def all_cryptids_here(request):
    data={"names": Cryptid.objects.all()}
    return render(request, 'polls/all_cryptids_here.html', data)

def cryptid_disc_date(request):
    return render(request, 'polls/cryptid_disc_date.html')
