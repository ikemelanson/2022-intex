from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from .forms import PersonForm

def indexPageView(request):
    return render(request, 'healthtracker/index.html' )

def registerPageView(request) :
    data = Person.objects.all()
    if request.method == 'POST' :
        form = PersonForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('/')
    else :
        form = PersonForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'healthtracker/register.html', context) 