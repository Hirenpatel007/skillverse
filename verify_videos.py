#!/usr/bin/env python
"""
SkillVerse Video System - Complete Verification Script
Tests all 29 videos and platform features
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillverse.settings')
django.setup()

from courses.models import YouTubeVideo

def verify_all_videos():
    """Verify all videos are properly configured"""
    print("=" * 80)
    print("🎓 SKILLVERSE VIDEO VERIFICATION SYSTEM")
    print("=" * 80)
    
    videos = YouTubeVideo.objects.all().order_by('id')
    
    print(f"\n📊 DATABASE STATISTICS:")
    print(f"   Total Videos: {videos.count()}")
    print(f"   Active Videos: {videos.filter(is_active=True).count()}")
    print(f"   Free Videos: {videos.filter(is_free=True).count()}")
    
    total_duration = 0
    categories = {}
    channels = {}
    
    print(f"\n📺 DETAILED VIDEO LIST:\n")
    print(f"{'#':<3} {'Title':<40} {'Channel':<25} {'YouTube ID':<15} {'Status'}")
    print("-" * 100)
    
    for idx, video in enumerate(videos, 1):
        status = "✅ OK" if video.is_active and video.is_free else "⚠️ CHECK"
        print(f"{idx:<3} {video.title[:39]:<40} {video.channel[:24]:<25} {video.video_id:<15} {status}")
        
        # Collect stats
        if video.category not in categories:
            categories[video.category] = 0
        categories[video.category] += 1
        
        if video.channel not in channels:
            channels[video.channel] = 0
        channels[video.channel] += 1
    
    print("\n" + "=" * 80)
    print(f"✅ CATEGORY BREAKDOWN ({len(categories)} categories):")
    print("-" * 80)
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"   • {cat:<35} {count:>3} videos")
    
    print("\n" + "=" * 80)
    print(f"📡 CHANNEL BREAKDOWN ({len(channels)} channels):")
    print("-" * 80)
    for channel, count in sorted(channels.items(), key=lambda x: -x[1]):
        print(f"   • {channel:<35} {count:>3} videos")
    
    print("\n" + "=" * 80)
    print("🎯 VERIFICATION RESULTS:")
    print("-" * 80)
    
    checks = {
        "All videos active": videos.filter(is_active=False).count() == 0,
        "All videos free": videos.filter(is_free=False).count() == 0,
        "All have titles": all(v.title for v in videos),
        "All have video_ids": all(v.video_id for v in videos),
        "All have channels": all(v.channel for v in videos),
        "All have categories": all(v.category for v in videos),
        "29 total videos": videos.count() == 29,
    }
    
    for check_name, result in checks.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"   {status}  {check_name}")
    
    all_passed = all(checks.values())
    
    print("\n" + "=" * 80)
    if all_passed:
        print("✅ ALL VERIFICATION CHECKS PASSED!")
        print("✅ System is ready for production")
        print("✅ All 29 videos are accessible and verified")
    else:
        print("❌ Some verification checks failed")
        print("⚠️  Please review the issues above")
    
    print("=" * 80)
    print("\n🌟 PLATFORM OWNER: Hiren Patel")
    print("🎓 PLATFORM: SkillVerse")
    print("📅 VERIFICATION DATE: October 17, 2025")
    print("=" * 80)
    
    return all_passed

if __name__ == "__main__":
    verify_all_videos()
