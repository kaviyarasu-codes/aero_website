from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import ContactMessage, NewsletterSubscriber

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def partnership(request):
    return render(request, 'partnership.html')

def pricing(request):
    return render(request, 'pricing.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def faq(request):
    return render(request, 'faq.html')

def single_services(request):
    return render(request, 'single_services.html')


@csrf_exempt
def contact_form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not all([first_name, last_name, email, subject, message]):
            return JsonResponse({'success': False, 'error': 'All fields are required'})

        ContactMessage.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            subject=subject,
            message=message
        )

        # Send email (optional)
        send_mail(
            subject=f"New Contact: {subject}",
            message=f"From: {first_name} {last_name} <{email}>\n\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['info@aeroedgemedia.com'],
            fail_silently=True,
        )

        return JsonResponse({'success': True, 'message': 'Form submitted successfully!'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@csrf_exempt
def newsletter_subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            return JsonResponse({'success': False, 'error': 'Email is required'})

        if NewsletterSubscriber.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'error': 'Already subscribed'})

        NewsletterSubscriber.objects.create(email=email)
        return JsonResponse({'success': True, 'message': 'Subscribed successfully!'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})