# Generated by Django 4.1.2 on 2022-11-30 21:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=30)),
                ('food_unit', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('height', models.DecimalField(decimal_places=2, max_digits=4)),
                ('condition', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Serum_Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serum_entry_date', models.DateField()),
                ('serum_entry_time', models.TimeField()),
                ('meql_sodium', models.DecimalField(decimal_places=1, max_digits=4)),
                ('mgdl_potassium', models.DecimalField(decimal_places=1, max_digits=2)),
                ('mgdl_phosphorus', models.DecimalField(decimal_places=1, max_digits=2)),
                ('mgdl_creatinine', models.DecimalField(decimal_places=1, max_digits=2)),
                ('mgdl_albumin', models.DecimalField(decimal_places=1, max_digits=2)),
                ('mgdl_blood_sugar', models.DecimalField(decimal_places=1, max_digits=4)),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journals.person')),
            ],
        ),
        migrations.CreateModel(
            name='Journal_Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_date', models.DateField(default=datetime.datetime.today)),
                ('journal_time', models.TimeField(default=datetime.datetime.today)),
                ('meal_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='journals.meal')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journals.person')),
            ],
        ),
        migrations.CreateModel(
            name='Food_Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_protein', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('mg_phosphorus', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('mg_potassium', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('mg_sodium', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journals.food')),
                ('journal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journals.journal_entry')),
            ],
        ),
    ]
