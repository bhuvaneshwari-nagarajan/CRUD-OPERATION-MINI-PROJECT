from django.db import models
class Grocery(models.Model):
	name=models.CharField(max_length=65)
	quantity=models.IntegerField()
	price=models.FloatField()

# Create your models here.
