from rest_framework.decorators import api_view
from rest_framework.response import Response
from chapter.models import chapter_choices, chapter_choices_description, video_platform_choices

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