from dataclasses import field
import imp
from pyexpat import model
from rest_framework import serializers
from .models import Cat
class CatsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cat
        fields='__all__'