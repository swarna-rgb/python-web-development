from django.urls import path
from . import views

urlpatterns = [
    path('getTodo/',views.todo_view, name='todo_view'),
    path('addTodo/',views.add_todo_item,name='add_item'),
    path('deleteTodo/<int:todo_id>/', views.delete_todo_item, name='delete_item')
]