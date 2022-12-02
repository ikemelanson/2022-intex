from datetime import datetime
from django.db import models

# Create your models here.

class Person(models.Model) :
    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    age = models.IntegerField(default = 0)
    weight = models.IntegerField(default = 0)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    condition = models.IntegerField(default=0)
    gender = models.CharField(max_length=10)
    username = models.CharField(max_length=50)

    def __str__(self):
        return (self.first_name)

class Meal(models.Model):
    meal_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=20)

    def __str__(self):
        return (self.description)

class Journal_Entry(models.Model) :
    journal_id = models.AutoField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    journal_date = models.DateField(default=datetime.today)
    journal_time = models.TimeField(default=datetime.today)
    meal_id = models.ForeignKey(Meal, on_delete=models.DO_NOTHING)

    def __str__(self):
        return (self.full_date_time)

    @property
    def full_date_time(self):
        return '%s %s' % (self.journal_date, self.journal_time)


class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=30)
    g_protein = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    mg_phosphorus = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    mg_potassium = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    mg_sodium = models.DecimalField(max_digits=5, decimal_places=1, default=0)

    def __str__(self):
        return (self.food_name)

class Food_Journal(models.Model):
    journal_id = models.ForeignKey(Journal_Entry, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    servings = models.IntegerField(default= 0)

    def __str__(self):
        return (str(self.servings))

class Serum_Entry(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    serum_entry_date = models.DateField(default=datetime.today)
    serum_entry_time = models.TimeField(default=datetime.today)
    meql_sodium = models.DecimalField(max_digits=4, decimal_places=1)
    mgdl_potassium = models.DecimalField(max_digits=2, decimal_places=1)
    mgdl_phosphorus = models.DecimalField(max_digits=2, decimal_places=1)
    mgdl_creatinine = models.DecimalField(max_digits=2, decimal_places=1)
    mgdl_albumin = models.DecimalField(max_digits=2, decimal_places=1)
    mgdl_blood_sugar = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return (self.full_date_time)

    @property
    def full_date_time(self):
        return '%s %s' % (self.serum_entry_date, self.serum_entry_time)