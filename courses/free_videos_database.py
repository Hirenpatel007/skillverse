"""
Free YouTube Coding & Learning Videos Database
Complete list of high-quality, free YouTube videos for learning

Format:
- Video ID (YouTube's unique identifier)
- Title
- Channel
- Duration (approx)
- Language
- Category
- Level
"""

FREE_CODING_VIDEOS = [
    # ==========================================
    # PYTHON PROGRAMMING
    # ==========================================
    {
        'video_id': 'rfscVS0vtik',
        'title': 'Python for Beginners - Full Course',
        'channel': 'Programming with Mosh',
        'duration': '4:26:00',
        'language': 'English',
        'category': 'Python',
        'level': 'Beginner',
        'description': 'Complete beginner-friendly Python tutorial'
    },
    {
        'video_id': 'Ej_02ICOt7s',
        'title': 'Python Django Full Course',
        'channel': 'Traversy Media',
        'duration': '3:48:00',
        'language': 'English',
        'category': 'Python/Django',
        'level': 'Intermediate',
        'description': 'Learn Django framework for web development'
    },
    {
        'video_id': 'QJFQ9blHQVU',
        'title': 'Python OOP Tutorial',
        'channel': 'Tech with Tim',
        'duration': '1:20:00',
        'language': 'English',
        'category': 'Python',
        'level': 'Intermediate',
        'description': 'Object-Oriented Programming in Python'
    },
    {
        'video_id': 'YDa_mtS5cpw',
        'title': 'Python Data Science',
        'channel': 'Edureka',
        'duration': '3:10:00',
        'language': 'English',
        'category': 'Python/Data Science',
        'level': 'Intermediate',
        'description': 'Data Science with Python and Pandas'
    },
    
    # ==========================================
    # JAVASCRIPT & WEB DEVELOPMENT
    # ==========================================
    {
        'video_id': 'jS4aFq5-91o',
        'title': 'JavaScript for Beginners',
        'channel': 'Programming with Mosh',
        'duration': '3:37:00',
        'language': 'English',
        'category': 'JavaScript',
        'level': 'Beginner',
        'description': 'Complete JavaScript basics course'
    },
    {
        'video_id': '9i6q4q67CKE',
        'title': 'React Tutorial - Full Course',
        'channel': 'freeCodeCamp',
        'duration': '11:55:00',
        'language': 'English',
        'category': 'JavaScript/React',
        'level': 'Intermediate',
        'description': 'Complete React with Hooks and Context API'
    },
    {
        'video_id': 'mU6anWqk3UE',
        'title': 'HTML & CSS Full Course',
        'channel': 'Traversy Media',
        'duration': '12:02:00',
        'language': 'English',
        'category': 'Web Development',
        'level': 'Beginner',
        'description': 'Complete HTML and CSS tutorial'
    },
    {
        'video_id': '4SeQmsYWrMQ',
        'title': 'Node.js Tutorial for Beginners',
        'channel': 'Programming with Mosh',
        'duration': '3:29:00',
        'language': 'English',
        'category': 'JavaScript/Node.js',
        'level': 'Beginner',
        'description': 'Learn Node.js backend development'
    },
    {
        'video_id': 'pPzVKUC5ZHg',
        'title': 'Vue.js Full Course',
        'channel': 'Traversy Media',
        'duration': '4:51:00',
        'language': 'English',
        'category': 'JavaScript/Vue.js',
        'level': 'Intermediate',
        'description': 'Complete Vue.js framework tutorial'
    },
    
    # ==========================================
    # WEB DESIGN & UI/UX
    # ==========================================
    {
        'video_id': 'ydKzlqXQaKc',
        'title': 'Responsive Web Design',
        'channel': 'Traversy Media',
        'duration': '3:42:00',
        'language': 'English',
        'category': 'Web Design',
        'level': 'Beginner',
        'description': 'Mobile-first responsive design principles'
    },
    {
        'video_id': 'OXGznpKZ_sA',
        'title': 'CSS Flexbox Complete Guide',
        'channel': 'Traversy Media',
        'duration': '1:22:00',
        'language': 'English',
        'category': 'CSS',
        'level': 'Intermediate',
        'description': 'Master CSS Flexbox layout'
    },
    
    # ==========================================
    # DATABASE & SQL
    # ==========================================
    {
        'video_id': '4exKaLlNUjw',
        'title': 'SQL Complete Course',
        'channel': 'Programming with Mosh',
        'duration': '5:10:00',
        'language': 'English',
        'category': 'Database',
        'level': 'Beginner',
        'description': 'Complete SQL database tutorial'
    },
    {
        'video_id': 'TKvTvHB_JRk',
        'title': 'MongoDB Tutorial',
        'channel': 'Traversy Media',
        'duration': '2:15:00',
        'language': 'English',
        'category': 'Database/MongoDB',
        'level': 'Intermediate',
        'description': 'Learn MongoDB NoSQL database'
    },
    
    # ==========================================
    # JAVA PROGRAMMING
    # ==========================================
    {
        'video_id': 'grEKMHGYyLI',
        'title': 'Java for Complete Beginners',
        'channel': 'John Purcell',
        'duration': '7:09:00',
        'language': 'English',
        'category': 'Java',
        'level': 'Beginner',
        'description': 'Complete Java programming from scratch'
    },
    {
        'video_id': '9agem2dwtYE',
        'title': 'Spring Boot Tutorial',
        'channel': 'Telusko',
        'duration': '3:21:00',
        'language': 'English',
        'category': 'Java/Spring Boot',
        'level': 'Intermediate',
        'description': 'Learn Spring Boot framework'
    },
    
    # ==========================================
    # C / C++ PROGRAMMING
    # ==========================================
    {
        'video_id': 'vLnPJ8c5ZJc',
        'title': 'C Programming Complete',
        'channel': 'Telusko',
        'duration': '3:27:00',
        'language': 'English',
        'category': 'C',
        'level': 'Beginner',
        'description': 'C programming from basics to advanced'
    },
    {
        'video_id': 'mUQZ_DsYFEA',
        'title': 'C++ Complete Course',
        'channel': 'Telusko',
        'duration': '4:11:00',
        'language': 'English',
        'category': 'C++',
        'level': 'Beginner',
        'description': 'Complete C++ programming tutorial'
    },
    
    # ==========================================
    # MOBILE DEVELOPMENT
    # ==========================================
    {
        'video_id': 'fis26HvvDII',
        'title': 'Flutter & Dart for Beginners',
        'channel': 'Traversy Media',
        'duration': '3:45:00',
        'language': 'English',
        'category': 'Mobile/Flutter',
        'level': 'Beginner',
        'description': 'Learn Flutter for cross-platform mobile apps'
    },
    {
        'video_id': 'JsKsZAxg4Q4',
        'title': 'React Native for Beginners',
        'channel': 'Programming with Mosh',
        'duration': '3:02:00',
        'language': 'English',
        'category': 'Mobile/React Native',
        'level': 'Intermediate',
        'description': 'Mobile app development with React Native'
    },
    
    # ==========================================
    # DEVOPS & CLOUD
    # ==========================================
    {
        'video_id': 'fqMOX6JJhGo',
        'title': 'Docker Complete Course',
        'channel': 'Programming with Mosh',
        'duration': '2:28:00',
        'language': 'English',
        'category': 'DevOps/Docker',
        'level': 'Intermediate',
        'description': 'Learn Docker containerization'
    },
    {
        'video_id': '3c-iBkGY_x8',
        'title': 'Kubernetes Complete Guide',
        'channel': 'That DevOps Guy',
        'duration': '4:45:00',
        'language': 'English',
        'category': 'DevOps/Kubernetes',
        'level': 'Advanced',
        'description': 'Master Kubernetes orchestration'
    },
    
    # ==========================================
    # GIT & VERSION CONTROL
    # ==========================================
    {
        'video_id': 'apGV9Kg7ics',
        'title': 'Git & GitHub Complete Course',
        'channel': 'Traversy Media',
        'duration': '1:20:00',
        'language': 'English',
        'category': 'Tools/Git',
        'level': 'Beginner',
        'description': 'Learn Git and GitHub for version control'
    },
    
    # ==========================================
    # DATA STRUCTURES & ALGORITHMS
    # ==========================================
    {
        'video_id': 'rL8X2mlNHPM',
        'title': 'Data Structures Complete Course',
        'channel': 'Jenny\'s Lectures',
        'duration': '5:30:00',
        'language': 'English',
        'category': 'DSA',
        'level': 'Intermediate',
        'description': 'All data structures explained'
    },
    {
        'video_id': 'qli-JCrSwuk',
        'title': 'Algorithms Complete Course',
        'channel': 'TechVidvan',
        'duration': '4:12:00',
        'language': 'English',
        'category': 'DSA',
        'level': 'Intermediate',
        'description': 'Sorting, searching, and algorithm design'
    },
    
    # ==========================================
    # MACHINE LEARNING & AI
    # ==========================================
    {
        'video_id': 'Gv9_4yMHFhI',
        'title': 'Machine Learning Complete Course',
        'channel': 'Edureka',
        'duration': '11:00:00',
        'language': 'English',
        'category': 'Machine Learning',
        'level': 'Advanced',
        'description': 'Complete ML with Python and Scikit-learn'
    },
    {
        'video_id': 'PJOEPZQp0KY',
        'title': 'Deep Learning Neural Networks',
        'channel': 'Edureka',
        'duration': '6:30:00',
        'language': 'English',
        'category': 'AI/Deep Learning',
        'level': 'Advanced',
        'description': 'TensorFlow and Keras deep learning'
    },
    
    # ==========================================
    # CYBER SECURITY
    # ==========================================
    {
        'video_id': 'D__ZRp7QEgY',
        'title': 'Ethical Hacking Complete Course',
        'channel': 'Professor Messer',
        'duration': '6:45:00',
        'language': 'English',
        'category': 'Cybersecurity',
        'level': 'Intermediate',
        'description': 'Learn ethical hacking and penetration testing'
    },
    
    # ==========================================
    # LINUX & COMMAND LINE
    # ==========================================
    {
        'video_id': 'sB_tLDnfg2c',
        'title': 'Linux Command Line Complete',
        'channel': 'Edureka',
        'duration': '5:12:00',
        'language': 'English',
        'category': 'Linux',
        'level': 'Beginner',
        'description': 'Master Linux terminal commands'
    },
    
    # ==========================================
    # COMPETITIVE PROGRAMMING
    # ==========================================
    {
        'video_id': 'Z9lUwNK-ONE',
        'title': 'Competitive Programming Basics',
        'channel': 'Striver (Raj Vikramaditya)',
        'duration': '3:15:00',
        'language': 'English',
        'category': 'Programming',
        'level': 'Intermediate',
        'description': 'Start competitive programming journey'
    },
]

# Statistics
TOTAL_VIDEOS = len(FREE_CODING_VIDEOS)
TOTAL_HOURS = sum([
    int(v['duration'].split(':')[0]) * 60 + int(v['duration'].split(':')[1])
    for v in FREE_CODING_VIDEOS
]) // 60

print(f"Total Free Coding Videos: {TOTAL_VIDEOS}")
print(f"Total Learning Hours: {TOTAL_HOURS}+ hours")
print(f"100% FREE - No subscriptions required!")
