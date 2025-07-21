from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProgramadorSerializer, DisenadorSerializer
from .models import Programador, Disenador

# Create your views here.

class ProgramadorViewSet(viewsets.ModelViewSet):
    queryset = Programador.objects.all()
    serializer_class = ProgramadorSerializer

class DisenadorViewSet(viewsets.ModelViewSet):
    queryset = Disenador.objects.all()
    serializer_class = DisenadorSerializer