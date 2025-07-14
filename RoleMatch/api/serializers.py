from rest_framework import serializers
from .models import Programmer, Designer

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = '__all__'

class DesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designer
        fields = '__all__'