from django.urls import path
from . import views

urlpatterns = [
        path('getall/',views.display_post),
        path('addmsg/',views.add_post)
]