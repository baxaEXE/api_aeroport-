from rest_framework.serializers import *
from apps.airlane.models import Airlane  
from apps.flight.models import Flight
from apps.plane.models import Plane

class AirlaneSerializer(ModelSerializer):

    class Meta:
        model = Airlane
        fields = '__all__'

class FlightSerializer(ModelSerializer):

    class Meta:
        model = Flight
        fields = '__all__'

class PlaneSerializer(ModelSerializer):

    class Meta:
        model = Plane
        fields = '__all__'