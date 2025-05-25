from .models import Category, Course, Tag
from rest_framework.serializers import ModelSerializer

class CategorySerializer(ModelSerializer):
    """ Serializer for the Category model. """
    
    class Meta:
        model = Category
        fields = '__all__'
        

class CourseSerializer(ModelSerializer):
    """ Serializer for the Course model. """
    
    class Meta:
        model = Course
        fields = '__all__'

class TagSerializer(ModelSerializer):
    """ Serializer for the Tag model. """
    
    class Meta:
        model = Tag
        fields = '__all__'

