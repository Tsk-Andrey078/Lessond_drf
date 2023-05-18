from rest_framework import serializers
from .models import NewsModel

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = (
            'id',
            'add_date',
            'title',
            'text'
        )