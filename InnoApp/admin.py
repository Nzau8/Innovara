from django.contrib import admin
from .models import Service, PortfolioItem, BlogPost, Testimonial

# Register your models here.
admin.site.register(Service)
admin.site.register(PortfolioItem)
admin.site.register(BlogPost)
admin.site.register(Testimonial)