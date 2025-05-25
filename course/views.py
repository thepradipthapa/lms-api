from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class CategoryViewSet(ModelViewSet):
    """ ViewSet for handling Category operations. """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
  


