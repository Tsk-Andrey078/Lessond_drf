from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from lessond_drf.serializer import NewsSerializer
from .models import NewsModel

# Create your views here.
class ListInfo(APIView):
    def get(self, request, format=None):
        article_titles = [article for article in NewsModel.objects.all()]
        serializer = NewsSerializer(article_titles, many=True)
        return Response(serializer.data)