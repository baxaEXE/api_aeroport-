from django.db.models import *
from apps.plane.models import Plane
from apps.airlane.models import Airlane

class Flight(Model):
    
    fromm = CharField(max_length=128)
    too = CharField(max_length=128)
    plane = ForeignKey(Plane,on_delete=CASCADE)
    airlane = ForeignKey(Airlane,on_delete=CASCADE)
    price = PositiveIntegerField()

    def __str__(self):
        return f'{self.fromm}'
