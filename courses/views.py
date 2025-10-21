from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings
from .models import Course, Enrollment, VideoCompletion
from jobs.models import Job
from users.models import UserProfile, Achievement
from recommender.models import LearningPath
from payments.models import SubscriptionPlan
import json
import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime
import qrcode
from PIL import Image

def home(request):
    courses = Course.objects.all()[:6]
    return render(request, 'courses/home.html', {'courses': courses})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('free_videos_library')
        messages.error(request, 'Invalid credentials')
    return render(request, 'courses/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('free_videos_library')
    return render(request, 'courses/register.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    achievements = Achievement.objects.filter(user=request.user)[:5]
    recommended_courses = Course.objects.all()[:4]
    jobs = Job.objects.all()[:3]
    
    context = {
        'enrollments': enrollments,
        'achievements': achievements,
        'recommended_courses': recommended_courses,
        'jobs': jobs,
    }
    return render(request, 'courses/dashboard.html', context)

@login_required
def courses_view(request):
    category = request.GET.get('category')
    search = request.GET.get('search')
    
    courses = Course.objects.all()
    if category:
        courses = courses.filter(category=category)
    if search:
        courses = courses.filter(title__icontains=search)
    
    categories = Course.objects.values_list('category', flat=True).distinct()
    return render(request, 'courses/courses.html', {'courses': courses, 'categories': categories})

@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    enrolled = Enrollment.objects.filter(user=request.user, course=course).exists()
    return render(request, 'courses/course_detail.html', {'course': course, 'enrolled': enrolled})

@login_required
def enroll_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    Enrollment.objects.get_or_create(user=request.user, course=course)
    messages.success(request, f'Enrolled in {course.title}')
    return redirect('course_detail', pk=pk)

@login_required
def jobs_view(request):
    jobs = Job.objects.all()
    return render(request, 'courses/jobs.html', {'jobs': jobs})

@login_required
def learning_paths_view(request):
    paths = LearningPath.objects.filter(user=request.user)
    return render(request, 'courses/learning_paths.html', {'paths': paths})

@login_required
def subscriptions_view(request):
    plans = SubscriptionPlan.objects.filter(is_active=True)
    return render(request, 'courses/subscriptions.html', {'plans': plans})

@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile.skills = request.POST.get('skills', '')
        profile.career_goal = request.POST.get('career_goal', '')
        profile.experience_level = request.POST.get('experience_level', 'beginner')
        profile.bio = request.POST.get('bio', '')
        if request.FILES.get('profile_photo'):
            profile.profile_photo = request.FILES['profile_photo']
        profile.save()
        messages.success(request, 'Profile updated')
    return render(request, 'courses/profile.html', {'profile': profile})


# ===========================
# Certificate System Views
# ===========================

@csrf_exempt
@login_required
@require_http_methods(["POST"])
def complete_video(request):
    """API endpoint to mark video as complete and generate certificate"""
    try:
        data = json.loads(request.body)
        user = request.user
        video_id = data.get('video_id')
        
        if not video_id:
            return JsonResponse({'success': False, 'msg': 'video_id required'})
        
        # Check for duplicate completion
        if VideoCompletion.objects.filter(user=user, video_id=video_id).exists():
            return JsonResponse({'success': False, 'msg': 'Already completed'})
        
        # Create completion record
        completion = VideoCompletion.objects.create(user=user, video_id=video_id)
        
        # Generate PDF Certificate
        cert_id = generate_certificate(completion)
        
        return JsonResponse({
            'success': True, 
            'cert_id': cert_id,
            'msg': 'Certificate generated successfully!'
        })
    
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'msg': 'Invalid JSON'})
    except Exception as e:
        return JsonResponse({'success': False, 'msg': str(e)})


