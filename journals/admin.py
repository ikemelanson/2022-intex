from django.contrib import admin
from .models import Person, Journal_Entry, Meal, Food, Food_Journal, Serum_Entry

# Register your models here.
admin.site.register(Person)
admin.site.register(Journal_Entry)
admin.site.register(Meal)
admin.site.register(Food)
admin.site.register(Food_Journal)
admin.site.register(Serum_Entry)