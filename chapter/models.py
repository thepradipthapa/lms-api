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

chapter_choices_description = (
    ('T', 'Text Chapter'),
    ('H', 'Heading Chapter'),
    ('V', 'Video Chapter'),
    ('L', 'Link Chapter'),
)

video_platform_choices = [
    ('Y', 'YOUTUBE'),
    ('V', 'VIMEO'),

]

class Chapter(models.Model):
    """ Represents a chapter in the course."""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='chapters'
    )

    chapter_type = models.CharField(
        max_length=2,
        choices=chapter_choices
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
    

    class Meta:
        verbose_name = "Chapter"
        verbose_name_plural = "Chapters"
        ordering = ['course', 'index']

class LinkChapter(models.Model):
    """ Represents a link chapter in the database."""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    lecture = models.OneToOneField(
        Chapter,
        on_delete=models.CASCADE,
        related_name='link_chapter'
    )
    title = models.CharField(max_length=50, null=False)
    url = models.URLField(max_length=200, null=False)

    class Meta:
        verbose_name = "Link Chapter"
        verbose_name_plural = "Link Chapters"

class TextChapter(models.Model):
    """ Represents a text chapter in the database."""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    lecture = models.OneToOneField(
        Chapter,
        on_delete=models.CASCADE,
        related_name='text_chapter'
    )
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(null=False)

    class Meta:
        verbose_name = "Text Chapter"
        verbose_name_plural = "Text Chapters"

class VideoChapter(models.Model):
    """ Represents a video chapter in the database."""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    lecture = models.OneToOneField(
        Chapter,
        on_delete=models.CASCADE,
        related_name='video_chapter'
    )
    title = models.CharField(max_length=50, null=False)
    video_id = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True)
    video_platform = models.CharField(
        max_length=2,
        choices=video_platform_choices,
    )
    class Meta:
        verbose_name = "Video Chapter"
        verbose_name_plural = "Video Chapters"