def generate_certificate(completion):
    """Generate premium PDF certificate with logo and signature"""
    try:
        from courses.models import YouTubeVideo
        
        # Create media directories
        media_root = settings.MEDIA_ROOT
        certs_dir = os.path.join(media_root, 'certs')
        qr_dir = os.path.join(media_root, 'qrcodes')
        os.makedirs(certs_dir, exist_ok=True)
        os.makedirs(qr_dir, exist_ok=True)
        
        # Get video details
        try:
            video = YouTubeVideo.objects.get(video_id=completion.video_id)
            video_title = video.title
            video_category = video.category
        except:
            video_title = f"Video {completion.video_id}"
            video_category = "Programming"
        
        # Detect technology from title/category
        def detect_tech(text):
            text_lower = text.lower()
            tech_map = {
                'python': ('PYTHON', 'python'),
                'django': ('PYTHON', 'python'),
                'flask': ('PYTHON', 'python'),
                'java': ('JAVA', 'java'),
                'kotlin': ('JAVA', 'java'),
                'android': ('JAVA', 'java'),
                'javascript': ('JS', 'javascript'),
                'js': ('JS', 'javascript'),
                'react': ('JS', 'javascript'),
                'vue': ('JS', 'javascript'),
                'angular': ('JS', 'javascript'),
                'node': ('NODE', 'node'),
                'nodejs': ('NODE', 'node'),
                'express': ('NODE', 'node'),
                'next': ('NEXT', 'nextjs'),
                'nextjs': ('NEXT', 'nextjs'),
                'sql': ('SQL', 'sql'),
                'mysql': ('SQL', 'sql'),
                'postgresql': ('SQL', 'sql'),
                'database': ('SQL', 'sql'),
                'go': ('GO', 'go'),
                'golang': ('GO', 'go'),
                'php': ('PHP', 'php'),
                'github': ('GIT', 'github'),
                'git': ('GIT', 'github'),
                'html': ('WEB', 'web'),
                'css': ('WEB', 'web'),
                'web': ('WEB', 'web'),
                'c++': ('C++', 'cpp'),
                'cpp': ('C++', 'cpp'),
            }
            for key, (name, logo) in tech_map.items():
                if key in text_lower:
                    return (name, logo)
            return ('CODE', 'default')
        
        tech_name, tech_key = detect_tech(f"{video_title} {video_category}")
        
        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(f"https://skillverse.com/certificate/{completion.id}/")
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="#667eea", back_color="white")
        qr_path = os.path.join(qr_dir, f'qr_{completion.id}.png')
        qr_img.save(qr_path)
        
        # Create PDF
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4
        
        # Premium border
        p.setStrokeColorRGB(0.4, 0.49, 0.92)
        p.setLineWidth(3)
        p.rect(30, 30, width-60, height-60)
        p.setLineWidth(1)
        p.rect(40, 40, width-80, height-80)
        
        # Logo at top
        logo_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'skillverse.png')
        if os.path.exists(logo_path):
            p.drawImage(logo_path, width/2-100, height-120, width=200, height=60, preserveAspectRatio=True, mask='auto')
        
        # Title
        p.setFont("Helvetica-Bold", 32)
        p.setFillColorRGB(0.4, 0.49, 0.92)
        p.drawCentredString(width/2, height-160, "Certificate of Completion")
        
        # Decorative line
        p.setStrokeColorRGB(0.4, 0.49, 0.92)
        p.setLineWidth(2)
        p.line(width/2-150, height-170, width/2+150, height-170)
        
        # Body text
        p.setFont("Helvetica", 16)
        p.setFillColorRGB(0.3, 0.3, 0.3)
        p.drawCentredString(width/2, height-220, "This is to certify that")
        
        # Student name
        p.setFont("Helvetica-Bold", 28)
        p.setFillColorRGB(0.17, 0.24, 0.31)
        student_name = completion.user.first_name or completion.user.username
        p.drawCentredString(width/2, height-270, student_name)
        
        # Underline name
        p.setStrokeColorRGB(0.4, 0.49, 0.92)
        p.setLineWidth(1)
        p.line(width/2-150, height-280, width/2+150, height-280)
        
        # Course info
        p.setFont("Helvetica", 16)
        p.setFillColorRGB(0.3, 0.3, 0.3)
        p.drawCentredString(width/2, height-320, "has successfully completed the video course")
        
        # Technology logo (mini format) - Draw colored box with text
        tech_colors = {
            'PYTHON': ((0.22, 0.46, 0.67), (1, 1, 1)),
            'JAVA': ((0.0, 0.45, 0.59), (1, 1, 1)),
            'JS': ((0.97, 0.87, 0.12), (0, 0, 0)),
            'SQL': ((0.8, 0.16, 0.15), (1, 1, 1)),
            'GO': ((0.0, 0.68, 0.85), (1, 1, 1)),
            'PHP': ((0.47, 0.48, 0.71), (1, 1, 1)),
            'NODE': ((0.2, 0.6, 0.2), (1, 1, 1)),
            'NEXT': ((0.0, 0.0, 0.0), (1, 1, 1)),
            'GIT': ((0.09, 0.09, 0.09), (1, 1, 1)),
            'WEB': ((0.23, 0.52, 0.78), (1, 1, 1)),
            'C++': ((0.0, 0.37, 0.66), (1, 1, 1)),
            'CODE': ((0.4, 0.49, 0.92), (1, 1, 1)),
        }
        bg_color, text_color = tech_colors.get(tech_name, ((0.4, 0.49, 0.92), (1, 1, 1)))
        
        # Draw rounded rectangle
        p.setFillColorRGB(*bg_color)
        p.roundRect(width/2-25, height-370, 50, 40, 5, fill=1, stroke=0)
        
        # Draw text
        p.setFillColorRGB(*text_color)
        p.setFont("Helvetica-Bold", 11)
        text_width = p.stringWidth(tech_name, "Helvetica-Bold", 11)
        p.drawString(width/2 - text_width/2, height-353, tech_name)
        
        p.setFont("Helvetica-Bold", 16)
        p.setFillColorRGB(0.4, 0.49, 0.92)
        p.drawCentredString(width/2, height-395, video_title[:60])
        
        p.setFont("Helvetica", 11)
        p.setFillColorRGB(0.5, 0.5, 0.5)
        p.drawCentredString(width/2, height-415, f"Video ID: {completion.video_id}")
        
        # Date and ID
        p.setFont("Helvetica", 14)
        p.setFillColorRGB(0.3, 0.3, 0.3)
        completion_date = completion.completed_at.strftime("%B %d, %Y")
        p.drawCentredString(width/2, height-450, f"Date of Completion: {completion_date}")
        p.drawCentredString(width/2, height-475, f"Certificate ID: SV-{completion.id:06d}")
        
        # Signature section
        sig_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'signature.png')
        if os.path.exists(sig_path):
            p.drawImage(sig_path, width/2-100, height-590, width=200, height=60, preserveAspectRatio=True, mask='auto')
        
        p.setFont("Helvetica-Bold", 12)
        p.setFillColorRGB(0.17, 0.24, 0.31)
        p.drawCentredString(width/2, height-610, "Hiren Patel")
        p.setFont("Helvetica", 10)
        p.setFillColorRGB(0.4, 0.4, 0.4)
        p.drawCentredString(width/2, height-625, "Founder & CEO, SkillVerse")
        
        # QR Code
        p.drawImage(qr_path, width-150, 60, width=80, height=80)
        p.setFont("Helvetica", 8)
        p.setFillColorRGB(0.4, 0.4, 0.4)
        p.drawCentredString(width-110, 45, "Scan to Verify")
        
        # Footer
        p.setFont("Helvetica-Bold", 10)
        p.setFillColorRGB(0.4, 0.49, 0.92)
        p.drawCentredString(width/2, 60, "SkillVerse Learning Platform")
        p.setFont("Helvetica", 8)
        p.setFillColorRGB(0.4, 0.4, 0.4)
        p.drawCentredString(width/2, 48, "www.skillverse.com | Verified Certificate")
        
        p.save()
        buffer.seek(0)
        
        # Save PDF
        cert_filename = f"cert_{completion.id}.pdf"
        cert_path = os.path.join(certs_dir, cert_filename)
        with open(cert_path, 'wb') as f:
            f.write(buffer.getvalue())
        
        completion.certificate_path = f'certs/{cert_filename}'
        completion.save()
        
        return completion.id
    
    except Exception as e:
        print(f"Error generating certificate: {str(e)}")
        raise


