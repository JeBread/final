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

class MovieGetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=('title','release_date','vote_average','overview',
                'poster_path','ost','video')
