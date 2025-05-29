from django.db import models
import uuid

class Category(models.Model):
    """ Represents a category for organizing course in the database."""

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    slug = models.SlugField(null=False, unique=True)
    title = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

class Course(models.Model):
    """ Represents a course in the database."""

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=100, null=False)
    slug = models.SlugField(null=False, unique=True)
    instructor = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=1000, null=False)
    language = models.CharField(max_length=50, null=False)
    tagline = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    duration = models.IntegerField(null=False)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='courses'
    )
    thumbnail = models.ImageField(upload_to='course/thumbnails/', null=True)
    resourse = models.FileField(upload_to='course/resources/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['title']


class Tag(models.Model):
    """ Represents a tag for organizing courses in the database."""

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=20, null=False)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE, 
        related_name='tags'
    ) 

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ['title']