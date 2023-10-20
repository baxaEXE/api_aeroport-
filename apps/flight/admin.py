from django.contrib.admin import *
from .models import Flight

@register(Flight)

class FlightUser(ModelAdmin):
    list_display = ('fromm','too','plane','airlane','price')
    list_display_links = ('fromm','too','plane','airlane','price')
