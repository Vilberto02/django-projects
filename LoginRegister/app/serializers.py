from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('companyName', 'ruc')

    def create(self, validated_data):
        user = User.objects.create_user(
            companyName=validated_data['companyName'],
            ruc=validated_data['ruc'],
        )
        return user

