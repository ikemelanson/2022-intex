from django import forms
from .models import *

class PersonForm(forms.ModelForm) :
    class Meta :
        model = Person
        fields = '__all__'

class Journal_Entry_Form(forms.ModelForm) :
    class Meta :
        model = Journal_Entry
        fields = '__all__'

class Serum_Entry_Form(forms.ModelForm):
    class Meta:
        model = Serum_Measure
        fields = '__all__'