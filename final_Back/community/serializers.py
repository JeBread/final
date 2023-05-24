from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields='__all__'
        

class CommentSerializer(serializers.ModelSerializer):
    username=serializers.CharField(source='user.username',read_only=True)
    def create(self, validated_data):
    
        request = self.context.get("request")
        
        comment = Comment()
        comment.content = validated_data['content']
        comment.article_id=self.context.get("article")
        comment.user = request.user

        comment.save()

        return comment

    class Meta:
        
        model=Comment
        fields='__all__'
        read_only_fields=('article_id','user')

class ArticleDetailSerializer(serializers.ModelSerializer):
    comment_set=CommentSerializer(many=True,read_only=True)
    username=serializers.CharField(source='user.username',read_only=True)
    like_users_count=serializers.IntegerField(source='like_users.count',read_only=True)
    def create(self, validated_data):
    
        request = self.context.get("request")
        
        article = Article()
        article.title = validated_data['title']
        article.content = validated_data['content']
        article.user = request.user

        article.save()

        return article

    class Meta:
        
        model=Article
        fields='__all__'
        read_only_fields=('like_users','user')

class ArticleListSerializer(serializers.ModelSerializer):
    comment_set=CommentSerializer(many=True,read_only=True)
    username=serializers.CharField(source='user.username',read_only=True)
    like_users_count=serializers.IntegerField(source='like_users.count')
    class Meta:
        model=Article
        fields='__all__'