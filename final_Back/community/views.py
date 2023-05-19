from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def index(request):
    articles=Article.objects.all()
    serializer=ArticleListSerializer(articles,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request,article_pk):
    article=Article.objects.get(pk=article_pk)
    serializer=ArticleDetailSerializer(article)
    return Response(serializer.data)

@api_view(['POST'])
def create_article(request):
    serializer=ArticleDetailSerializer(data=request.data,context={'request':request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    return Response(serializer.errors,status=404)

