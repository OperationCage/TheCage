from django.urls import path
from . import views

urlpatterns = [
    path("crypids/", views.crypids, name='crypids'),
    path("location/", views.location, name='location'),
    path("indicrypids/", views.indicrypids, name='indicrypids'),
    path("all_crypids_here/", views.all_crypids_here, name='all_crypids_here'),
    path("crypid_disc_date/", views.crypid_disc_date, name='crypid_disc_date'),

]