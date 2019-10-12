from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('media/', views.media, name='random_media'),
    path('media/<int:file_id>/', views.media, name='media'),
]