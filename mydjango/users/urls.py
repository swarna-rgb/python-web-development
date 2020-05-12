from . import views
from django.urls import path, include

urlpatterns = [
    path('register/',views.user_registration, name = 'register')
]