from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Resume(models.Model):
    personal_info = models.JSONField(blank=True, null=True, default=dict)
    summary = RichTextField(blank=True, null=True)
    education = models.JSONField(blank=True, null=True, default=list)
    skills = models.JSONField(blank=True, null=True, default=list)
    work_experience = models.JSONField(blank=True, null=True, default=list)
    projects = models.JSONField(blank=True, null=True, default=list)
    certifications = models.JSONField(blank=True, null=True, default=list)
    awards = models.JSONField(blank=True, null=True, default=list)
    languages = models.JSONField(blank=True, null=True, default=list)
    publications = models.JSONField(blank=True, null=True, default=list)
    interests = models.JSONField(blank=True, null=True, default=list)
    references = models.JSONField(blank=True, null=True, default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
