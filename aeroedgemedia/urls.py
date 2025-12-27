from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('partnership/', views.partnership, name='partnership'),
    path('pricing/', views.pricing, name='pricing'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('faq/', views.faq, name='faq'),
    path('single_services/', views.single_services, name='single_services'),
    path('contact/submit/', views.contact_form, name='contact_form'),
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
]