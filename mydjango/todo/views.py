from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import ToDoItem

def todo_view(request):
    #return HttpResponse('Hi, this is todo view')
        all_todo_items = ToDoItem.objects.all()
        return render(request,'todo/todo.html', {'all_items': all_todo_items})

def add_todo_item(request):
    #return HttpResponse(request.POST['todoitem'] + " added")
    todoitemtobeadded = request.POST['todoitem']
    newitem = ToDoItem(todoitem = todoitemtobeadded)
    newitem.save()
    return HttpResponseRedirect('/todo/getTodo/')

def delete_todo_item(request,todo_id):
    itemtobedeleted = ToDoItem.objects.get(id=todo_id)
    itemtobedeleted.delete()
    #itemtobedeleted.save()
    return HttpResponseRedirect('/todo/getTodo/')

