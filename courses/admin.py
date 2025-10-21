from django.contrib import admin
from .models import Course, Enrollment, VideoCompletion, YouTubeVideo, UserUpload

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'price', 'created_at']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'enrolled_at']

@admin.register(VideoCompletion)
class VideoCompletionAdmin(admin.ModelAdmin):
    list_display = ['user', 'video_id', 'completed_at', 'has_certificate']
    list_filter = ['completed_at', 'video_id']
    search_fields = ['user__username', 'video_id']
    readonly_fields = ['completed_at', 'certificate_path']
    
    def has_certificate(self, obj):
        return bool(obj.certificate_path)
    has_certificate.boolean = True
    has_certificate.short_description = 'Certificate Generated'

@admin.register(YouTubeVideo)
class YouTubeVideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'channel', 'category', 'level', 'duration', 'is_free', 'is_active']
    list_filter = ['category', 'level', 'is_free', 'is_active', 'language', 'added_date']
    search_fields = ['title', 'description', 'channel', 'video_id']
    readonly_fields = ['video_id', 'added_date', 'updated_date']
    
    fieldsets = (
        ('Video Information', {
            'fields': ('video_id', 'title', 'description', 'channel')
        }),
        ('Details', {
            'fields': ('category', 'level', 'language', 'duration')
        }),
        ('Media', {
            'fields': ('thumbnail_url', 'is_free', 'is_active')
        }),
        ('Metadata', {
            'fields': ('views', 'rating', 'added_date', 'updated_date'),
            'classes': ('collapse',)
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ['is_free']
        return self.readonly_fields


@admin.register(UserUpload)
class UserUploadAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'file_type', 'category', 'is_public', 'downloads', 'uploaded_at']
    list_filter = ['file_type', 'is_public', 'category', 'uploaded_at']
    search_fields = ['title', 'description', 'user__username']
    readonly_fields = ['uploaded_at', 'downloads']

