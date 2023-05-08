from django.db import models


class t_automobiles(models.Model):
    id      = models.AutoField(primary_key=True)
    brand   = models.CharField(max_length=50)
    model   = models.CharField(max_length=50)
    year    = models.IntegerField()
    color   = models.CharField(max_length=50)
    price   = models.IntegerField()
    engine  = models.CharField(max_length=50)
    vin     = models.CharField(max_length=50)
    status  = models.CharField(max_length=50, default='Available')


# Создать таблицу Студенты:
class TableStudents(models.Model):
    id      = models.AutoField(primary_key=True)
    Name    = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Age     = models.IntegerField()
    Group   = models.CharField(max_length=50)
    Course  = models.IntegerField()
    Faculty = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    Phone   = models.CharField(max_length=50)
    Email   = models.CharField(max_length=50)