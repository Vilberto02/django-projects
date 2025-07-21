from rest_framework import serializers
from .models import Programador, Disenador

class ProgramadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programador
        fields = '__all__'

class DisenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disenador
        fields = '__all__'