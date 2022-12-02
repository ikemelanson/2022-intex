from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class PersonForm(forms.ModelForm) :
    class Meta :
        model = Person
        fields = '__all__'

class Journal_Entry_Form(forms.ModelForm) :
    class Meta :
        model = Journal_Entry
        fields = ['person_id', 'journal_date', 'journal_time', 'meal_id']

class AccountRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', ]
        
class Serum_Entry_Form(forms.ModelForm):
    class Meta:
        model = Serum_Entry
        fields = '__all__'

class Food_Journal_Form(forms.ModelForm) :
    class Meta :
        model = Food_Journal
        fields = '__all__'

class Food_Form(forms.ModelForm) :
    class Meta :
        model = Food
        fields = ['food_name', 'g_protein', 'mg_phosphorus', 'mg_potassium', 'mg_sodium']
