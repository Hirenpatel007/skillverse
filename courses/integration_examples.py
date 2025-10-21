"""
Integration Examples for YouTube Certificate System
Showing how to use the certificate system in your views
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import VideoCompletion, Course
from .certificate_utils import create_certificate_for_completion, get_user_completion_stats


# ============================================
# Example 1: Video Page with Course
# ============================================

@login_required
def course_video_view(request, course_id, video_id):
    """
    Display a course video with certificate generation support
    
    Example URL: /course/1/video/dQw4w9WgXcQ/
    """
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return JsonResponse({'error': 'Course not found'}, status=404)
    
    context = {
        'course': course,
        'video_id': video_id,
        'course_title': course.title,
        'course_description': course.description,
        'duration': course.duration,
        'instructor': course.instructor,
        'category': course.category,
        'user': request.user,
    }
    
    return render(request, 'courses/video.html', context)


# ============================================
# Example 2: Multi-Video Course (Series)
# ============================================

@login_required
def course_series_view(request, course_id):
    """
    Display course series with multiple videos
    After completing all videos, issue a master certificate
    """
    course = Course.objects.get(id=course_id)
    
    # Assume course has JSON with video IDs
    video_ids = ['dQw4w9WgXcQ', 'jNQXAC9IVRw', 'CJvoNdIyV1A']
    
    # Get completion status
    completions = VideoCompletion.objects.filter(
        user=request.user,
        video_id__in=video_ids
    )
    
    completion_status = {
        video_id: completions.filter(video_id=video_id).exists()
        for video_id in video_ids
    }
    
    all_completed = all(completion_status.values())
    
    context = {
        'course': course,
        'video_ids': video_ids,
        'completion_status': completion_status,
        'all_completed': all_completed,
        'progress': f"{sum(completion_status.values())}/{len(video_ids)}",
    }
    
    return render(request, 'courses/course_series.html', context)


# ============================================
# Example 3: User Dashboard with Certificates
# ============================================

@login_required
def user_dashboard_view(request):
    """
    User dashboard showing:
    - Recent certificates
    - Completion statistics
    - Progress tracking
    """
    user = request.user
    
    # Get certificate stats
    stats = get_user_completion_stats(user)
    
    # Get recent completions
    recent_completions = VideoCompletion.objects.filter(
        user=user
    ).order_by('-completed_at')[:5]
    
    context = {
        'total_videos': stats['total_videos'],
        'total_certificates': stats['total_certificates'],
        'recent_completion': stats['recent_completion'],
        'recent_completions': recent_completions,
        'completion_rate': (
            (stats['total_certificates'] / stats['total_videos'] * 100)
            if stats['total_videos'] > 0 else 0
        )
    }
    
    return render(request, 'courses/dashboard.html', context)


# ============================================
# Example 4: Bulk Certificate Generation
# ============================================

@login_required
def generate_bulk_certificates(request):
    """
    Generate certificates for all pending completions
    Useful for admin tasks or background jobs
    """
    user = request.user
    
    # Get all completions without certificates
    pending = VideoCompletion.objects.filter(
        user=user,
        certificate_path__isnull=True
    )
    
    generated = 0
    errors = []
    
    for completion in pending:
        try:
            cert_path = create_certificate_for_completion(completion)
            if cert_path:
                completion.certificate_path = cert_path
                completion.save()
                generated += 1
            else:
                errors.append(f"Failed for video {completion.video_id}")
        except Exception as e:
            errors.append(f"Error for {completion.video_id}: {str(e)}")
    
    return JsonResponse({
        'success': len(errors) == 0,
        'generated': generated,
        'errors': errors,
    })


# ============================================
# Example 5: Certificate with Custom Template
# ============================================

@login_required
def generate_custom_certificate(request, cert_id):
    """
    Generate certificate with custom template
    Supports different certificate designs per course
    """
    from .certificate_utils import CertificateGenerator
    
    try:
        completion = VideoCompletion.objects.get(id=cert_id, user=request.user)
    except VideoCompletion.DoesNotExist:
        return JsonResponse({'error': 'Certificate not found'}, status=404)
    
    # Choose template based on course or video type
    template = request.GET.get('template', 'standard')  # 'standard' or 'professional'
    
    try:
        # Generate certificate
        cert_path = create_certificate_for_completion(
            completion,
            template=template,
            include_qr=True
        )
        
        if cert_path:
            completion.certificate_path = cert_path
            completion.save()
            
            return JsonResponse({
                'success': True,
                'message': 'Certificate generated successfully',
                'cert_id': cert_id,
                'download_url': f'/certificate/{cert_id}/download/',
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Failed to generate certificate'
            })
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)


# ============================================
# Example 6: Leaderboard by Certificates
# ============================================

@login_required
def certificate_leaderboard(request):
    """
    Display leaderboard of users by number of certificates
    """
    from django.db.models import Count
    from django.contrib.auth.models import User
    
    leaderboard = (
        User.objects
        .annotate(cert_count=Count('videocompletion', distinct=True))
        .filter(cert_count__gt=0)
        .order_by('-cert_count')[:20]
    )
    
    context = {
        'leaderboard': leaderboard,
        'user_rank': None,
    }
    
    # Get current user's rank
    for i, user in enumerate(leaderboard, 1):
        if user.id == request.user.id:
            context['user_rank'] = i
            context['user_certs'] = user.cert_count
            break
    
    return render(request, 'courses/leaderboard.html', context)


# ============================================
# Example 7: Progress Tracking
# ============================================

@login_required
def track_video_progress(request):
    """
    Track video progress and save milestones
    
    POST /api/track-progress/
    {
        "video_id": "dQw4w9WgXcQ",
        "progress": 50,  # Percentage
        "duration": 600  # Total seconds
    }
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=400)
    
    import json
    data = json.loads(request.body)
    
    video_id = data.get('video_id')
    progress = data.get('progress', 0)
    
    # You could save progress to a separate model
    # For now, just return success
    
    milestones = {
        25: 'Start Milestone',
        50: 'Halfway There!',
        75: 'Almost Done',
        100: 'Completed! Certificate Ready',
    }
    
    milestone_msg = None
    for milestone, msg in milestones.items():
        if progress == milestone:
            milestone_msg = msg
            break
    
    return JsonResponse({
        'success': True,
        'progress': progress,
        'milestone': milestone_msg,
    })


