from django.shortcuts import render, redirect
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.response import Response
from .models import NewsModel
from .serializers import NewsSerializer

class NewsListAPIView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = NewsSerializer
    queryset = NewsModel.objects.all()

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class NewsRetrieveAPIView(GenericAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = NewsSerializer
    queryset = NewsModel.objects.all()

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def patch(self, request, pk):
        return self.update(request, pk)
    
