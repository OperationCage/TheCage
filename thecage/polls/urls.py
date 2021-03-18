from django.urls import path
from . import views

urlpatterns = [
    path("cryptids/", views.cryptids, name='cryptids'),
    path("location/", views.location, name='location'),
    path("indicryptids/", views.indicryptids, name='indicryptids'),
    path("all_cryptids_here/", views.all_cryptids_here, name='all_cryptids_here'),
    path("cryptid_disc_date/", views.cryptid_disc_date, name='cryptid_disc_date'),
    path("", views.home, name="home"),
]