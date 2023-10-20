from django.urls import path,include
from .views import (
    AirlineAPIView,
    AirlineDetailAPIView,
    PlaneAPIView,
    PlaneDetailAPIView,
    FlightAPIView,
    FlightDetailAPIView
)


urlpatterns = [
    path('plane/',PlaneAPIView.as_view()),
    path('plane_detail/<int:pk>/',PlaneDetailAPIView.as_view()),
    path('airline/',AirlineAPIView.as_view()),
    path('airline_detail/<int:pk>/',AirlineDetailAPIView.as_view()),
    path('flight/',FlightAPIView.as_view()),
    path('flight_detail/<int:pk>/',FlightDetailAPIView.as_view()),
    path('auth/', include('dj_rest_auth.urls'))
]
