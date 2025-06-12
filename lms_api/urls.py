"""
URL configuration for lms_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from core.views import api_root


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", api_root, name="api_root"),
     path('api/', include(('course.urls', 'course'), namespace='course')),
    path('api/chapters/', include('chapter.urls')),
    path('api/coupons/', include('coupon.urls')),
    path('api/review/', include('review.urls')),
    path('api/orders/', include('order.urls')),
    path('api/doubts/', include('doubt.urls')),
]
if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)