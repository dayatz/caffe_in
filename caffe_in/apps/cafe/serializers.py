from rest_framework import serializers
from .models import Cafe, Menu, Gallery


class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        exclude = ['']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        exclude = ['']


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        exclude = ['']
