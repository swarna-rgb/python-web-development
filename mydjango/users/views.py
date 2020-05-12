from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import  messages
# Create your views here.
def user_registration(request):
    form = UserCreationForm()
    return render(request,'users/registration.html', {'form':form})
    """if request.method == "POST":
       form = UserCreationForm(request.POST)
      if form.is_valid():
           username =  form.cleaned_data.get('username')
           messages.success(request, f'Account has been created for {username} !')
           return redirect('')
       else:
           form = UserCreationForm()
       return render(request, 'users/registration.html', {'form': form})"""


