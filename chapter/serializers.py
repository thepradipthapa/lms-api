from chapter.models import Chapter, TextChapter, VideoChapter, LinkChapter, HeadingChapter
from rest_framework.serializers import ModelSerializer


class ChapterSerializer(ModelSerializer):
    """ Serializer for the Chapter model. """
    
    class Meta:
        model = Chapter
        fields = '__all__'

class TextChapterSerializer(ModelSerializer):
    """ Serializer for the TextChapter model. """
    
    class Meta:
        model = TextChapter
        fields = '__all__' 

class VideoChapterSerializer(ModelSerializer):
    """ Serializer for the VideoChapter model. """
    
    class Meta:
        model = VideoChapter
        fields = '__all__'

class LinkChapterSerializer(ModelSerializer):
    """ Serializer for the LinkChapter model. """
    
    class Meta:
        model = LinkChapter
        fields = '__all__'

class HeadingChapterSerializer(ModelSerializer):
    """ Serializer for the HeadingChapter model. """
    
    class Meta:
        model = HeadingChapter
        fields = '__all__'
