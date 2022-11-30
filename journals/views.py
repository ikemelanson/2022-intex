from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def indexPageView(request):
    return render(request, 'healthtracker/index.html' )

def registerPageView(request) :
    data = Person.objects.all()
    if request.method == 'POST' :
        form = PersonForm(request.POST)
        if form.is_valid() :
            form.save()
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('/')
    else :
        form = PersonForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'healthtracker/register.html', context) 

def accountRegisterView(request):
    if request.method == 'POST' :
        form = AccountRegister(request.POST)
        if form.is_valid() :
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('/')
    else :
        form = AccountRegister()
    context = {
        'form': form,
    }
    return render(request, 'healthtracker/accountregister.html', context) 


def dashboardPageView(request) :
    data = Journal_Entry.objects.all()
    serum_data = Serum_Measure.objects.all()
    if request.method == 'POST' :
        form = Journal_Entry_Form(request.POST)
        serum_form = Serum_Entry_Form(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('/')
    else :
        form = Journal_Entry_Form()
        serum_form = Serum_Entry_Form
    context = {
        'serum_data': serum_data,
        'serum_form': serum_form,
        'data': data,
        'form': form,
    }
    return render(request, 'healthtracker/dashboard.html', context) 

def profilePageView(request):
    return render(request, 'healthtracker/profile.html') 
# def serumDashboardPageView(request) :
#     data = Serum_Measure.objects.all()
#     if request.method == 'POST':
#         form = Serum_Entry_Form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = Serum_Entry_Form()
#     context = {
#         'entry': data,
#         'form' : form,
#     }
#     return render(request, 'healthtracker/dashboard.html', context)
