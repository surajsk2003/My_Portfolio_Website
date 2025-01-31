from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),  # Add this path to your new_app's urls.py file
    path('contact/', views.contact, name='contact'),
    path('receive-message/', views.receive_message, name='receive_message'),
]
