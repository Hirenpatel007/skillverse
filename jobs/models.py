from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    skills_required = models.TextField(help_text='Comma-separated skills')
    job_type = models.CharField(max_length=50)
    salary_range = models.CharField(max_length=100, blank=True)
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
