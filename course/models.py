from django.db import models
import uuid

class Category(models.Model):
    """ Represents a category for organizing coirses in the database."""

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    slug = models.SlugField()
    title = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

