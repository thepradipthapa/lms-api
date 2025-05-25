from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, CourseSerializer, TagSerializer
from .models import Category, Course, Tag

# Create your views here.
class CategoryViewSet(ModelViewSet):
    """ ViewSet for handling Category operations. """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
  
class CourseViewSet(ModelViewSet):
    """ ViewSet for handling Course operations. """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class TagViewSet(ModelViewSet):
    """ ViewSet for handling Tag operations. """
    serializer_class = TagSerializer
    queryset = Tag.objects.all()  



