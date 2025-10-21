"""
Management command to load free YouTube videos into database
Run: python manage.py load_free_videos
"""

from django.core.management.base import BaseCommand
from courses.models import YouTubeVideo
from courses.free_videos_database import FREE_CODING_VIDEOS


class Command(BaseCommand):
    help = 'Load free YouTube coding videos into database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing videos before loading',
        )

    def handle(self, *args, **options):
        if options['clear']:
            YouTubeVideo.objects.all().delete()
            self.stdout.write(self.style.WARNING('Cleared existing videos'))

        created_count = 0
        updated_count = 0
        skipped_count = 0

        for video_data in FREE_CODING_VIDEOS:
            try:
                video, created = YouTubeVideo.objects.update_or_create(
                    video_id=video_data['video_id'],
                    defaults={
                        'title': video_data['title'],
                        'description': video_data.get('description', ''),
                        'channel': video_data['channel'],
                        'duration': video_data['duration'],
                        'category': video_data['category'],
                        'level': video_data['level'].lower(),
                        'language': video_data.get('language', 'English'),
                        'thumbnail_url': f"https://i.ytimg.com/vi/{video_data['video_id']}/maxresdefault.jpg",
                        'is_free': True,
                        'is_active': True,
                    }
                )
                
                if created:
                    created_count += 1
                    self.stdout.write(
                        self.style.SUCCESS(f'✓ Created: {video.title}')
                    )
                else:
                    updated_count += 1
                    self.stdout.write(
                        self.style.WARNING(f'↻ Updated: {video.title}')
                    )
                    
            except Exception as e:
                skipped_count += 1
                self.stdout.write(
                    self.style.ERROR(f'✗ Failed: {video_data["title"]} - {str(e)}')
                )

        # Print summary
        total_videos = YouTubeVideo.objects.count()
        self.stdout.write('\n' + '='*60)
        self.stdout.write(self.style.SUCCESS(f'✓ Created: {created_count} videos'))
        self.stdout.write(self.style.WARNING(f'↻ Updated: {updated_count} videos'))
        if skipped_count > 0:
            self.stdout.write(self.style.ERROR(f'✗ Skipped: {skipped_count} videos'))
        self.stdout.write(self.style.SUCCESS(f'\n✓ Total videos in database: {total_videos}'))
        self.stdout.write('='*60)
