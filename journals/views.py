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
        Person_form = PersonForm(request.POST)
        if Person_form.is_valid() :
            Person_form.save()
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('dashboard')
    else :
        Person_form = PersonForm()
    context = {
        'data': data,
        'Person_form': Person_form,
    }
    return render(request, 'healthtracker/register.html', context) 

def accountRegisterView(request):
    if request.method == 'POST' :
        Register_form = UserCreationForm(request.POST)
        if Register_form.is_valid() :
            Register_form.save()
            username = Register_form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('/')
    else :
        Register_form = UserCreationForm()
    context = {
        'Register_form': Register_form,
    }
    return render(request, 'healthtracker/accountregister.html', context) 


def dashboardPageView(request) :
    person_data = Person.objects.all()
    data = Journal_Entry.objects.all()
    serum_data = Serum_Entry.objects.all()
    food_journal_data = Food_Journal.objects.all()
    meal_data = Meal.objects.all()

    if request.method == 'POST' :
        Dashboard_form = Journal_Entry_Form(request.POST)
        serum_form = Serum_Entry_Form(request.POST)
        Person_form = PersonForm(request.POST)
        Food_journal_form = Food_Journal_Form(request.POST)

        # if Person_form.is_valid():
        #     Person_form.save()
        #     return redirect('dashboard')

        if Dashboard_form.is_valid() :
            Dashboard_form.save()
            return redirect('dashboard')
        if serum_form.is_valid() :
            serum_form.save()
            return redirect('dashboard')

        if Food_journal_form.is_valid() :
            Food_journal_form.save()
            return redirect('dashboard')
    else :
        Dashboard_form = Journal_Entry_Form()
        serum_form = Serum_Entry_Form()
        Person_form = PersonForm()
        Food_journal_form = Food_Journal_Form()

    context = {
        'person_form': Person_form,
        'person_data': person_data,
        'serum_data': serum_data,
        'serum_form': serum_form,
        'data': data,
        'Dashboard_form': Dashboard_form,
        'food_journal_data': food_journal_data,
        'Food_journal_form': Food_journal_form,
        'meal_data': meal_data,
    }
    return render(request, 'healthtracker/dashboard.html', context) 

def profilePageView(request):
    return render(request, 'healthtracker/profile.html') 

def submituser(request):
    if request.method == "POST":
        person = Person()

        person.first_name = request.POST['first_name']
        person.last_name = request.POST['last_name']
        person.age = request.POST['age']
        person.gender = request.POST['gender']
        person.weight = request.POST['weight']
        person.height = request.POST['height']
        person.condition = request.POST['condition']
        person.username = request.POST['username']

        person.save()

        return dashboardPageView(request)



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
