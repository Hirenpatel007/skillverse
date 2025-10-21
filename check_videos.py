#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillverse.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from courses.models import YouTubeVideo

print("✅ VIDEO LIBRARY DIAGNOSTIC")
print("=" * 60)

videos = YouTubeVideo.objects.all()
active_videos = YouTubeVideo.objects.filter(is_active=True)
free_videos = YouTubeVideo.objects.filter(is_free=True)

print(f"Total Videos in Database: {videos.count()}")
print(f"Active Videos: {active_videos.count()}")
print(f"Free Videos: {free_videos.count()}")
print()

if videos.exists():
    print("✅ VIDEOS FOUND! Sample Videos:")
    print("-" * 60)
    for i, v in enumerate(videos[:5], 1):
        print(f"{i}. {v.title}")
        print(f"   Video ID: {v.video_id}")
        print(f"   Category: {v.category}")
        print(f"   Level: {v.level}")
        print(f"   Duration: {v.duration}")
        print(f"   Active: {v.is_active}, Free: {v.is_free}")
        print()
else:
    print("❌ NO VIDEOS IN DATABASE!")
    print("Run this command to load videos:")
    print("  python manage.py load_free_videos")
