from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    SOURCE_CHOICES = [
        ('internal', 'Internal'),
        ('coursera', 'Coursera'),
        ('udemy', 'Udemy'),
        ('youtube', 'YouTube'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default='internal')
    url = models.URLField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    thumbnail = models.URLField(blank=True)
    category = models.CharField(max_length=100, default='General')
    duration = models.CharField(max_length=50, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'course']


class YouTubeVideo(models.Model):
    """Model for free YouTube coding videos"""
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    
    video_id = models.CharField(max_length=20, unique=True)  # YouTube ID
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    channel = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)  # Format: HH:MM:SS
    category = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
    language = models.CharField(max_length=50, default='English')
    thumbnail_url = models.URLField(blank=True)
    is_free = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-added_date']
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['level']),
        ]

    def __str__(self):
        return f"{self.title} ({self.video_id})"


class VideoCompletion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=20)  # YouTube ID: dQw4w9WgXcQ
    completed_at = models.DateTimeField(auto_now_add=True)
    certificate_path = models.FileField(upload_to='certs/', blank=True, null=True)

    class Meta:
        unique_together = ('user', 'video_id')  # Prevent duplicate completions

    def __str__(self):
        return f"{self.user.username} - {self.video_id}"


class UserUpload(models.Model):
    """User uploaded resources - notes, PDFs, images, videos"""
    FILE_TYPES = [
        ('note', 'Note'),
        ('pdf', 'PDF'),
        ('image', 'Image'),
        ('video', 'Video'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='uploads/%Y/%m/')
    file_type = models.CharField(max_length=20, choices=FILE_TYPES)
    category = models.CharField(max_length=100, blank=True)
    is_public = models.BooleanField(default=True)
    downloads = models.IntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.title} by {self.user.username}"
