from django.db import models
class Product(models.Model):
	pno=models.IntegerField()
	pname=models.CharField(max_length=70)
	pquantity=models.IntegerField()
	pprice=models.IntegerField()

# Create your models here.
