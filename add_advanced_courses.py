import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillverse.settings')
django.setup()

from courses.models import YouTubeVideo

# Add advanced DevOps, AI, ML, MLOps courses
advanced_videos = [
    # DevOps & Cloud
    (30, "AI Assisted DevOps Zero to Hero", "AI & DevOps Toolkit", "0RBEw_fBkys", "DevOps/AI", "Intermediate", "Complete AI-powered DevOps workflow"),
    (31, "Transforming DevOps with AI and ML", "DevOps Cloud and AI Labs", "PklN6N5N8bE", "DevOps/AI", "Intermediate", "AI integration in DevOps practices"),
    (32, "DevOps Full Course 2025 for Beginners", "DevOps Cloud and AI Labs", "WYsVdw3KJUo", "DevOps", "Beginner", "Modern DevOps practices and tools"),
    (33, "Fundamentals of AI Assisted DevOps", "AI & DevOps Toolkit", "gT8j_w0SIKE", "DevOps/AI", "Intermediate", "Demo and best practices for AI DevOps"),
    
    # MLOps & Machine Learning
    (34, "Learn MLOps In Simple Way - EP 1", "KAUSTUBH SHARMA", "BoZvNNSkMEI", "MLOps", "Beginner", "Introduction to Machine Learning Operations"),
    (35, "MLOps Course - Build ML Production Projects", "KAUSTUBH SHARMA", "AvJ3n5LhGEU", "MLOps", "Intermediate", "Production-grade ML project implementation"),
    (36, "Complete Machine Learning In 6 Hours", "Krish Naik", "WcqvqelSqkI", "Machine Learning", "Beginner", "Comprehensive ML fundamentals crash course"),
    
    # AIOps & Advanced AI
    (37, "AIOps School - AI for IT Operations", "AIOps School", "PK2pQCKwAHE", "AIOps", "Intermediate", "Artificial Intelligence for IT operations"),
    (38, "DAY-5 AI Assisted DevOps - AIOps Explained", "AI & DevOps Toolkit", "C4J7G-4R8fI", "AIOps", "Intermediate", "AIOps with free playgrounds and demos"),
    
    # AI Engineering & GenAI for DevOps
    (39, "DAY-3 Gen-AI Project For DevOps Engineers", "AI & DevOps Toolkit", "m7lB4j-gEqM", "AI/GenAI", "Advanced", "Generative AI applications for DevOps"),
    (40, "AI Engineering For DevOps and Platform", "AI & DevOps Toolkit", "Q8Z-4hL2vE0", "AI Engineering", "Advanced", "AI engineering principles for cloud platforms"),
]

print("=" * 80)
print("🚀 ADDING ADVANCED COURSES TO SKILLVERSE")
print("=" * 80)

added_count = 0
for vid_id, title, channel, video_id, category, level, description in advanced_videos:
    try:
        # Check if video already exists
        if YouTubeVideo.objects.filter(id=vid_id).exists():
            print(f"⚠️  Video {vid_id} already exists, skipping...")
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
        print(f"✅ Added Video {vid_id}: {title[:50]}")
        added_count += 1
    except Exception as e:
        print(f"❌ Error adding video {vid_id}: {str(e)}")

print("\n" + "=" * 80)
print(f"✅ Successfully added {added_count} advanced courses!")
print("=" * 80)

# Show updated stats
all_videos = YouTubeVideo.objects.all()
print(f"\n📊 UPDATED PLATFORM STATISTICS:")
print(f"   Total Videos: {all_videos.count()}")
print(f"   Free Videos: {all_videos.filter(is_free=True).count()}")
print(f"   Active Videos: {all_videos.filter(is_active=True).count()}")
print(f"   Categories: {all_videos.values('category').distinct().count()}")
print(f"   Channels: {all_videos.values('channel').distinct().count()}")

# Show new categories
print(f"\n🎓 NEW ADVANCED CATEGORIES ADDED:")
new_categories = ["DevOps/AI", "MLOps", "AIOps", "AI Engineering", "AI/GenAI"]
for cat in new_categories:
    count = all_videos.filter(category=cat).count()
    if count > 0:
        print(f"   • {cat}: {count} courses")

print("\n" + "=" * 80)
print("✅ Advanced DevOps, AI, ML, MLOps courses added successfully!")
print("=" * 80)
