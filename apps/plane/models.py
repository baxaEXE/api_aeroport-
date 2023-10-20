from django.db.models import *


class Plane(Model):
    name = CharField(max_length=128)
    characteristics = TextField(blank=True,null=True)
    capacity =DecimalField(decimal_places=2,default=0,max_digits=4)

    def __str__(self):
        return f'{self.name}'