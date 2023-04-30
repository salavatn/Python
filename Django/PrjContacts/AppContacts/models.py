from django.db import models


class Contacts(models.Model):
    FirstName   = models.CharField(max_length=50)
    LastName    = models.CharField(max_length=50)
    City        = models.CharField(max_length=50)
    Email       = models.EmailField()
    Birthday    = models.DateField()

    def __str__(self):
        return self.FirstName + ' ' + self.LastName
    