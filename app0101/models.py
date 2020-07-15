from django.db import models

class new_shedule_class_model(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    fee = models.IntegerField()
    durtion_days = models.IntegerField()
    def __str__(self):
        return self.name


class user_register(models.Model):
    Idno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Contact_No = models.IntegerField(unique=True)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=50)
