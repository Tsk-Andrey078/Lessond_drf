from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from lessond_drf.serializer import NewsSerializer
from .models import NewsModel

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action

# Create your views here.
class ListInfo(APIView):
    def get(self, request, format=None):
        article_titles = [article for article in NewsModel.objects.all()]
        serializer = NewsSerializer(article_titles, many=True)
        return Response(serializer.data)
    
class NewsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        response = NewsModel.objects.all()
        serialize = NewsSerializer(response, many=True)
        if len(response) > 0:
            return Response(serialize.data)
        else:
            return Response(False)

    def update(self, request):
        print(request.data)
        NewsModel.objects.filter(id=int(request.data['id'])).update(text=request.data['text'])
        return Response("Value is changed")
        
    @action(detail=False, methods=['post'])
    def delete_news(self, request, format=None):
        NewsModel.objects.filter(id = request.data['id']).delete()
        return Response(request.data['id'] + ' deleted')
