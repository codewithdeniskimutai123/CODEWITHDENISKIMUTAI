from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_img", blank=True, null=True)
    facebook = models.URLField(max_length=255, blank=True, null=True)
    youtube = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    twitter = models.URLField(max_length=255, blank=True, null=True)



    def __str__(self):
        return self.username
    
class Blog(models.Model):
    CATEGORY = (("Technology", "Technology"),
                ("Economy", "Economy"),
                ("Business", "Business"),
                ("Sports", "Sports"),
                ("Lifestyle", "Lifestyle")

    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="blogs", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(null=True, blank=True)
    is_draft = models.BooleanField(default=True)
    category = models.CharField(max_length=255, choices=CATEGORY, blank=True, null=True)
    featured_image = models.ImageField(upload_to="blog_img", blank=True, null=True)

    class Meta:
        ordering = ["-publish_date"]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while Blog.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug=f'{base_slug}-{num}' 
                num += 1
            self.slug = slug

        if not self.is_draft and self.publish_date is None:
            self.publish_date = timezone.now()

        super().save(*args, **kwargs)
            




