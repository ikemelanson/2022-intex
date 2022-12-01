from datetime import datetime
from django.db import models

# Create your models here.

class Person(models.Model) :
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    age = models.IntegerField(default = 0)
    weight = models.IntegerField(default = 0)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    condition = models.IntegerField(default=0)
    # username = models.CharField(max_length=30)
    # password = models.CharField(max_length=30)

    def __str__(self):
        return (self.first_name)

class Meal(models.Model):
    description = models.CharField(max_length=20)

    def __str__(self):
        return (self.description)

# to do: possibly add default current date and time for the journal entry
class Journal_Entry(models.Model) :
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

# class Nutrient(models.Model):
#     nutrient_name = models.CharField(max_length=30)
#     nutrient_unit = models.CharField(max_length=30)

#     def __str__(self):
#         return (self.nutrient_name)

# class Food_Nutrient(models.Model):
#     food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
#     nutrient_id = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
#     food_nutrient_amount = models.DecimalField(max_digits=8, decimal_places=2)

#     def __str__(self):
#         return (str(self.food_nutrient_amount))


class Serum_Entry(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    serum_entry_date = models.DateField()
    serum_entry_time = models.TimeField()
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

# class Serum(models.Model):
#     serum_name = models.CharField(max_length=30)
#     serum_unit = models.CharField(max_length=30)

#     def __str__(self):
#         return (self.serum_name)

# class Serum_Measure(models.Model):
#     serum_entry_id = models.ForeignKey(Serum_Entry, on_delete=models.CASCADE)
#     serum_nutrient_id = models.ForeignKey(Serum, on_delete=models.CASCADE)
#     serum_measure_amount = models.DecimalField(max_digits=8, decimal_places=2)

#     def __str__(self):
#         return (str(self.serum_measure_amount))