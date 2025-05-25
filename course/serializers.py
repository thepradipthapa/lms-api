from .models import Category
from rest_framework.serializers import ModelSerializer

class CategorySerializer(ModelSerializer):
    """ Serializer for the Category model. """
    
    class Meta:
        model = Category
        fields = '__all__'
        