from django.shortcuts import render
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import CategorySerializer, CourseSerializer, TagSerializer
from .models import Category, Course, Tag
from core.permissions import IsAdminOrReadOnly

# Create your views here.
class CategoryViewSet(ModelViewSet):
    """ ViewSet for handling Category operations. """
    permission_classes = [IsAdminOrReadOnly]  
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetailbySlugView(RetrieveUpdateDestroyAPIView):
    """ View for retrieving, updating, or deleting a category by its slug. """
    permission_classes = [IsAdminOrReadOnly]  
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'
  
class CourseViewSet(ModelViewSet):
    """ ViewSet for handling Course operations. """
    permission_classes = [IsAdminOrReadOnly]  
    serializer_class = CourseSerializer
    search_fields = ['title', 'description', 'tagline', 'slug']
    filterset_fields = ['category', 'slug', 'price']
    ordering_fields = '__all__'

    queryset = Course.objects.all()

    def get_queryset(self):
        """ Override the get_queryset method to filter courses by tag if provided. """
        tag = self.request.query_params.get('tag')
        if tag is not None:
            courseids = Tag.objects.filter(title=tag).values_list('course')
            return Course.objects.filter(id__in=courseids)
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        """ Override the create method to handle custom logic. """
        course = request.data
        category = course.get('category')
        if category is None:
            return Response(
                {"error": "Category is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )  
        try:
            category = Category.objects.get(id=category)

        except (ValidationError, Category.DoesNotExist):
            return Response(
                {"error": "Invalid category ID"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = CourseSerializer(data=course)
        if serializer.is_valid():
            instance = Course(**serializer.validated_data, category=category)
            instance.save()
            return Response(
                serializer.data , 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors)
        
class CourseDetailbySlugView(RetrieveUpdateDestroyAPIView):
    """ View for retrieving, updating, or deleting a course by its slug. """
    permission_classes = [IsAdminOrReadOnly]  
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'slug'

class CourseByCategoryView(APIView):

    """ View for retrieving courses by category id. """
    permission_classes = [IsAdminOrReadOnly]  

    def get(self, request, category_id):
        """ Handle GET requests to retrieve courses by category id. """
        try:
            category = Category.objects.get(id=category_id)
        except (ValidationError, Category.DoesNotExist):
            return Response(
                {"error": "Invalid category ID"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        courses = Course.objects.filter(category=category)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TagViewSet(ModelViewSet):
    """ ViewSet for handling Tag operations. """
    permission_classes = [IsAdminOrReadOnly]  
    serializer_class = TagSerializer
    queryset = Tag.objects.all()  

    def create(self, request, *args, **kwargs):
        """ Override the create method to handle custom logic. """
        tag = request.data
        course = tag.get('course')
        if course is None:
            return Response(
                {"error": "Course is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )  
        try:
            course = Course.objects.get(id=course)

        except (ValidationError, Course.DoesNotExist):
            return Response(
                {"error": "Invalid course ID"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = TagSerializer(data=tag)
        if serializer.is_valid():
            instance = Tag(**serializer.validated_data, course=course)
            instance.save()
            return Response(
                serializer.data , 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors)



