from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=50)
    publication_date = models.DateField()
    price = models.PositiveIntegerField()
    page = models.PositiveIntegerField()