@login_required
def download_certificate(request, cert_id):
    """Download certificate PDF"""
    try:
        completion = VideoCompletion.objects.get(id=cert_id, user=request.user)
        
        if not completion.certificate_path:
            return JsonResponse({'success': False, 'msg': 'Certificate not found'})
        
        cert_file_path = os.path.join(settings.MEDIA_ROOT, str(completion.certificate_path))
        
        if not os.path.exists(cert_file_path):
            return JsonResponse({'success': False, 'msg': 'Certificate file not found'})
        
        return FileResponse(
            open(cert_file_path, 'rb'), 
            as_attachment=True,
            filename=f"skillverse_cert_{cert_id}.pdf"
        )
    
    except VideoCompletion.DoesNotExist:
        return JsonResponse({'success': False, 'msg': 'Certificate not found'})
    except Exception as e:
        return JsonResponse({'success': False, 'msg': str(e)})


@login_required
def view_certificate(request, cert_id):
    """View certificate in browser"""
    try:
        completion = VideoCompletion.objects.get(id=cert_id, user=request.user)
        
        if not completion.certificate_path:
            messages.error(request, 'Certificate not found. Please regenerate.')
            return redirect('user_certificates')
        
        cert_url = f"/media/{completion.certificate_path}"
        
        return render(request, 'courses/certificate.html', {
            'completion': completion,
            'cert_url': cert_url
        })
    
    except VideoCompletion.DoesNotExist:
        messages.error(request, 'Certificate not found')
        return redirect('user_certificates')
    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
        return redirect('user_certificates')


