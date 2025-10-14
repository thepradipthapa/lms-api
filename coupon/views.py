from django.shortcuts import render
from .serializers import CouponSerializer
from rest_framework.generics import ListAPIView
from .models import Coupon
from course.models import Course
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from uuid import UUID

# Create your views here.
class CouponListView(ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    def get(self, request, *args, **kwargs):
        code = self.kwargs.get('code')
        course_id= self.kwargs.get('course_id')
        try:
            UUID(course_id)
        except:
            return Response(
                {"course": ["course id is not valid"]}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        self.queryset=  self.queryset.filter(course=Course(pk=course_id), code=code, is_active=True)

        if len(self.queryset)==0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return super().get(request, *args, **kwargs)
    

class CouponModelviewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer




