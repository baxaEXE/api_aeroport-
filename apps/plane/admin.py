from django.contrib.admin import *
from .models import Plane

@register(Plane)

class PlaneUser(ModelAdmin):
    list_display = ('name','characteristics','capacity')
    list_display_links = ('name','characteristics','capacity')