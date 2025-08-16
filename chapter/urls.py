from django.urls import path
from .views import chapter_choice_view, video_platform_view, ChapterListCreateView

# base url : api/chapter
urlpatterns = [
    path('chapter-types/', chapter_choice_view, name='chapter-types'),
    path('video-platform/', video_platform_view, name='video-platform-choices'),
    path('', ChapterListCreateView.as_view(), name='chapter-listcreateview'),
]