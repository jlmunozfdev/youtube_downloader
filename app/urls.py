from django.urls import path
from app.views import download_video

urlpatterns = [
    path('', download_video, name='download_video'),
]