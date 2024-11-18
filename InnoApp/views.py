from django.shortcuts import render, redirect
from .forms import TestimonialForm
from .models import Testimonial
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BlogPost



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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_content = request.POST.get('message')
        
        # Compose email message
        subject = f"New message from {name}"
        message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_content}"
        recipient_list = ['nzau878@gmail.com']
        
        try:
            send_mail(subject, message, email, recipient_list)
            messages.success(request, 'Your message has been sent successfully.')
        except:
            messages.error(request, 'There was an error sending your message. Please try again.')

        return redirect('contact')  # Redirect to the same page to clear the form

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


def blog_list(request):
    # Check if there are any blog posts in the database
    blogs = BlogPost.objects.all().order_by('-published_date')

    # If no blog posts are found, pass an empty list or show a message
    if not blogs:
        return render(request, 'blog_list.html', {'message': 'No blog posts available. Please check back later.'})

    return render(request, 'blog_list.html', {'blogs': blogs})