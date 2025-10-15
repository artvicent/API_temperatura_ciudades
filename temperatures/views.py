from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .models import CityTemperature
from .serializers import CityTemperatureSerializer

class CityTemperatureViewSet(viewsets.ModelViewSet):
    queryset = CityTemperature.objects.all().order_by('city')
    serializer_class = CityTemperatureSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
