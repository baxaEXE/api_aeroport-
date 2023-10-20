from .serializers import PlaneSerializer,AirlaneSerializer,FlightSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *

from apps.airlane.models import Airlane
from apps.plane.models import Plane
from apps.flight.models import Flight


class PlaneAPIView(APIView):
    def get(self, request):
        plane = Plane.objects.all()
        serializer = PlaneSerializer(plane, many=True)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def post(self, request):
        serializer = PlaneSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    

class PlaneDetailAPIView(APIView):
    def get(self, request, pk):
        plane = Plane.objects.get(pk=pk)
        serializer = PlaneSerializer(plane)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    def patch(self, request, pk):
        plane = Plane.objects.get(pk=pk)
        serializer = PlaneSerializer(plane,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        plane=Plane.objects.get(pk=pk)
        plane.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class AirlineAPIView(APIView):
    def get(self, request):
        airline = Airlane.objects.all()
        serializer = AirlaneSerializer(airline, many=True)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def post(self, request):
        serializer = AirlaneSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    
    
class AirlineDetailAPIView(APIView):
    
    def get(self, request, pk):
        airline = Airlane.objects.get(pk=pk)
        serializer = AirlaneSerializer(airline)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    def patch(self, request, pk):
        airline = Plane.objects.get(pk=pk)
        serializer = PlaneSerializer(airline,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        airline=Airlane.objects.get(pk=pk)
        airline.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class FlightAPIView(APIView):

    def get(self,request):
        flight = Flight.objects.all()
        serializer = FlightSerializer(flight, many=True)
        return Response(serializer.data,status=HTTP_200_OK)
    
    def post(self, request):
        serializer = FlightSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    
    
class FlightDetailAPIView(APIView):
    def get(self, request, pk):
        flight = Flight.objects.get(pk=pk)
        serializer = FlightSerializer(flight)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    def patch(self, request, pk):
        flight = Flight.objects.get(pk=pk)
        serializer = FlightSerializer(flight,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        flight = Flight.objects.get(pk=pk)
        flight.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    