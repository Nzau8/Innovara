from django.urls import path
from . import views



urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('testimonials/',views.testimonials,name='testimonials'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('custom_website/',views.custom_website,name='custom_website'),
    path('web_maintenance/',views.web_maintenance,name='web_maintenance'),
    path('branding_identity/',views.branding_identity,name='branding_identity'),
    path('submit_testimonial/',views.submit_testimonial,name='submit_testimonial'),
]