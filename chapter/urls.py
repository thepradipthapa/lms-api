from django.urls import path
from .views import chapter_choice_view, video_platform_view

# base url : api/chapter
urlpatterns = [
    path('chapter-choices/', chapter_choice_view, name='chapter-choices'),
    path('video-platform/', video_platform_view, name='video-platform-choices'),
]
 