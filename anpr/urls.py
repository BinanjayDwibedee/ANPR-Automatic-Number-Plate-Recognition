from django.urls import path
from .views import upload_video, video_result

urlpatterns = [
    path('', upload_video, name='upload_video'),
    path('video_result/<int:video_id>/', video_result, name='video_result'),
]
