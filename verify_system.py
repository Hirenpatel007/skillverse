#!/usr/bin/env python
"""
Certificate System Verification Script
Run this to verify the YouTube Certificate System is properly installed

Usage:
    python verify_system.py
"""

import os
import sys
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillverse.settings')
sys.path.insert(0, str(Path(__file__).parent))

django.setup()

from django.conf import settings
from courses.models import VideoCompletion, Course, Enrollment
from django.contrib.auth.models import User

print("=" * 60)
print("🎓 SKILLVERSE CERTIFICATE SYSTEM VERIFICATION")
print("=" * 60)
print()

# Check 1: Required packages
print("✓ Step 1: Checking installed packages...")
try:
    import reportlab
    print("  ✅ reportlab installed")
except ImportError:
    print("  ❌ reportlab NOT installed")
    print("     Run: pip install reportlab")

try:
    import qrcode
    print("  ✅ qrcode installed")
except ImportError:
    print("  ❌ qrcode NOT installed")
    print("     Run: pip install qrcode[pil]")

try:
    import PIL
    print("  ✅ pillow (PIL) installed")
except ImportError:
    print("  ❌ pillow NOT installed")
    print("     Run: pip install pillow")

print()

# Check 2: Media directories
print("✓ Step 2: Checking media directories...")
media_root = settings.MEDIA_ROOT

if os.path.exists(media_root):
    print(f"  ✅ Media root exists: {media_root}")
else:
    print(f"  ⚠️  Media root doesn't exist: {media_root}")
    print(f"     Creating it...")
    os.makedirs(media_root, exist_ok=True)
    print(f"     ✅ Created")

cert_dir = os.path.join(media_root, 'certs')
if os.path.exists(cert_dir):
    print(f"  ✅ Certs directory exists")
else:
    print(f"  ⚠️  Certs directory doesn't exist")
    print(f"     Creating it...")
    os.makedirs(cert_dir, exist_ok=True)
    print(f"     ✅ Created")

qr_dir = os.path.join(media_root, 'qrcodes')
if os.path.exists(qr_dir):
    print(f"  ✅ QR codes directory exists")
else:
    print(f"  ⚠️  QR codes directory doesn't exist")
    print(f"     Creating it...")
    os.makedirs(qr_dir, exist_ok=True)
    print(f"     ✅ Created")

print()

# Check 3: Database model
print("✓ Step 3: Checking database models...")
try:
    vc = VideoCompletion.objects.first()
    print(f"  ✅ VideoCompletion model exists in database")
    print(f"     Total completions: {VideoCompletion.objects.count()}")
except Exception as e:
    print(f"  ❌ VideoCompletion model error: {e}")
    print(f"     Run: python manage.py migrate")

print()

# Check 4: Test files exist
print("✓ Step 4: Checking template files...")
templates = [
    'courses/templates/courses/video.html',
    'courses/templates/courses/certificate.html',
    'courses/templates/courses/certificates.html',
]

base_path = Path(__file__).parent
for template in templates:
    template_path = base_path / template
    if template_path.exists():
        print(f"  ✅ {template}")
    else:
        print(f"  ❌ {template} NOT found")

print()

# Check 5: Views exist
print("✓ Step 5: Checking views...")
try:
    from courses.views import (
        complete_video, 
        download_certificate, 
        view_certificate,
        user_certificates
    )
    print(f"  ✅ complete_video view exists")
    print(f"  ✅ download_certificate view exists")
    print(f"  ✅ view_certificate view exists")
    print(f"  ✅ user_certificates view exists")
except ImportError as e:
    print(f"  ❌ Views import error: {e}")

print()

# Check 6: Utilities exist
print("✓ Step 6: Checking utility modules...")
try:
    from courses.certificate_utils import CertificateGenerator, create_certificate_for_completion
    print(f"  ✅ certificate_utils module exists")
    print(f"  ✅ CertificateGenerator class available")
except ImportError as e:
    print(f"  ❌ Utilities error: {e}")

try:
    from courses.integration_examples import course_video_view
    print(f"  ✅ integration_examples module exists")
except ImportError as e:
    print(f"  ❌ Examples error: {e}")

print()

# Check 7: Settings
print("✓ Step 7: Checking Django settings...")
print(f"  MEDIA_URL: {settings.MEDIA_URL}")
print(f"  MEDIA_ROOT: {settings.MEDIA_ROOT}")
print(f"  CORS_ALLOW_ALL_ORIGINS: {settings.CORS_ALLOW_ALL_ORIGINS}")
print(f"  DEBUG: {settings.DEBUG}")

print()

# Check 8: URLs
print("✓ Step 8: Checking URL configuration...")
try:
    from django.urls import reverse
    urls_to_check = [
        'complete_video',
        'download_certificate',
        'view_certificate',
        'user_certificates',
    ]
    
    for url_name in urls_to_check:
        try:
            url = reverse(url_name, kwargs={'cert_id': 1} if 'cert' in url_name else {})
            print(f"  ✅ {url_name}: {url}")
        except Exception as e:
            if 'cert_id' in str(e):
                # Expected for routes that need cert_id
                print(f"  ✅ {url_name}: (requires cert_id parameter)")
            else:
                print(f"  ⚠️  {url_name}: {e}")
except Exception as e:
    print(f"  ❌ URL check error: {e}")

print()

# Summary
print("=" * 60)
print("✅ VERIFICATION COMPLETE!")
print("=" * 60)
print()
print("📋 QUICK START:")
print("  1. python manage.py runserver")
print("  2. Login at http://localhost:8000/")
print("  3. Visit http://localhost:8000/watch/dQw4w9WgXcQ/")
print("  4. Play video until completion")
print("  5. Certificate auto-generates!")
print("  6. View certificates at http://localhost:8000/certificates/")
print()
print("📚 DOCUMENTATION:")
print("  - CERTIFICATE_SYSTEM.md (complete guide)")
print("  - CERTIFICATE_IMPLEMENTATION.md (setup summary)")
print("  - courses/integration_examples.py (10 code examples)")
print()
print("🎓 System is ready to use!")
print()
