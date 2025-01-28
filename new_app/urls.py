from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('edit-about/', views.edit_about, name='edit_about'),
    path('edit-project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('receive-message/', views.receive_message, name='receive_message'),
]
