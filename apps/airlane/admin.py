from django.contrib.admin import *
from .models import Airlane

@register(Airlane)

class AirlaneUser(ModelAdmin):
    list_display = ('name','created_at')
    list_display_links = ('name','created_at')

     


