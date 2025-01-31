from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('receive-message/', views.receive_message, name='receive_message'),
]
