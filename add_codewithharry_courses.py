import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillverse.settings')
django.setup()

from courses.models import YouTubeVideo

# Add CodeWithHarry courses (popular beginner-friendly channel)
codewithharry_videos = [
    # Web Development
    (41, "HTML Crash Course For Beginners", "CodeWithHarry", "qz0aGYrrlhU", "Web Development", "Beginner", "Complete HTML fundamentals in one video"),
    (42, "CSS Crash Course For Beginners", "CodeWithHarry", "Edsqc84hctY", "CSS", "Beginner", "CSS styling from basics to advanced"),
    (43, "JavaScript Tutorial for Beginners", "CodeWithHarry", "W6NZfCO5SIk", "JavaScript", "Beginner", "Complete JavaScript fundamentals"),
    (44, "Python Complete Course For Beginners", "CodeWithHarry", "7wnove7K-ZQ", "Python", "Beginner", "Python from zero to hero"),
    (45, "C Programming Tutorial", "CodeWithHarry", "irqbmMQckaU", "C", "Beginner", "C programming fundamentals"),
    (46, "C++ Programming Complete Course", "CodeWithHarry", "z9bC3xfqrj0", "C++", "Beginner", "C++ from basics to OOP"),
    (47, "Java Complete Course", "CodeWithHarry", "ntLJNY2jhN4", "Java", "Beginner", "Java programming fundamentals"),
    
    # Advanced Web Development
    (48, "React JS Tutorial for Beginners", "CodeWithHarry", "A1gaR66jYu0", "JavaScript/React", "Beginner", "React fundamentals and components"),
    (49, "Node.js Complete Course", "CodeWithHarry", "eIrMbAQSU34", "JavaScript/Node.js", "Beginner", "Backend development with Node.js"),
    (50, "MongoDB Complete Course", "CodeWithHarry", "oSIv-E60NiU", "Database/MongoDB", "Beginner", "NoSQL database with MongoDB"),
    
    # Advanced Topics
    (51, "Git & GitHub Tutorial", "CodeWithHarry", "apGV9Kg7ics", "Tools/Git", "Beginner", "Version control with Git and GitHub"),
    (52, "Web Development Full Course", "CodeWithHarry", "BsDoLVMnmZs", "Web Development", "Beginner", "Complete web development bootcamp"),
    (53, "Data Structures & Algorithms", "CodeWithHarry", "AT14lCcyHEF", "DSA", "Intermediate", "DSA with practical implementations"),
    (54, "Machine Learning Tutorial", "CodeWithHarry", "NqoXPBLO-8I", "Machine Learning", "Beginner", "ML fundamentals and applications"),
]

print("=" * 90)
print("🚀 ADDING CODEWITHHARRY COURSES TO SKILLVERSE")
print("=" * 90)

added_count = 0
duplicate_count = 0

for vid_id, title, channel, video_id, category, level, description in codewithharry_videos:
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
        print(f"✅ Added Video {vid_id}: {title[:60]}")
        added_count += 1
    except Exception as e:
        print(f"❌ Error adding video {vid_id}: {str(e)}")

print("\n" + "=" * 90)
print(f"✅ Successfully added {added_count} CodeWithHarry courses!")
if duplicate_count > 0:
    print(f"⚠️  Skipped {duplicate_count} duplicate videos")
print("=" * 90)

# Show updated stats
all_videos = YouTubeVideo.objects.all()
print(f"\n📊 UPDATED PLATFORM STATISTICS:")
print(f"   Total Videos: {all_videos.count()}")
print(f"   Free Videos: {all_videos.filter(is_free=True).count()}")
print(f"   Active Videos: {all_videos.filter(is_active=True).count()}")
print(f"   Categories: {all_videos.values('category').distinct().count()}")
print(f"   Channels: {all_videos.values('channel').distinct().count()}")

# Show CodeWithHarry course count
codewithharry_count = all_videos.filter(channel="CodeWithHarry").count()
print(f"\n📺 CodeWithHarry Courses Added: {codewithharry_count}")

# Top channels
print(f"\n🎓 TOP CHANNELS BY COURSE COUNT:")
from django.db.models import Count
top_channels = all_videos.values('channel').annotate(count=Count('id')).order_by('-count')[:10]
for item in top_channels:
    print(f"   • {item['channel'][:40]:40} : {item['count']:2} courses")

print("\n" + "=" * 90)
print("✅ CodeWithHarry comprehensive course collection added successfully!")
print("=" * 90)
