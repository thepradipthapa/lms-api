from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from chapter.models import chapter_choices, chapter_choices_description, video_platform_choices, Chapter
from .serializers import ChapterSerializer 
from rest_framework.permissions import IsAdminUser
from core.permissions import IsAdminOrReadOnly

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


class ChapterListCreateView(ListCreateAPIView):
    """ Return chapter list and create chapter. """
    permission_classes = [IsAdminOrReadOnly]
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'POST':
            # passing extra context to the serializer 
            serializer =  self.serializer_class(data=self.request.data, context={'request': self.request})
            serializer.is_valid()
            return serializer
        return super().get_serializer(*args, **kwargs)