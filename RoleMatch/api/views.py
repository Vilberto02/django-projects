from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProgrammerSerializer, DesignerSerializer
from .models import Programmer, Designer

# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

class DesignerViewSet(viewsets.ModelViewSet):
    queryset = Designer.objects.all()
    serializer_class = DesignerSerializer