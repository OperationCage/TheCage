from django.contrib import admin
from .models import Name, Location, DiscoveryDate, Description

admin.site.register(Name)
admin.site.register(Location)
admin.site.register(DiscoveryDate)
admin.site.register(Description)