@login_required
def user_certificates(request):
    """List all user certificates"""
    completions = VideoCompletion.objects.filter(user=request.user).order_by('-completed_at')
    return render(request, 'courses/certificates.html', {'completions': completions})


# ===========================
# User Upload System
# ===========================

from .models import UserUpload
from django.core.paginator import Paginator

@login_required
def upload_resource(request):
    """Upload notes, PDFs, images, videos"""
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        category = request.POST.get('category', '')
        file = request.FILES.get('file')
        is_public = request.POST.get('is_public') == 'on'
        
        if title and file:
            # Detect file type
            file_ext = file.name.split('.')[-1].lower()
            file_type_map = {
                'pdf': 'pdf',
                'jpg': 'image', 'jpeg': 'image', 'png': 'image', 'gif': 'image',
                'mp4': 'video', 'avi': 'video', 'mov': 'video',
                'txt': 'note', 'doc': 'note', 'docx': 'note',
            }
            file_type = file_type_map.get(file_ext, 'other')
            
            UserUpload.objects.create(
                user=request.user,
                title=title,
                description=description,
                file=file,
                file_type=file_type,
                category=category,
                is_public=is_public
            )
            messages.success(request, 'Resource uploaded successfully!')
            return redirect('sharing_platform')
        else:
            messages.error(request, 'Title and file are required')
    
    return render(request, 'courses/upload.html')


@login_required
def sharing_platform(request):
    """View all shared resources"""
    file_type = request.GET.get('type', '')
    search = request.GET.get('search', '')
    
    uploads = UserUpload.objects.filter(is_public=True)
    
    if file_type:
        uploads = uploads.filter(file_type=file_type)
    if search:
        uploads = uploads.filter(title__icontains=search)
    
    uploads = uploads.order_by('-uploaded_at')
    
    paginator = Paginator(uploads, 12)
    page = request.GET.get('page', 1)
    uploads_page = paginator.get_page(page)
    
    context = {
        'uploads': uploads_page,
        'file_types': UserUpload.FILE_TYPES,
        'active_type': file_type,
        'search_term': search,
    }
    return render(request, 'courses/sharing_platform.html', context)


@login_required
def my_uploads(request):
    """View user's own uploads"""
    uploads = UserUpload.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'courses/my_uploads.html', {'uploads': uploads})


@login_required
def download_resource(request, pk):
    """Download a resource"""
    upload = get_object_or_404(UserUpload, pk=pk)
    if upload.is_public or upload.user == request.user:
        upload.downloads += 1
        upload.save()
        return FileResponse(upload.file.open('rb'), as_attachment=True, filename=upload.file.name)
    return JsonResponse({'error': 'Access denied'}, status=403)


@login_required
def delete_upload(request, pk):
    """Delete user's upload"""
    upload = get_object_or_404(UserUpload, pk=pk, user=request.user)
    upload.file.delete()
    upload.delete()
    messages.success(request, 'Resource deleted successfully')
    return redirect('my_uploads')
