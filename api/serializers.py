from rest_framework import serializers
from . models import Article
from birthday.models import Birthday

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'description']

class BirthdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Birthday
        fields = ['id', 'name', 'age', 'image']