from django.db import models

# Create your models here.

# Service Model
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ImageField(upload_to='services/', null=True, blank=True)

    def _str_(self):
        return self.title


# Portfolio Model
class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200, null=True, blank=True)  # optional link to project

    def _str_(self):
        return self.title




class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Testimonial from {self.name}"

# Blog Post Model
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/', null=True, blank=True)
    
    def _str_(self):
        return self.title