from django.db import models


class t_auto(models.Model):
    id      = models.AutoField(primary_key=True)
    brand   = models.CharField(max_length=50)
    model   = models.CharField(max_length=50)
    year    = models.IntegerField()
    color   = models.CharField(max_length=50)
    price   = models.IntegerField()
    engine  = models.CharField(max_length=50)
    vin     = models.CharField(max_length=50)
    status  = models.CharField(max_length=50, default='Available')

