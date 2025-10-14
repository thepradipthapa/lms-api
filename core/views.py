from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

# Create your views here.
@api_view(['GET'])
def api_root(request):
    """
    API root view that returns various API endpoints.
    """
    response = {
        "API root": reverse('api_root', request=request),

        "Course": {
            "Course List": reverse('course:course-list', request=request),
            "Course Detail": reverse('course:course-detail', kwargs={'pk': 'course-pk'}, request=request),
            "Course Detail By Slug": reverse('course:course-detail-by-slug', kwargs={'slug': 'course-slug'}, request=request),
            "Course  By Category Id": reverse('course:course-by-category', kwargs={'category_id': 'category-uuid'}, request=request),
    
        },
    
        "Category": {
            "Category List": reverse('course:category-list', request=request),
            "Category Detail": reverse('course:category-detail', kwargs={'pk': 'category-pk'}, request=request),
            "Category Detail By Slug": reverse('course:category-detail-by-slug', kwargs={'slug': 'category-slug'}, request=request),
        },

        "Tag": {
        "Tag list": reverse('course:tag-list', request=request),
        "Tag Detail": reverse('course:tag-detail', kwargs={'pk': 'tag-pk'}, request=request),
        },

        "Chapter": {
            "Chapter Types": reverse('chapter:chapter-types', request=request),
            "Video Plateform List": reverse('chapter:video-platform-choices', request=request),
            "Chapter Create": reverse('chapter:chapter-createview', request=request),
            "Chapter List": reverse('chapter:chapter-listview', kwargs={'course_id': 'course-uuid'}, request=request),
        },

         "Coupon": {
            "Coupon List": reverse('coupon:coupon-list', request=request),
            "Coupon Detail": reverse('coupon:coupon-detail', args=['pk'],request=request),
            "Coupon by Code": reverse('coupon:coupon-by-code', args=['course-id', 'code'], request=request),

        }
    }
    return Response(response)