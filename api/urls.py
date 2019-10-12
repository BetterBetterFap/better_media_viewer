from django.urls import path
from . import views

urlpatterns = [
    path('media', views.MediaView.as_view()),
    path('media/<int:pk>', views.MediaView.as_view()),
]