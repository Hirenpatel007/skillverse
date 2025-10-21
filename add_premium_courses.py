import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillverse.settings')
django.setup()

from courses.models import YouTubeVideo

# Add premium beginner courses from CodeWithHarry and Apna College
premium_beginner_courses = [
    # CodeWithHarry - Programming Fundamentals
    (41, "Introduction to Programming & Python | Day #1", "CodeWithHarry", "xvIkp_lXnWY", "Python", "Beginner", "Start your programming journey with Python basics"),
    (42, "Introduction to Data Structures & Algorithms", "CodeWithHarry", "kVmD_39zEAQ", "DSA", "Beginner", "Learn DSA fundamentals from scratch"),
    (43, "Introduction to C++, Installing VS Code & g++", "CodeWithHarry", "a0AaWgtKQAU", "C++", "Beginner", "C++ setup and fundamentals"),
    (44, "C Language Tutorial for Beginners (With Notes)", "CodeWithHarry", "fsfy4kFyP5c", "C", "Beginner", "Complete C programming with notes"),
    (45, "JavaScript Tutorial (2024) for Beginners to Pro", "CodeWithHarry", "W6NZfCO5SIk", "JavaScript", "Beginner", "JavaScript complete guide 2024"),
    (46, "Your First HTML Website | Sigma Web Development", "CodeWithHarry", "BsDoLVMnmZs", "Web Development", "Beginner", "Build your first website with HTML"),
    
    # Apna College - Comprehensive Courses
    (47, "C Language Tutorial for Beginners", "Apna College", "irqbmMQckaU", "C", "Beginner", "Complete C programming tutorial"),
    (48, "HTML Tutorial for Beginners | Complete HTML", "Apna College", "qz0aGYrrlhU", "Web Development", "Beginner", "HTML fundamentals with notes and practice"),
    (49, "Introduction to Java Language | Lecture 1", "Apna College", "ntLJNY2jhN4", "Java", "Beginner", "Java programming fundamentals"),
    
    # Chai aur Code - MLOps & Advanced
    (50, "Introduction | Learn MLOps In Simple Way | EP 1", "Chai aur Code", "BoZvNNSkMEI", "MLOps", "Beginner", "MLOps fundamentals explained simply"),
]

print("=" * 100)
print("🚀 ADDING PREMIUM BEGINNER COURSES FROM CODEWITHHARRY & APNA COLLEGE")
print("=" * 100)

added_count = 0
duplicate_count = 0

for vid_id, title, channel, video_id, category, level, description in premium_beginner_courses:
    try:
        # Check if video already exists
        if YouTubeVideo.objects.filter(id=vid_id).exists():
            print(f"⚠️  Video {vid_id} already exists, skipping...")
            duplicate_count += 1
            continue
        
        video = YouTubeVideo.objects.create(
            id=vid_id,
            title=title,
            channel=channel,
            video_id=video_id,
            category=category,
            level=level,
            description=description,
            is_free=True,
            is_active=True,
            language="English"
        )
        print(f"✅ Added Video {vid_id}: {title[:70]}")
        added_count += 1
    except Exception as e:
        print(f"❌ Error adding video {vid_id}: {str(e)}")

print("\n" + "=" * 100)
print(f"✅ Successfully added {added_count} premium beginner courses!")
if duplicate_count > 0:
    print(f"⚠️  Skipped {duplicate_count} duplicate videos")
print("=" * 100)

# Show updated stats
all_videos = YouTubeVideo.objects.all()
print(f"\n📊 UPDATED PLATFORM STATISTICS:")
print(f"   ├─ Total Videos: {all_videos.count()}")
print(f"   ├─ Free Videos: {all_videos.filter(is_free=True).count()}")
print(f"   ├─ Active Videos: {all_videos.filter(is_active=True).count()}")
print(f"   ├─ Categories: {all_videos.values('category').distinct().count()}")
print(f"   └─ Channels: {all_videos.values('channel').distinct().count()}")

# Show channel statistics
print(f"\n📺 CHANNEL BREAKDOWN:")
from django.db.models import Count
top_channels = all_videos.values('channel').annotate(count=Count('id')).order_by('-count')
for i, item in enumerate(top_channels[:15], 1):
    print(f"   {i:2}. {item['channel'][:45]:45} : {item['count']:2} videos")

# Show category statistics
print(f"\n🎓 TOP CATEGORIES:")
top_categories = all_videos.values('category').annotate(count=Count('id')).order_by('-count')
for i, item in enumerate(top_categories[:15], 1):
    print(f"   {i:2}. {item['category'][:45]:45} : {item['count']:2} videos")

print("\n" + "=" * 100)
print("✅ Premium beginner courses added successfully!")
print(f"📊 Platform now has {all_videos.count()} high-quality free courses!")
print("=" * 100)
