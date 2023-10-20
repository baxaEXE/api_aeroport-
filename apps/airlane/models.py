from django.db.models import *
from apps.plane.models import Plane

class Airlane(Model):
    name = CharField(max_length=256)
    created_at = DateTimeField()
    planes = ManyToManyField(Plane)

    def __str__(self):
        return f'{self.name}'