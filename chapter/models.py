from django.db import models
import uuid
from course.models import Course

# Create your models here.
chapter_choices = [
    ('T', 'TEXT'),
    ('H', 'HEADING'),
    ('V', 'VIDEO'),
    ('L', 'LINK'),
]

class Chapter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='chapters'
    )

    chapter_type = models.CharField(
        max_length=2,
        choices=chapter_choices,
        default='TEXT'
    )
    index = models.IntegerField(null=False)
    parent_chapter = models.ForeignKey(
        'Chapter',
        on_delete=models.CASCADE,
        related_name='subchapters',
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Chapter {self.index} - {self.chapter_type}"
    
