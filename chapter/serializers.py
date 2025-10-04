from chapter.models import Chapter, TextChapter, VideoChapter, LinkChapter, HeadingChapter
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class TextChapterSerializer(ModelSerializer):
    """ Serializer for the TextChapter model. """

    # making lecture optional in API request.
    chapter = serializers.UUIDField(required=False)
    
    class Meta:
        model = TextChapter
        fields = '__all__' 
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('chapter', None)
        return data  # Returns the full dictionary without 'chapter'


class VideoChapterSerializer(ModelSerializer):
    """ Serializer for the VideoChapter model. """
    
    
    # making lecture optional in API request.
    chapter = serializers.UUIDField(required=False)

    class Meta:
        model = VideoChapter
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('chapter', None)
        return data  # Returns the full dictionary without 'chapter'


class LinkChapterSerializer(ModelSerializer):
    """ Serializer for the LinkChapter model. """
    
    
    # making lecture optional in API request.
    chapter = serializers.UUIDField(required=False)

    class Meta:
        model = LinkChapter
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('chapter', None)
        return data  # Returns the full dictionary without 'chapter'


class HeadingChapterSerializer(ModelSerializer):
    """ Serializer for the HeadingChapter model. """

    
    # making lecture optional in API request.
    chapter = serializers.UUIDField(required=False)
    
    class Meta:
        model = HeadingChapter
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('chapter', None)
        return data  # Returns the full dictionary without 'chapter'



class ChildChapterSerializer(ModelSerializer):
    """ Serializer for the Chapter model. """
    index = serializers.IntegerField(required=False)
    heading_chapter = HeadingChapterSerializer(read_only=True)
    link_chapter = LinkChapterSerializer(read_only=True)
    text_chapter = TextChapterSerializer(read_only=True)
    video_chapter = VideoChapterSerializer(read_only=True)

    class Meta:
        model = Chapter
        fields = '__all__'

class ChapterSerializer(ModelSerializer):
    """ Serializer for the Chapter model. """
    index = serializers.IntegerField(required=False)
    heading_chapter = HeadingChapterSerializer(read_only=True)
    link_chapter = LinkChapterSerializer(read_only=True)
    text_chapter = TextChapterSerializer(read_only=True)
    video_chapter = VideoChapterSerializer(read_only=True)
    subchapters = ChildChapterSerializer(many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = '__all__'

    # overwrite Create() Method
    def create(self, validated_data):
        data = self.context.get('request').data
        chapter_type = data.get('chapter_type')
        chapter_type_object = None
        parent_chapter = validated_data.get('parent_chapter')

        if chapter_type == 'H':
            chapter_type_object = self.HandleHeadingChapter(data)

        if chapter_type == 'T':
            chapter_type_object = self.HandleTextChapter(data)

        if chapter_type == 'V':
            chapter_type_object = self.HandleVideoChapter(data)

        if chapter_type == 'L':
            chapter_type_object = self.HandleLinkChapter(data)

        chapter = Chapter(**validated_data)
        course = chapter.course

        if chapter.parent_chapter is None:
            # If the chapter is a root chapter, set its index to the next available index
            chapter.index = Chapter.objects.filter(course=course, parent_chapter=None).count() + 1
            chapter.save()
            chapter_type_object.chapter = chapter
            chapter_type_object.save()
        else:
            # If the chapter is a sub-chapter, set its index to the next available index under its parent
            chapter.index = Chapter.objects.filter(parent_chapter=parent_chapter).count() + 1
            chapter.save()
            chapter_type_object.chapter = chapter
            chapter_type_object.save()
        return chapter

    def HandleHeadingChapter(self, raw_json):
        # Handle the creation of a HeadingChapter instance
        heading_chapter_raw = raw_json.get('heading_chapter')
        if not heading_chapter_raw:
            raise ValidationError({"heading_chapter": ["heading_chapter is required"]})

        heading_chapter_serializer = HeadingChapterSerializer(data=heading_chapter_raw)

        if heading_chapter_serializer.is_valid():
            return HeadingChapter(**heading_chapter_serializer.validated_data)
        else:
            raise ValidationError({"heading_chapter": heading_chapter_serializer.errors})
        
    def HandleTextChapter(self, raw_json):
        # Handle the creation of a TextChapter instance
        text_chapter_raw = raw_json.get('text_chapter')
        if not text_chapter_raw:
            raise ValidationError({"text_chapter": ["text_chapter is required"]})

        text_chapter_serializer = TextChapterSerializer(data=text_chapter_raw)

        if text_chapter_serializer.is_valid():
            return TextChapter(**text_chapter_serializer.validated_data)
        else:
            raise ValidationError({"text_chapter": text_chapter_serializer.errors})
        
    def HandleVideoChapter(self, raw_json):
        # Handle the creation of a VideoChapter instance
        video_chapter_raw = raw_json.get('video_chapter')
        if not video_chapter_raw:
            raise ValidationError({"video_chapter": ["video_chapter is required"]})

        video_chapter_serializer = VideoChapterSerializer(data=video_chapter_raw)

        if video_chapter_serializer.is_valid():
            return VideoChapter(**video_chapter_serializer.validated_data)
        else:
            raise ValidationError({"video_chapter": video_chapter_serializer.errors})
        
    def HandleLinkChapter(self, raw_json):
        # Handle the creation of a LinkChapter instance
        link_chapter_raw = raw_json.get('link_chapter')
        if not link_chapter_raw:
            raise ValidationError({"link_chapter": ["link_chapter is required"]})

        link_chapter_serializer = LinkChapterSerializer(data=link_chapter_raw)

        if link_chapter_serializer.is_valid():
            return LinkChapter(**link_chapter_serializer.validated_data)
        else:
            raise ValidationError({"link_chapter": link_chapter_serializer.errors})