# ============================================
# Example 8: Share Certificate on Social Media
# ============================================

@login_required
def get_certificate_share_data(request, cert_id):
    """
    Get data for sharing certificate on social media
    
    Returns OG tags and metadata
    """
    try:
        completion = VideoCompletion.objects.get(id=cert_id, user=request.user)
    except VideoCompletion.DoesNotExist:
        return JsonResponse({'error': 'Certificate not found'}, status=404)
    
    share_url = f"https://yourdomain.com/certificate/{cert_id}/view/"
    
    share_data = {
        'title': f"🎓 I completed: {completion.video_id}",
        'description': f"{request.user.first_name or request.user.username} completed a video on Skillverse!",
        'url': share_url,
        'image': f"https://yourdomain.com/static/skillverse-cert-badge.png",
        'hashtags': ['#Skillverse', '#Learning', '#Certificate', '#Achievement'],
    }
    
    # Generate share links
    share_links = {
        'twitter': f"https://twitter.com/intent/tweet?text={share_data['description']}&url={share_url}",
        'facebook': f"https://facebook.com/sharer/sharer.php?u={share_url}",
        'linkedin': f"https://linkedin.com/sharing/share-offsite/?url={share_url}",
        'whatsapp': f"https://wa.me/?text={share_data['description']} {share_url}",
    }
    
    return JsonResponse({
        'success': True,
        'share_data': share_data,
        'share_links': share_links,
    })


# ============================================
# Example 9: Admin Certificate Management
# ============================================

@login_required
def admin_certificate_management(request):
    """
    Admin view for managing certificates
    - Regenerate certificates
    - Export certificates
    - View statistics
    """
    if not request.user.is_staff:
        return JsonResponse({'error': 'Permission denied'}, status=403)
    
    # Get statistics
    from django.db.models import Count
    
    total_completions = VideoCompletion.objects.count()
    total_users = VideoCompletion.objects.values('user').distinct().count()
    certificates_generated = VideoCompletion.objects.filter(
        certificate_path__isnull=False
    ).count()
    
    stats = {
        'total_completions': total_completions,
        'total_users': total_users,
        'certificates_generated': certificates_generated,
        'pending_certificates': total_completions - certificates_generated,
    }
    
    context = {
        'stats': stats,
    }
    
    return render(request, 'admin/certificate_management.html', context)


# ============================================
# Example 10: Export User Certificates as ZIP
# ============================================

@login_required
def export_my_certificates(request):
    """
    Export all user certificates as ZIP file
    """
    from .certificate_utils import export_certificates_batch
    from django.http import FileResponse
    
    user = request.user
    
    # Get all user's video IDs
    video_ids = VideoCompletion.objects.filter(
        user=user
    ).values_list('video_id', flat=True).distinct()
    
    # Generate batch
    zip_path = export_certificates_batch(user, video_ids)
    
    if zip_path and os.path.exists(zip_path):
        return FileResponse(
            open(zip_path, 'rb'),
            as_attachment=True,
            filename=f'skillverse_certificates_{user.id}.zip'
        )
    
    return JsonResponse({
        'error': 'No certificates to export'
    }, status=404)
