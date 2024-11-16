from django.shortcuts import render, redirect
from .forms import TestimonialForm
from .models import Testimonial

# Views to render static pages
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials.html', {'testimonials': testimonials})

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def custom_website(request):
    return render(request, 'custom_website.html')

def web_maintenance(request):
    return render(request, 'web_maintenance.html')

def branding_identity(request):
    return render(request, 'branding_identity.html')

# View for submitting testimonials
def submit_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()  # Save the testimonial
            return redirect('testimonials')  # Redirect to testimonials page or wherever you'd like
    else:
        form = TestimonialForm()
    
    return render(request, 'submit_testimonial.html', {'form': form})