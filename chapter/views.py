from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from chapter.models import chapter_choices, chapter_choices_description, video_platform_choices, Chapter
import course
from .serializers import ChapterSerializer 
from rest_framework.permissions import IsAdminUser
from core.permissions import IsAdminOrReadOnly
from course.models import Course
import uuid
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def chapter_choice_view(request):
    """ Returns chapter choices. """
    def searchDescription(id):
        """ Searches for the description of the chapter type. """
        for _id, description in chapter_choices_description:
            if id == _id :
                return description
    def changeToDict(choice_tuple):
        """ Converts tuple to dictionary. """
        return {
            'id': choice_tuple[0], 
            'type': choice_tuple[1],
            'description': searchDescription(choice_tuple[0])
        }
    return Response(list(map(changeToDict, chapter_choices)))


@api_view(['GET'])
def video_platform_view(request):
    """ Returns video platform choices. """
    platform = map(lambda choice: dict(id=choice[0], platform=choice[1]),
                   video_platform_choices)
    return Response(platform)



class ChapterListView(ListAPIView):
    """ Return Chapter list """
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    ordering_fields = ['index']

    def get(self, request, *args, **kwargs):
        try:
            course = self.kwargs.get('course_id')
            uuid.UUID(course)
        except:
            return Response(
                {"course": ["Invalid course ID"]}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        course = self.kwargs.get('course_id')
        return Chapter.objects.filter(parent_chapter=None, course=Course(pk=course))


class ChapterCreateView(CreateAPIView):
    """ create chapter. """
    permission_classes = [IsAdminUser]
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


    def get_serializer(self, *args, **kwargs):
        # passing extra context to the serializer 
        serializer =  self.serializer_class(data=self.request.data, context={'request': self.request})
        serializer.is_valid()
        return serializer
    


    
