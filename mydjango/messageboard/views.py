from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import MessageBoard
def display_post(request):
    #return HttpResponse("My first post")
    messages = MessageBoard.objects.all()
    return render(request, 'messageboard/mb.html',{'msg_list':messages})

def add_post(request):
    msg = request.POST['message_txt']
    print(msg)
    new_posted_msg = MessageBoard(posted_msg = msg)
    new_posted_msg.save()
    return HttpResponseRedirect('/mb/getall')