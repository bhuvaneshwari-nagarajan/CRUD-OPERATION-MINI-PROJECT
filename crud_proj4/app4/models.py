from django.db import models
class Banking(models.Model):
	account_no=models.IntegerField()
	name=models.CharField(max_length=70)
	deposit=models.IntegerField()
	balance=models.IntegerField()

# Create your models here.
