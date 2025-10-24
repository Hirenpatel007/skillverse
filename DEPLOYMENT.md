# 🚀 SkillVerse - Render Deployment Guide

## 📋 Prerequisites

1. GitHub account
2. Render account (https://render.com)
3. Git installed locally

---

## 📁 Files Created for Deployment

✅ `requirements.txt` - Python dependencies
✅ `build.sh` - Build script
✅ `render.yaml` - Render configuration
✅ `runtime.txt` - Python version
✅ `.env.example` - Environment variables template
✅ Updated `settings.py` - Production settings

---

## 🔧 Step 1: Prepare Repository

### 1.1 Initialize Git (if not already)
```bash
cd skillverse
git init
git add .
git commit -m "Initial commit - SkillVerse platform"
```

### 1.2 Create GitHub Repository
1. Go to https://github.com/new
2. Name: `skillverse`
3. Don't initialize with README
4. Click "Create repository"

### 1.3 Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/skillverse.git
git branch -M main
git push -u origin main
```

---

## 🌐 Step 2: Deploy on Render

### 2.1 Create New Web Service
1. Go to https://dashboard.render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Select `skillverse` repository

### 2.2 Configure Service
```
Name: skillverse
Environment: Python 3
Region: Choose closest to you
Branch: main
Build Command: ./build.sh
Start Command: gunicorn skillverse.wsgi:application
```

### 2.3 Add Environment Variables
Click "Advanced" → "Add Environment Variable":

```
SECRET_KEY = (click "Generate" for random key)
DEBUG = False
ALLOWED_HOSTS = .onrender.com
PYTHON_VERSION = 3.11.0
```

### 2.4 Create PostgreSQL Database
1. Click "New +" → "PostgreSQL"
2. Name: `skillverse-db`
3. Database: `skillverse`
4. User: `skillverse`
5. Region: Same as web service
6. Click "Create Database"

### 2.5 Link Database to Web Service
1. Go back to your web service
2. Environment → Add Environment Variable
3. Key: `DATABASE_URL`
4. Value: Copy from PostgreSQL "Internal Database URL"

### 2.6 Deploy
1. Click "Create Web Service"
2. Wait for deployment (5-10 minutes)
3. Your app will be live at: `https://skillverse.onrender.com`

---

## 🔐 Step 3: Post-Deployment Setup

### 3.1 Create Superuser
1. Go to Render Dashboard → Your Service
2. Click "Shell" tab
3. Run:
```bash
python manage.py createsuperuser
```

### 3.2 Add Videos
```bash
python add_50_real_videos.py
```

### 3.3 Test Your Site
Visit: `https://skillverse.onrender.com`

---

## 📊 Environment Variables Reference

| Variable | Value | Description |
|----------|-------|-------------|
| SECRET_KEY | (generated) | Django secret key |
| DEBUG | False | Production mode |
| ALLOWED_HOSTS | .onrender.com | Allowed domains |
| DATABASE_URL | (from Render) | PostgreSQL connection |
| PYTHON_VERSION | 3.11.0 | Python version |

---

## 🔄 Updating Your Deployment

### Push Changes
```bash
git add .
git commit -m "Update description"
git push origin main
```

Render will automatically redeploy!

---

## 📁 Static Files

Static files are handled by WhiteNoise:
- Automatically collected during build
- Compressed and cached
- Served efficiently

---

## 💾 Database

PostgreSQL database includes:
- Automatic backups
- Connection pooling
- SSL encryption

---

## 🎯 URLs After Deployment

```
Home: https://skillverse.onrender.com/
Admin: https://skillverse.onrender.com/admin/
Videos: https://skillverse.onrender.com/free-videos/
Login: https://skillverse.onrender.com/login/
```

---

## 🐛 Troubleshooting

### Build Fails
- Check `build.sh` has execute permissions
- Verify all dependencies in `requirements.txt`
- Check Python version in `runtime.txt`

### Database Connection Error
- Verify DATABASE_URL is set correctly
- Check PostgreSQL database is running
- Ensure database is in same region

### Static Files Not Loading
- Run: `python manage.py collectstatic`
- Check STATIC_ROOT in settings.py
- Verify WhiteNoise is in MIDDLEWARE

### 500 Error
- Set DEBUG=True temporarily to see error
- Check Render logs
- Verify all environment variables

---

## 📝 Render Dashboard

Access logs and metrics:
1. Go to https://dashboard.render.com
2. Click your service
3. View:
   - Logs
   - Metrics
   - Events
   - Settings

---

## 💰 Pricing

**Free Tier:**
- Web Service: Free (spins down after inactivity)
- PostgreSQL: Free (90 days, then $7/month)

**Paid Tier:**
- Web Service: $7/month (always on)
- PostgreSQL: $7/month

---

## ✅ Deployment Checklist

- [ ] Git repository created
- [ ] Pushed to GitHub
- [ ] Render account created
- [ ] Web service configured
- [ ] PostgreSQL database created
- [ ] Environment variables set
- [ ] Service deployed successfully
- [ ] Superuser created
- [ ] Videos added
- [ ] Site tested

---

## 🎉 Success!

Your SkillVerse platform is now live!

**Share your link:**
`https://skillverse.onrender.com`

---

## 📞 Support

- Render Docs: https://render.com/docs
- Django Docs: https://docs.djangoproject.com
- GitHub Issues: Create issue in your repo

---

**Built by Hiren Patel**  
**SkillVerse - Learn • Grow • Excel** 🚀
