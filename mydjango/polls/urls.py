from django.urls import path
from . import views

urlpatterns = [
    path('polls2/', views.welcome, name="welcome"),
    path('<int:question_id>/', views.detail, name="details"),
    path('<int:question_id>/results', views.result, name = "results"),
    path('<int:question_id>/vote', views.vote, name = "vote")

]