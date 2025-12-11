"""
URL configuration for Diploma project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from operator import index

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Hotel import views
from Hotel.views import HotelAPIView, HotelInfoAPIView, RoomAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("hotel/<int:hotel_id>/", views.hotel_info, name="hotel_info"),
    path('api/v1/hotels/', HotelAPIView.as_view()),
    path('api/v1/hotels/<int:pk>/', HotelInfoAPIView.as_view()),
    path('api/v1/rooms/', RoomAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)