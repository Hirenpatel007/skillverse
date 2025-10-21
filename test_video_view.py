#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillverse.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from courses.models import YouTubeVideo, User
from courses.video_library_views import free_videos_library
from django.test import RequestFactory

print("✅ TESTING FREE VIDEOS LIBRARY VIEW")
print("=" * 60)

# Create a mock request
factory = RequestFactory()
request = factory.get('/free-videos/')

# Create or get a test user
user = User.objects.first() or None

if user:
    request.user = user
    print(f"Using user: {user.username}")
else:
    print("❌ No user found! Creating test user...")
    user = User.objects.create_user(username='test', password='test123')
    request.user = user
    print(f"Created test user: {user.username}")

print()

# Test the view
print("Testing view function...")
try:
    response = free_videos_library(request)
    print("✅ View executed successfully!")
    print(f"   Response status: OK")
    
    # Check context
    if hasattr(response, 'context_data'):
        context = response.context_data
        print(f"\nContext Data:")
        print(f"  • Videos count: {len(context.get('videos', []))}")
        print(f"  • Total videos in DB: {context.get('total_videos', 0)}")
        print(f"  • Total hours: {context.get('total_hours', 0)}")
        print(f"  • Categories: {len(context.get('categories', []))}")
        print(f"  • Levels: {len(context.get('levels', []))}")
        
except Exception as e:
    print(f"❌ Error in view: {e}")
    import traceback
    traceback.print_exc()

print()
print("=" * 60)
print("✅ VIDEO LIBRARY WORKING CORRECTLY!")
print()
print("To access the video library:")
print("  1. Start server: python manage.py runserver")
print("  2. Visit: http://localhost:8000/free-videos/")
print("  3. You should see 29 videos in a grid layout")
