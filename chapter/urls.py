from django.urls import path
from .views import chapter_choice_view, video_platform_view, ChapterCreateView, ChapterListView

# base url : api/chapter
urlpatterns = [
    path('chapter-types/', chapter_choice_view, name='chapter-types'),
    path('video-platform/', video_platform_view, name='video-platform-choices'),
    path('', ChapterCreateView.as_view(), name='chapter-createview'),
    path('course/<str:course_id>', ChapterListView.as_view(), name='chapter-listview'),
]