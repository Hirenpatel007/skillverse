from django.core.management.base import BaseCommand
from courses.models import Course
from jobs.models import Job
from payments.models import SubscriptionPlan

class Command(BaseCommand):
    help = 'Add sample data'

    def handle(self, *args, **kwargs):
        courses_data = [
            {'title': 'Python for Beginners', 'category': 'Web Development', 'price': 49.99, 'instructor': 'John Doe'},
            {'title': 'Data Science Masterclass', 'category': 'Data Science', 'price': 79.99, 'instructor': 'Jane Smith'},
            {'title': 'Machine Learning A-Z', 'category': 'Machine Learning', 'price': 89.99, 'instructor': 'AI Expert'},
            {'title': 'React Native Development', 'category': 'Mobile Development', 'price': 59.99, 'instructor': 'Mobile Dev'},
            {'title': 'AWS Cloud Practitioner', 'category': 'Cloud Computing', 'price': 69.99, 'instructor': 'Cloud Guru'},
            {'title': 'Ethical Hacking', 'category': 'Cybersecurity', 'price': 99.99, 'instructor': 'Security Pro'},
            {'title': 'Docker & Kubernetes', 'category': 'DevOps', 'price': 74.99, 'instructor': 'DevOps Master'},
            {'title': 'UI/UX Design Fundamentals', 'category': 'UI/UX Design', 'price': 54.99, 'instructor': 'Design Expert'},
            {'title': 'Digital Marketing 2024', 'category': 'Digital Marketing', 'price': 44.99, 'instructor': 'Marketing Pro'},
            {'title': 'Business Analytics', 'category': 'Business', 'price': 64.99, 'instructor': 'Business Analyst'},
        ]
        
        for course_data in courses_data:
            Course.objects.get_or_create(
                title=course_data['title'],
                defaults={
                    'description': f"Learn {course_data['title']} from scratch. Complete hands-on course with real-world projects.",
                    'category': course_data['category'],
                    'price': course_data['price'],
                    'instructor': course_data['instructor'],
                    'rating': 4.5,
                    'duration': '10 hours',
                }
            )
        
        jobs_data = [
            {'title': 'Python Developer', 'company': 'Tech Corp', 'location': 'Remote', 'skills': 'Python, Django, REST API'},
            {'title': 'Data Scientist', 'company': 'Data Inc', 'location': 'New York', 'skills': 'Python, ML, Statistics'},
            {'title': 'Full Stack Developer', 'company': 'Startup XYZ', 'location': 'San Francisco', 'skills': 'React, Node.js, MongoDB'},
        ]
        
        for job_data in jobs_data:
            Job.objects.get_or_create(
                title=job_data['title'],
                defaults={
                    'company': job_data['company'],
                    'location': job_data['location'],
                    'description': f"Exciting opportunity for {job_data['title']}",
                    'skills_required': job_data['skills'],
                    'job_type': 'Full-time',
                    'url': 'https://example.com/jobs',
                }
            )
        
        plans_data = [
            {'name': 'Free', 'price': 0, 'days': 365, 'features': 'Basic courses\nLimited access\nCommunity support'},
            {'name': 'Pro', 'price': 29.99, 'days': 30, 'features': 'All courses\nUnlimited access\nPriority support\nCertificates'},
            {'name': 'Enterprise', 'price': 99.99, 'days': 30, 'features': 'All Pro features\nTeam management\nCustom learning paths\n1-on-1 mentoring'},
        ]
        
        for plan_data in plans_data:
            SubscriptionPlan.objects.get_or_create(
                name=plan_data['name'],
                defaults={
                    'price': plan_data['price'],
                    'duration_days': plan_data['days'],
                    'features': plan_data['features'],
                }
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully added sample data'))
