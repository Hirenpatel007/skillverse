"""
Certificate utility functions for Skillverse
Reusable functions for certificate generation and management
"""

import os
import qrcode
from io import BytesIO
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.colors import HexColor
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings


class CertificateGenerator:
    """Generate professional certificates with customization"""
    
    # Certificate Colors
    COLORS = {
        'primary': HexColor('#0066CC'),
        'accent': HexColor('#FF6B6B'),
        'text': HexColor('#333333'),
        'light': HexColor('#F0F0F0'),
    }
    
    # Certificate Templates
    TEMPLATES = {
        'standard': {
            'title': '🎓 Certificate of Completion',
            'footer': 'Skillverse Learning Platform | Verified Certificate',
        },
        'professional': {
            'title': 'Professional Certificate of Achievement',
            'footer': 'This certificate verifies professional competency',
        }
    }
    
    def __init__(self, user, video_id, template='standard', pagesize=A4):
        self.user = user
        self.video_id = video_id
        self.template = self.TEMPLATES.get(template, self.TEMPLATES['standard'])
        self.pagesize = pagesize
        self.width, self.height = pagesize
        
    def generate_qr_code(self, data, cert_id):
        """Generate QR code image"""
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=5,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        qr_img = qr.make_image(fill_color="black", back_color="white")
        
        # Save QR code
        qr_dir = os.path.join(settings.MEDIA_ROOT, 'qrcodes')
        os.makedirs(qr_dir, exist_ok=True)
        qr_path = os.path.join(qr_dir, f'qr_{cert_id}.png')
        qr_img.save(qr_path)
        
        return qr_path
    
    def create_pdf(self, completion, qr_code_path=None):
        """Create PDF certificate"""
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=self.pagesize)
        
        # Add decorative border
        p.setLineWidth(3)
        p.setStrokeColor(self.COLORS['primary'])
        p.rect(30, 30, self.width-60, self.height-60)
        
        # Add inner border
        p.setLineWidth(1)
        p.rect(50, 50, self.width-100, self.height-100)
        
        # Title
        p.setFont("Helvetica-Bold", 32)
        p.setFillColor(self.COLORS['primary'])
        p.drawCentredString(self.width/2, self.height-100, self.template['title'])
        
        # Subtitle
        p.setFont("Helvetica", 14)
        p.setFillColor(self.COLORS['text'])
        p.drawCentredString(self.width/2, self.height-140, "This is to certify that")
        
        # User name
        p.setFont("Helvetica-Bold", 24)
        p.setFillColor(HexColor('#000000'))
        user_name = completion.user.first_name or completion.user.username
        p.drawCentredString(self.width/2, self.height-190, user_name)
        
        # Achievement text
        p.setFont("Helvetica", 14)
        p.setFillColor(self.COLORS['text'])
        p.drawCentredString(self.width/2, self.height-240, "has successfully completed")
        
        # Video/Course details
        p.setFont("Helvetica-Bold", 16)
        p.setFillColor(self.COLORS['accent'])
        p.drawCentredString(self.width/2, self.height-290, f"Video Tutorial: {completion.video_id}")
        
        # Completion date
        p.setFont("Helvetica", 12)
        p.setFillColor(self.COLORS['text'])
        completion_date = completion.completed_at.strftime("%d %B %Y")
        p.drawCentredString(self.width/2, self.height-350, f"Date of Completion: {completion_date}")
        
        # Certificate ID
        p.setFont("Helvetica", 10)
        p.setFillColor(HexColor('#666666'))
        p.drawCentredString(self.width/2, self.height-370, f"Certificate ID: {completion.id}")
        
        # Add QR code if provided
        if qr_code_path and os.path.exists(qr_code_path):
            try:
                p.drawImage(
                    qr_code_path,
                    self.width/2 - 50,
                    self.height - 500,
                    width=100,
                    height=100
                )
            except Exception as e:
                print(f"Error adding QR code: {e}")
        
        # Footer
        p.setFont("Helvetica", 9)
        p.setFillColor(HexColor('#999999'))
        p.drawCentredString(self.width/2, 40, self.template['footer'])
        
        p.save()
        buffer.seek(0)
        
        return buffer
    
    def save_certificate(self, buffer, cert_id):
        """Save certificate PDF to file"""
        certs_dir = os.path.join(settings.MEDIA_ROOT, 'certs')
        os.makedirs(certs_dir, exist_ok=True)
        
        cert_filename = f"cert_{cert_id}.pdf"
        cert_path = os.path.join(certs_dir, cert_filename)
        
        with open(cert_path, 'wb') as f:
            f.write(buffer.getvalue())
        
        return f'certs/{cert_filename}'


def create_certificate_for_completion(completion, template='standard', include_qr=True):
    """
    Helper function to create certificate for a VideoCompletion
    
    Args:
        completion: VideoCompletion object
        template: Certificate template name
        include_qr: Whether to include QR code
        
    Returns:
        Certificate path or None on error
    """
    try:
        generator = CertificateGenerator(
            completion.user,
            completion.video_id,
            template=template
        )
        
        # Generate QR code
        qr_path = None
        if include_qr:
            cert_url = f"https://yourdomain.com/certificate/{completion.id}/view/"
            qr_path = generator.generate_qr_code(cert_url, completion.id)
        
        # Create PDF
        pdf_buffer = generator.create_pdf(completion, qr_path)
        
        # Save to file
        cert_path = generator.save_certificate(pdf_buffer, completion.id)
        
        return cert_path
    
    except Exception as e:
        print(f"Error creating certificate: {str(e)}")
        return None


def get_user_completion_stats(user):
    """Get user's certificate completion statistics"""
    from courses.models import VideoCompletion
    
    completions = VideoCompletion.objects.filter(user=user)
    
    return {
        'total_videos': completions.count(),
        'total_certificates': completions.filter(certificate_path__isnull=False).count(),
        'recent_completion': completions.order_by('-completed_at').first(),
        'completion_dates': list(completions.values_list('completed_at', flat=True)),
    }


def export_certificates_batch(user, video_ids):
    """Generate multiple certificates for a user"""
    from courses.models import VideoCompletion
    import zipfile
    
    completions = VideoCompletion.objects.filter(
        user=user,
        video_id__in=video_ids
    )
    
    cert_files = []
    
    for completion in completions:
        if not completion.certificate_path:
            cert_path = create_certificate_for_completion(completion)
            if cert_path:
                completion.certificate_path = cert_path
                completion.save()
        
        if completion.certificate_path:
            full_path = os.path.join(settings.MEDIA_ROOT, str(completion.certificate_path))
            cert_files.append(full_path)
    
    # Create ZIP file
    if cert_files:
        zip_path = os.path.join(settings.MEDIA_ROOT, f'certs_batch_{user.id}.zip')
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for cert_file in cert_files:
                zipf.write(cert_file, arcname=os.path.basename(cert_file))
        return zip_path
    
    return None
