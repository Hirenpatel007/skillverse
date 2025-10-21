# 🎓 SkillVerse - Complete Learning Platform

**Created by:** Hiren Patel  
**Version:** 2.0  
**Status:** ✅ Production Ready

---

## 🚀 Quick Start

```bash
cd skillverse
py manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

---

## ✨ Features

### 1. Video Library
- ✅ 109+ Real YouTube Videos
- ✅ Categories: Python, JavaScript, Java, C++, Web Dev, Data Science, Mobile
- ✅ Search & Filter (Site, YouTube, Google)
- ✅ Responsive Design

### 2. Certificate System
- ✅ Auto-generated PDF Certificates
- ✅ SkillVerse Logo
- ✅ Technology Logos (Python, Java, JS, SQL, Go, PHP, Node, Next.js, GitHub)
- ✅ Hiren Patel Signature
- ✅ QR Code Verification
- ✅ Certificate ID (SV-XXXXXX)

### 3. Upload & Sharing Platform
- ✅ Upload: PDFs, Images, Videos, Notes
- ✅ Public/Private Control
- ✅ Download Tracking
- ✅ Search & Filter
- ✅ Community Sharing

### 4. User Authentication
- ✅ Login/Register with Logo
- ✅ User Profiles
- ✅ Dashboard
- ✅ Progress Tracking

---

## 📁 Project Structure

```
skillverse/
├── courses/              # Main app
├── users/                # User management
├── jobs/                 # Job listings
├── payments/             # Subscriptions
├── recommender/          # AI recommendations
├── static/
│   └── images/
│       ├── skillverse.png       # Main logo
│       ├── signature.png        # Signature
│       └── tech-logos/          # Tech logos
├── media/
│   ├── certs/                   # Certificates
│   ├── qrcodes/                 # QR codes
│   └── uploads/                 # User uploads
└── manage.py
```

---

## 🎯 Key URLs

| Page | URL |
|------|-----|
| Home | http://127.0.0.1:8000/ |
| Login | http://127.0.0.1:8000/login/ |
| Register | http://127.0.0.1:8000/register/ |
| Videos | http://127.0.0.1:8000/free-videos/ |
| Upload | http://127.0.0.1:8000/upload/ |
| Sharing | http://127.0.0.1:8000/sharing/ |
| Certificates | http://127.0.0.1:8000/certificates/ |
| Admin | http://127.0.0.1:8000/admin/ |

---

## 🔧 Setup

### 1. Install Dependencies
```bash
pip install django djangorestframework django-cors-headers reportlab qrcode pillow
```

### 2. Run Migrations
```bash
py manage.py migrate
```

### 3. Create Superuser
```bash
py manage.py createsuperuser
```

### 4. Add Videos (Optional)
```bash
py add_50_real_videos.py
```

### 5. Start Server
```bash
py manage.py runserver
```

---

## 📊 Statistics

- **Total Videos:** 109+
- **Categories:** 7
- **Total Duration:** 200+ hours
- **File Types Supported:** 5 (PDF, Image, Video, Note, Other)
- **Technology Logos:** 9

---

## 🎨 Certificate Features

### Premium Design
- SkillVerse logo (top)
- Double-line border
- Student name (bold, centered)
- Technology logo (colored box)
- Video title
- Completion date
- Certificate ID (SV-XXXXXX)
- Hiren Patel signature
- "Founder & CEO, SkillVerse" title
- QR code verification
- Professional footer

### Technology Detection
Automatically detects and displays logo for:
- Python, Java, JavaScript, SQL, Go, PHP, Node.js, Next.js, GitHub

---

## 🔒 Security

- ✅ Login required for uploads
- ✅ CSRF protection
- ✅ User ownership verification
- ✅ File type validation
- ✅ Public/Private access control

---

## 📱 Responsive Design

- ✅ Desktop (4-column grid)
- ✅ Tablet (2-3 columns)
- ✅ Mobile (1 column)

---

## 🎓 Admin Panel

Access: **http://127.0.0.1:8000/admin/**

Manage:
- Users
- Videos
- Certificates
- Uploads
- Courses
- Jobs

---

## 🚀 Technology Stack

- **Backend:** Django 4.2.7
- **Database:** SQLite3
- **Frontend:** Bootstrap 5, Custom CSS
- **PDF Generation:** ReportLab
- **QR Codes:** qrcode + Pillow
- **Python:** 3.13

---

## 📝 Quick Commands

```bash
# Start server
py manage.py runserver

# Create superuser
py manage.py createsuperuser

# Run migrations
py manage.py migrate

# Collect static files
py manage.py collectstatic

# Check system
py manage.py check
```

---

## ✅ Features Checklist

- [x] Video library with 109+ videos
- [x] Search & filter (3 scopes)
- [x] Certificate generation
- [x] Technology logos on certificates
- [x] Upload system (PDFs, images, videos)
- [x] Sharing platform
- [x] User authentication
- [x] Responsive design
- [x] Admin panel
- [x] QR code verification

---

## 🎉 Success!

All features implemented and working:
- ✅ Centered search interface
- ✅ 109 real YouTube videos
- ✅ Premium certificates with logos
- ✅ Upload & sharing platform
- ✅ Secure authentication
- ✅ Professional branding

---

## 📞 Support

For issues or questions:
1. Check admin panel
2. Review code comments
3. Test in browser console (F12)

---

**Built by Hiren Patel**  
**SkillVerse - Learn • Grow • Excel** 🚀
