from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import CategorySerializer, CourseSerializer, TagSerializer
from .models import Category, Course, Tag

# Create your views here.
class CategoryViewSet(ModelViewSet):
    """ ViewSet for handling Category operations. """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetailbySlugView(RetrieveUpdateDestroyAPIView):
    """ View for retrieving, updating, or deleting a category by its slug. """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'
  
class CourseViewSet(ModelViewSet):
    """ ViewSet for handling Course operations. """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class CourseDetailbySlugView(RetrieveUpdateDestroyAPIView):
    """ View for retrieving, updating, or deleting a course by its slug. """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'slug'


class TagViewSet(ModelViewSet):
    """ ViewSet for handling Tag operations. """
    serializer_class = TagSerializer
    queryset = Tag.objects.all()  



