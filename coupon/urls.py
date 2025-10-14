from django.urls import path, include
from coupon.views import CouponListView
from rest_framework.routers import DefaultRouter
from .views import CouponModelviewSet

coupon_router = DefaultRouter()
coupon_router.register("", CouponModelviewSet, basename='coupon' )


urlpatterns = [
    path('course/<str:course_id>/code/<str:code>/', CouponListView.as_view(), name='coupon-by-code'),
    path('',include(coupon_router.urls))
]
