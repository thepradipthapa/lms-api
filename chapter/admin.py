from django.contrib import admin
from .models import Chapter, LinkChapter, TextChapter, VideoChapter

# Register your models here.
admin.site.register(Chapter)
admin.site.register(LinkChapter)
admin.site.register(TextChapter)
admin.site.register(VideoChapter)