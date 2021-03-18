from django.urls import path
from . import views

urlpatterns = [
    path("crypids/", views.crypids),
    path("location/", views.location),
    path("indicrypids/", views.indicrypids),
    path("all_crypids_here/", views.all_crypids_here),
    path("crypid_disc_date/", views.crypid_disc_date),

]