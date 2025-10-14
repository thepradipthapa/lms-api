from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from core.views import api_root


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", api_root, name="api_root"),
    path('api/', include(('course.urls', 'course'), namespace='course')),
    path('api/chapters/', include(('chapter.urls', 'chapter'), namespace='chapter')),
    path('api/coupons/', include(('coupon.urls', 'coupon'), namespace='coupon')),
    path('api/review/', include('review.urls')),
    path('api/orders/', include('order.urls')),
    path('api/doubts/', include('doubt.urls')),
]
if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)