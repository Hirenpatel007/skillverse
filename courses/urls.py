from django.urls import path
from . import views
from .video_library_views import (
    free_videos_library,
    video_player,
    videos_by_category,
    videos_by_level,
    video_api_search,
    get_video_stats,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('courses/', views.courses_view, name='courses'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('courses/<int:pk>/enroll/', views.enroll_course, name='enroll_course'),
    path('jobs/', views.jobs_view, name='jobs'),
    path('learning-paths/', views.learning_paths_view, name='learning_paths'),
    path('subscriptions/', views.subscriptions_view, name='subscriptions'),
    path('profile/', views.profile_view, name='profile'),
    
    # Certificate System URLs
    path('api/complete-video/', views.complete_video, name='complete_video'),
    path('certificate/<int:cert_id>/download/', views.download_certificate, name='download_certificate'),
    path('certificate/<int:cert_id>/view/', views.view_certificate, name='view_certificate'),
    path('certificates/', views.user_certificates, name='user_certificates'),
    
    # Free Video Library URLs
    path('free-videos/', free_videos_library, name='free_videos_library'),
    path('watch/<str:video_id>/', video_player, name='video_player'),
    path('videos/category/<str:category>/', videos_by_category, name='videos_by_category'),
    path('videos/level/<str:level>/', videos_by_level, name='videos_by_level'),
    
    # API Endpoints
    path('api/videos/search/', video_api_search, name='video_api_search'),
    path('api/videos/stats/', get_video_stats, name='video_stats'),
    
    # Upload & Sharing Platform
    path('upload/', views.upload_resource, name='upload_resource'),
    path('sharing/', views.sharing_platform, name='sharing_platform'),
    path('my-uploads/', views.my_uploads, name='my_uploads'),
    path('download/<int:pk>/', views.download_resource, name='download_resource'),
    path('delete-upload/<int:pk>/', views.delete_upload, name='delete_upload'),
]
