from django.contrib import admin
from .models import Course, Category, Tag

# Register models here.
admin.site.register(Course)
admin.site.register(Category) 
admin.site.register(Tag)