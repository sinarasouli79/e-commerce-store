from pyexpat import model
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    inventory = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    last_update = models.DateTimeField(auto_now=True)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)