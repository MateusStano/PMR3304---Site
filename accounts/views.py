from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from albuns.forms import BasicUserCreationForm, ClinicaCreationForm       

def signupclinica(request):
    if request.method == 'POST':
        form = ClinicaCreationForm(request.POST)
        if form.is_valid():
            user = form.save()                                
            user_group = Group.objects.get(name='clinicas') 
            user.groups.add(user_group)                       

            return HttpResponseRedirect(reverse('login'))
    else:
        form = ClinicaCreationForm()

    context = {'form': form}
    return render(request, 'accounts/signup-clinica.html', context)

def signupuser(request):
    if request.method == 'POST':
        form = BasicUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()                                
            user_group = Group.objects.get(name='basic_user') 
            user.groups.add(user_group)                       

            return HttpResponseRedirect(reverse('login'))
    else:
        form = BasicUserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/signup-user.html', context)
