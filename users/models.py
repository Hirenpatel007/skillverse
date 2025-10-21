from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.TextField(blank=True, help_text='Comma-separated skills')
    career_goal = models.CharField(max_length=200, blank=True)
    experience_level = models.CharField(max_length=50, default='beginner')
    subscription_plan = models.CharField(max_length=20, default='free')
    subscription_end = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.URLField(blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username

class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=10, default='🏆')
    earned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"
