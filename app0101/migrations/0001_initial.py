# Generated by Django 3.0.8 on 2020-07-14 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='new_shedule_class_model',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('faculty_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('fee', models.IntegerField()),
                ('durtion_days', models.IntegerField()),
            ],
        ),
    ]