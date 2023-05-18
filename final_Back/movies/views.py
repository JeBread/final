from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET',])
def movie_list(request):
    movies=Movie.objects.all()
    serializer=MovieListSerializer(movies,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request,movie_pk):
    movie=Movie.objects.get(pk=movie_pk)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)
