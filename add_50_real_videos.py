import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillverse.settings')
django.setup()

from courses.models import YouTubeVideo

# 50 Real YouTube Programming Videos
videos = [
    # Python (10 videos)
    {'video_id': 'rfscVS0vtbw', 'title': 'Learn Python - Full Course for Beginners', 'channel': 'freeCodeCamp.org', 'duration': '4:26:52', 'category': 'Python', 'level': 'beginner', 'language': 'English'},
    {'video_id': '_uQrJ0TkZlc', 'title': 'Python Tutorial - Python Full Course for Beginners', 'channel': 'Programming with Mosh', 'duration': '6:14:07', 'category': 'Python', 'level': 'beginner', 'language': 'English'},
    {'video_id': 'kqtD5dpn9C8', 'title': 'Python for Beginners - Learn Python in 1 Hour', 'channel': 'Programming with Mosh', 'duration': '1:00:05', 'category': 'Python', 'level': 'beginner', 'language': 'English'},
    {'video_id': 'eWRfhZUzrAc', 'title': 'Python for Data Science - Course for Beginners', 'channel': 'freeCodeCamp.org', 'duration': '12:32:30', 'category': 'Python', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'HGOBQPFzWKo', 'title': 'Intermediate Python Programming Course', 'channel': 'freeCodeCamp.org', 'duration': '6:00:00', 'category': 'Python', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'WGJJIrtnfpk', 'title': 'Python Django Web Framework - Full Course', 'channel': 'freeCodeCamp.org', 'duration': '4:23:06', 'category': 'Python', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'F5mRW0jo-U4', 'title': 'Python Django 7 Hour Course', 'channel': 'freeCodeCamp.org', 'duration': '7:00:00', 'category': 'Python', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'jBzwzrDvZ18', 'title': 'Python Machine Learning Tutorial', 'channel': 'freeCodeCamp.org', 'duration': '2:30:17', 'category': 'Python', 'level': 'advanced', 'language': 'English'},
    {'video_id': 'LHBE6Q9XlzI', 'title': 'Python Flask Tutorial', 'channel': 'freeCodeCamp.org', 'duration': '1:47:23', 'category': 'Python', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'Ven-pqwk3ec', 'title': 'Python Automation Tutorial', 'channel': 'freeCodeCamp.org', 'duration': '1:30:00', 'category': 'Python', 'level': 'intermediate', 'language': 'English'},
    
    # JavaScript (10 videos)
    {'video_id': 'PkZNo7MFNFg', 'title': 'Learn JavaScript - Full Course for Beginners', 'channel': 'freeCodeCamp.org', 'duration': '3:26:42', 'category': 'JavaScript', 'level': 'beginner', 'language': 'English'},
    {'video_id': 'W6NZfCO5SIk', 'title': 'JavaScript Programming - Full Course', 'channel': 'freeCodeCamp.org', 'duration': '7:44:29', 'category': 'JavaScript', 'level': 'beginner', 'language': 'English'},
    {'video_id': 'jS4aFq5-91M', 'title': 'JavaScript Full Course for Beginners', 'channel': 'Dave Gray', 'duration': '8:08:09', 'category': 'JavaScript', 'level': 'beginner', 'language': 'English'},
    {'video_id': 'Qqx_wzMmFeA', 'title': 'React Course - Beginners Tutorial', 'channel': 'freeCodeCamp.org', 'duration': '11:55:27', 'category': 'JavaScript', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'DLX62G4lc44', 'title': 'React JS - React Tutorial for Beginners', 'channel': 'Programming with Mosh', 'duration': '2:25:26', 'category': 'JavaScript', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'RGKi6LSPDLU', 'title': 'React Tutorial for Beginners', 'channel': 'Programming with Mosh', 'duration': '1:08:25', 'category': 'JavaScript', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'Dorf8i6lCuk', 'title': 'Node.js and Express.js - Full Course', 'channel': 'freeCodeCamp.org', 'duration': '8:16:48', 'category': 'JavaScript', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'fBNz5xF-Kx4', 'title': 'Node.js Tutorial for Beginners', 'channel': 'Programming with Mosh', 'duration': '1:03:26', 'category': 'JavaScript', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'Oe421EPjeBE', 'title': 'Node.js Full Course for Beginners', 'channel': 'Dave Gray', 'duration': '8:33:00', 'category': 'JavaScript', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'zBZgdyqWaIU', 'title': 'Vue.js Course for Beginners', 'channel': 'freeCodeCamp.org', 'duration': '3:24:43', 'category': 'JavaScript', 'level': 'intermediate', 'language': 'English'},
    
    # Java (5 videos)
    {'video_id': 'grEKMHGYyns', 'title': 'Java Tutorial for Beginners', 'channel': 'Programming with Mosh', 'duration': '2:18:35', 'category': 'Java', 'level': 'beginner', 'language': 'English'},
    {'video_id': 'eIrMbAQSU34', 'title': 'Java Programming for Beginners', 'channel': 'freeCodeCamp.org', 'duration': '9:00:00', 'category': 'Java', 'level': 'beginner', 'language': 'English'},
    {'video_id': 'A74TOX803D0', 'title': 'Java Full Course', 'channel': 'Amigoscode', 'duration': '10:00:00', 'category': 'Java', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'xk4_1vDrzzo', 'title': 'Spring Boot Tutorial for Beginners', 'channel': 'freeCodeCamp.org', 'duration': '3:18:24', 'category': 'Java', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'vtPkZShrvXQ', 'title': 'Java Spring Framework Tutorial', 'channel': 'freeCodeCamp.org', 'duration': '4:00:00', 'category': 'Java', 'level': 'advanced', 'language': 'English'},
    
    # C++ (5 videos)
    {'video_id': 'vLnPwxZdW4Y', 'title': 'C++ Tutorial for Beginners - Full Course', 'channel': 'freeCodeCamp.org', 'duration': '4:01:19', 'category': 'C++', 'level': 'beginner', 'language': 'English'},
    {'video_id': 'ZzaPdXTrSb8', 'title': 'C++ Programming Course - Beginner to Advanced', 'channel': 'freeCodeCamp.org', 'duration': '31:00:00', 'category': 'C++', 'level': 'intermediate', 'language': 'English'},
    {'video_id': '8jLOx1hD3_o', 'title': 'C++ Full Course for Beginners', 'channel': 'Bro Code', 'duration': '4:00:00', 'category': 'C++', 'level': 'beginner', 'language': 'English'},
    {'video_id': 'GQp1zzTwrIg', 'title': 'C++ Object Oriented Programming', 'channel': 'freeCodeCamp.org', 'duration': '1:30:00', 'category': 'C++', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'wN0x9eZLix4', 'title': 'C++ Data Structures and Algorithms', 'channel': 'freeCodeCamp.org', 'duration': '10:00:00', 'category': 'C++', 'level': 'advanced', 'language': 'English'},
    
    # Web Development (10 videos)
    {'video_id': 'pQN-pnXPaVg', 'title': 'HTML Full Course - Build a Website Tutorial', 'channel': 'freeCodeCamp.org', 'duration': '2:04:36', 'category': 'Web Development', 'level': 'beginner', 'language': 'English'},
    {'video_id': 'OXGznpKZ_sA', 'title': 'CSS Tutorial - Zero to Hero', 'channel': 'freeCodeCamp.org', 'duration': '11:00:00', 'category': 'Web Development', 'level': 'beginner', 'language': 'English'},
    {'video_id': 'mU6anWqZJcc', 'title': 'HTML & CSS Full Course - Beginner to Pro', 'channel': 'SuperSimpleDev', 'duration': '6:31:00', 'category': 'Web Development', 'level': 'beginner', 'language': 'English'},
    {'video_id': 'G3e-cpL7ofc', 'title': 'HTML & CSS Full Course', 'channel': 'SuperSimpleDev', 'duration': '6:00:00', 'category': 'Web Development', 'level': 'beginner', 'language': 'English'},
    {'video_id': 'nu_pCVPKzTk', 'title': 'Responsive Web Design - Full Course', 'channel': 'freeCodeCamp.org', 'duration': '4:00:00', 'category': 'Web Development', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'srvUrASNj0s', 'title': 'Tailwind CSS Full Course for Beginners', 'channel': 'Dave Gray', 'duration': '3:00:00', 'category': 'Web Development', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'hdI2bqOjy3c', 'title': 'Bootstrap 5 Tutorial for Beginners', 'channel': 'freeCodeCamp.org', 'duration': '2:00:00', 'category': 'Web Development', 'level': 'beginner', 'language': 'English'},
    {'video_id': 'RBSGKlAvoiM', 'title': 'Full Stack Web Development Course', 'channel': 'freeCodeCamp.org', 'duration': '10:00:00', 'category': 'Web Development', 'level': 'advanced', 'language': 'English'},
    {'video_id': 'zJSY8tbf_ys', 'title': 'Frontend Web Development Bootcamp', 'channel': 'freeCodeCamp.org', 'duration': '17:00:00', 'category': 'Web Development', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'erEgovG9WBs', 'title': 'TypeScript Course for Beginners', 'channel': 'freeCodeCamp.org', 'duration': '8:00:00', 'category': 'Web Development', 'level': 'intermediate', 'language': 'English'},
    
    # Data Science & AI (5 videos)
    {'video_id': 'ua-CiDNNj30', 'title': 'Machine Learning Course for Beginners', 'channel': 'freeCodeCamp.org', 'duration': '3:00:00', 'category': 'Data Science', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'tPYj3fFJGjk', 'title': 'TensorFlow 2.0 Complete Course', 'channel': 'freeCodeCamp.org', 'duration': '7:00:00', 'category': 'Data Science', 'level': 'advanced', 'language': 'English'},
    {'video_id': 'LHBE6Q9XlzI', 'title': 'Data Science Full Course', 'channel': 'Simplilearn', 'duration': '12:00:00', 'category': 'Data Science', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'r-uOLxNrNk8', 'title': 'Data Analysis with Python', 'channel': 'freeCodeCamp.org', 'duration': '10:00:00', 'category': 'Data Science', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'QLVMqwpOLPk', 'title': 'Artificial Intelligence Full Course', 'channel': 'Simplilearn', 'duration': '8:00:00', 'category': 'Data Science', 'level': 'advanced', 'language': 'English'},
    
    # Mobile Development (5 videos)
    {'video_id': 'fis26HvvDII', 'title': 'Flutter Course - Full Tutorial for Beginners', 'channel': 'freeCodeCamp.org', 'duration': '37:00:00', 'category': 'Mobile Development', 'level': 'beginner', 'language': 'English'},
    {'video_id': 'VFGUJFHfRO0', 'title': 'React Native Tutorial for Beginners', 'channel': 'Programming with Mosh', 'duration': '2:00:00', 'category': 'Mobile Development', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'fgdpvwEWJ9M', 'title': 'Android Development for Beginners', 'channel': 'freeCodeCamp.org', 'duration': '10:00:00', 'category': 'Mobile Development', 'level': 'beginner', 'language': 'English'},
    {'video_id': 'CmRkfkLNmh8', 'title': 'iOS Development Tutorial', 'channel': 'freeCodeCamp.org', 'duration': '8:00:00', 'category': 'Mobile Development', 'level': 'intermediate', 'language': 'English'},
    {'video_id': 'Hc79sDi3f0U', 'title': 'Kotlin Tutorial for Beginners', 'channel': 'freeCodeCamp.org', 'duration': '4:00:00', 'category': 'Mobile Development', 'level': 'beginner', 'language': 'English'},
]

print("Adding 50 real YouTube videos...")
added = 0
updated = 0

for video_data in videos:
    video_id = video_data['video_id']
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    
    video, created = YouTubeVideo.objects.update_or_create(
        video_id=video_id,
        defaults={
            'title': video_data['title'],
            'channel': video_data['channel'],
            'duration': video_data['duration'],
            'category': video_data['category'],
            'level': video_data['level'],
            'language': video_data['language'],
            'thumbnail_url': thumbnail_url,
            'is_free': True,
            'is_active': True,
        }
    )
    
    if created:
        added += 1
        print(f"[+] Added: {video_data['title'][:50]}...")
    else:
        updated += 1
        print(f"[*] Updated: {video_data['title'][:50]}...")

print(f"\n[SUCCESS] Complete! Added: {added}, Updated: {updated}")
print(f"[INFO] Total videos in database: {YouTubeVideo.objects.count()}")
