from django.db import models

class new_shedule_class_model(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    fee = models.IntegerField()
    durtion_days =models.IntegerField()
