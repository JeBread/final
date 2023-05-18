from rest_framework import serializers
from .models import *


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
