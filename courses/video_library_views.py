"""
Free YouTube Video Library Views
Display and manage free coding videos
"""

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from .models import YouTubeVideo


@login_required
def free_videos_library(request):
    """Display all free YouTube coding videos with filters"""
    
    # Get filter parameters
    category = request.GET.get('category')
    level = request.GET.get('level')
    search = request.GET.get('search')
    
    # Start with all videos
    videos = YouTubeVideo.objects.filter(is_active=True, is_free=True)
    
    # Apply filters
    if category:
        videos = videos.filter(category__icontains=category)
    
    if level:
        videos = videos.filter(level=level)
    
    if search:
        videos = videos.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(channel__icontains=search)
        )
    
    # Get unique categories and levels for filters
    categories = YouTubeVideo.objects.filter(
        is_active=True, is_free=True
    ).values_list('category', flat=True).distinct()
    
    levels = YouTubeVideo.LEVEL_CHOICES
    
    context = {
        'videos': videos,
        'categories': sorted(set(categories)),
        'levels': levels,
        'active_category': category,
        'active_level': level,
        'search_term': search,
        'total_videos': YouTubeVideo.objects.filter(is_active=True, is_free=True).count(),
        'total_hours': calculate_total_hours(videos),
    }
    
    return render(request, 'courses/free_videos_library.html', context)


@login_required
def video_player(request, video_id):
    """Display individual video player"""
    video = get_object_or_404(YouTubeVideo, video_id=video_id, is_active=True)
    
    # Get related videos (same category)
    related_videos = YouTubeVideo.objects.filter(
        category=video.category,
        is_active=True,
        is_free=True
    ).exclude(video_id=video_id)[:5]
    
    context = {
        'video': video,
        'related_videos': related_videos,
        'thumbnail_url': video.thumbnail_url or f"https://i.ytimg.com/vi/{video.video_id}/maxresdefault.jpg",
    }
    
    return render(request, 'courses/video_player.html', context)


@login_required
def videos_by_category(request, category):
    """Display videos by category"""
    videos = YouTubeVideo.objects.filter(
        category__icontains=category,
        is_active=True,
        is_free=True
    ).order_by('-added_date')
    
    categories = YouTubeVideo.objects.filter(
        is_active=True, is_free=True
    ).values_list('category', flat=True).distinct()
    
    context = {
        'videos': videos,
        'category': category,
        'categories': sorted(set(categories)),
        'count': videos.count(),
    }
    
    return render(request, 'courses/videos_by_category.html', context)


@login_required
def videos_by_level(request, level):
    """Display videos by difficulty level"""
    valid_levels = ['beginner', 'intermediate', 'advanced']
    
    if level not in valid_levels:
        return JsonResponse({'error': 'Invalid level'}, status=400)
    
    videos = YouTubeVideo.objects.filter(
        level=level,
        is_active=True,
        is_free=True
    ).order_by('-added_date')
    
    context = {
        'videos': videos,
        'level': level.capitalize(),
        'level_code': level,
        'count': videos.count(),
    }
    
    return render(request, 'courses/videos_by_level.html', context)


@login_required
def video_api_search(request):
    """API endpoint for video search (AJAX)"""
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    level = request.GET.get('level', '')
    
    videos = YouTubeVideo.objects.filter(is_active=True, is_free=True)
    
    if query:
        videos = videos.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(channel__icontains=query)
        )
    
    if category:
        videos = videos.filter(category__icontains=category)
    
    if level:
        videos = videos.filter(level=level)
    
    results = [
        {
            'id': video.video_id,
            'title': video.title,
            'channel': video.channel,
            'category': video.category,
            'level': video.level,
            'duration': video.duration,
            'thumbnail': video.thumbnail_url,
        }
        for video in videos[:20]
    ]
    
    return JsonResponse({'results': results})


@login_required
def get_video_stats(request):
    """Get statistics about video library"""
    total_videos = YouTubeVideo.objects.filter(is_active=True, is_free=True).count()
    
    categories = YouTubeVideo.objects.filter(
        is_active=True, is_free=True
    ).values('category').annotate(count=Count('id')).order_by('-count')
    
    levels = YouTubeVideo.objects.filter(
        is_active=True, is_free=True
    ).values('level').annotate(count=Count('id'))
    
    stats = {
        'total_videos': total_videos,
        'total_hours': calculate_total_hours(YouTubeVideo.objects.filter(is_active=True, is_free=True)),
        'categories': list(categories),
        'levels': list(levels),
    }
    
    return JsonResponse(stats)


def calculate_total_hours(videos):
    """Calculate total hours from video queryset"""
    total_seconds = 0
    for video in videos:
        try:
            parts = video.duration.split(':')
            if len(parts) == 3:
                hours, minutes, seconds = map(int, parts)
                total_seconds += hours * 3600 + minutes * 60 + seconds
            elif len(parts) == 2:
                minutes, seconds = map(int, parts)
                total_seconds += minutes * 60 + seconds
        except (ValueError, AttributeError):
            pass
    
    hours = total_seconds // 3600
    return hours


from django.db.models import Count
