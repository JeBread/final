from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core import serializers
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

@api_view(['POST'])
def create_comment(request,article_pk):
    article=Article.objects.get(pk=article_pk)
    serializer=CommentSerializer(data=request.data,context={'request':request,'article':article})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    return Response(serializer.errors,status=404)

@api_view(['POST'])
def like(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    user = request.user

    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        is_liked=False
    else:
        article.like_users.add(user)
        is_liked=True
    context={
        'is_liked': is_liked,
        'like_users': article.like_users.count(),
    }
    return Response(data=context)

@api_view(['DELETE'])
def article_delete(request,article_pk):
    article=Article.objects.get(pk=article_pk)
    article.delete()
    return Response()

@api_view(['DELETE'])
def comment_delete(request,comment_pk):
    comment=Comment.objects.get(pk=comment_pk)
    comment.delete()
    return Response()
