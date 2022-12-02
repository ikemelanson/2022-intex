from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import requests

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
    # person_data.username
    meal_data = Meal.objects.all()
    food_data = Food.objects.all()

    if request.method == 'POST' :
        Dashboard_form = Journal_Entry_Form(request.POST)
        serum_form = Serum_Entry_Form(request.POST)
        Person_form = PersonForm(request.POST)
        Food_journal_form = Food_Journal_Form(request.POST)
        Food_form = Food_Form(request.POST)

        if Dashboard_form.is_valid() :
            Dashboard_form.save()
            return redirect('dashboard')
        if serum_form.is_valid() :
            serum_form.save()
            return redirect('dashboard')

        if Food_journal_form.is_valid() :
            Food_journal_form.save()
            return redirect('dashboard')

        if Food_form.is_valid() :
            Food_form.save()
            return redirect('dashboard')
    else :
        Dashboard_form = Journal_Entry_Form()
        serum_form = Serum_Entry_Form()
        Person_form = PersonForm()
        Food_journal_form = Food_Journal_Form()
        Food_form = Food_Form()
    
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
        'food_data': food_data,
        'Food_form': Food_form
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
        # person.username = request.POST['username']

        person.save()
        return redirect('dashboard')

def submitmeal(request):
    if request.method == "POST":
        journalentry = Journal_Entry()
        

        journalentry.person_id = request.POST['person_id']
        journalentry.journal_date = request.POST['journal_date']
        journalentry.journal_time = request.POST['journal_time']
        journalentry.meal_id = request.POST['meal_id']

        journalentry.save()

        return dashboardPageView(request, request.POST['username'])

def newFoodPageView(request):
    return render(request, 'healthtracker/newFood.html')

def searchFoodPageView(request):

    query = request.POST['searchParameter']
    query  = query.lower()

    foodItem = {
        "status": 0,
        "name": query,
        "nutrients" : {
            "n" : 0.0,
            "a" : 0.0,
            "P" : 0.0,
            "K" : 0.0
        }
    }

    URL1 = "https://api.nal.usda.gov/fdc/v1/foods/search"
    PARAMS1 = {
        'api_key' : 't71OoedERi0Xneuuyblf1ECkNzqwBtNXf9Mgp3yp',
        'query': query,
    }

    r1 = requests.get(url = URL1, params= PARAMS1)
    data1 = r1.json()

    if data1['totalHits'] > 0:

        fdcID = str(data1['foods'][0]['fdcId'])

        URL2 = 'https://api.nal.usda.gov/fdc/v1/food/' 
        URL2 += fdcID
        URL2 += "?format=abridged&nutrients=305&nutrients=307&nutrients=203&nutrients=306&api_key=t71OoedERi0Xneuuyblf1ECkNzqwBtNXf9Mgp3yp"

        r2 = requests.get(url = URL2)
        data2 = r2.json()
        print(data2)

        if query in ((data2['description']).lower()):
            foodItem['name'] = (data2['description'])
            foodItem['status'] = 2
            nutrients = data2['foodNutrients']
            for count in range(0, len(nutrients)):
                name = nutrients[count]['name'] 
                amount = nutrients[count]['amount']
                foodItem['nutrients'][name[len(name) - 1]] = amount

        else:
            # be more specific
            foodItem['status'] = 1
            foodItem['name'] = query
            print("Query successful but no items match your search")

    else:
        # add the food yourself
        print("Query unsuccesful")

    print(foodItem)

    return render(request, 'healthtracker/addFood.html', foodItem)

def commitFood(request):
    if request.method == "POST":

        food = Food()

        food.food_name = request.POST['food_name']
        food.g_protein = request.POST['g_protein']
        food.mg_phosphorus = request.POST['mg_phosphorus']
        food.mg_potassium = request.POST['mg_potassium']
        food.mg_sodium = request.POST['mg_sodium']

        food.save()

        return redirect("newFood")

def commitSerum(request):
    if request.method == "POST":

        serum = Serum_Entry.objects.get(id = request.POST['serum_id'])

        serum.serum_entry_date = request.POST['serum_entry_date']
        serum.serum_entry_time = request.POST['serum_entry_time']
        serum.meql_sodium = request.POST['meql_sodium']
        serum.mgdl_potassium = request.POST['mgdl_potassium']
        serum.mgdl_phosphorus = request.POST['mgdl_phosphorus']
        serum.mgdl_creatinine = request.POST['mgdl_creatinine']
        serum.mgdl_albumin = request.POST['mgdl_albumin']
        serum.mgdl_blood_sugar = request.POST['mgdl_blood_sugar']

        serum.save()

        return redirect("viewSerums")

def commitPerson(request):
    if request.method == "POST":

        person = Person.objects.get(person_id = request.POST['person_id'])

        person.first_name = request.POST['first_name']
        person.last_name = request.POST['last_name']
        person.age = request.POST['age']
        person.height = request.POST['height']
        person.weight = request.POST['weight']
        person.condition = request.POST['condition']
        person.gender = request.POST['gender']

        person.save()

        return redirect("viewPeople")

def commitJournal(request):
    if request.method == "POST":

        journal = Journal_Entry.objects.get(journal_id = request.POST['journal_id'])

        journal.journal_date = request.POST['journal_date']
        journal.journal_time = request.POST['journal_time']

        journal.save()

        return redirect("dashboard")

def delSerum(request):

    serum = Serum_Entry.objects.get(id = request.POST['serum_id'])
    serum.delete()

    return redirect("viewSerums")

def delJournal(request):

    journal = Journal_Entry.objects.get(journal_id = request.POST['journal_id'])
    journal.delete()

    return redirect("dashboard")

def delPerson(request):

    person = Person.objects.get(person_id = request.POST['person_id'])
    person.delete()

    return redirect("viewPeople")

def viewSerums(request):

    serum_data = Serum_Entry.objects.all()

    context = {
        "serum_data" : serum_data
    }

    return render(request, "healthtracker/viewSerums.html", context)


def viewPeople(request):

    people_data = Person.objects.all()

    context = {
        "people_data" : people_data
    }

    return render(request, "healthtracker/viewPeople.html", context)


def editSerum(request):
    serumEntry = Serum_Entry.objects.get(id = request.POST['serum_id'])

    serumEntry.serum_entry_date = serumEntry.serum_entry_date.strftime('%Y-%m-%d')
    serumEntry.serum_entry_time = serumEntry.serum_entry_time.strftime('%H:%M:%S')

    context = {
        'serum_entry' : serumEntry
    }

    return render(request, "healthtracker/editSerum.html", context)

def editPerson(request):
    person = Person.objects.get(person_id = request.POST['person_id'])

    context = {
        'person' : person
    }

    return render(request, "healthtracker/editPerson.html", context)


def editJournal(request):
    journal = Journal_Entry.objects.get(journal_id = request.POST['journal_id'])

    journal.journal_date = journal.journal_date.strftime('%Y-%m-%d')
    journal.journal_time = journal.journal_time.strftime('%H:%M:%S')

    context = {
        'journal' : journal
    }

    return render(request, "healthtracker/editJournal.html", context)


# def dashboardUsernamePageView(request,username):
#     if request.method == "POST":
#         person = Person()
#         person.frist

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
