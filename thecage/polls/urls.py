from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("cryptids/", views.cryptids, name='cryptids'),
    path("cryptids/<int:cryptid_id>/", views.cryptid, name="cryptid"),
    path("locations/<int:location_id>/", views.location, name='location'),
    path("locations/", views.locations, name='locations'),
    path("all_cryptids_here/", views.all_cryptids_here, name='all_cryptids_here'),
    path("cryptid_disc_date/", views.cryptid_disc_date, name='cryptid_disc_date'),
]