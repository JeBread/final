from rest_framework import serializers
from .models import *

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields='__all__'
        


class ArticleDetailSerializer(serializers.ModelSerializer):

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

