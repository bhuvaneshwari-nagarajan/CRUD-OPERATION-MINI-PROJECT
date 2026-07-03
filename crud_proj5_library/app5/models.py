from django.db import models

class Library(models.Model):
    sno = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=90)
    author_name = models.CharField(max_length=90)
    publisher = models.CharField(max_length=90)
    price = models.IntegerField()
    quantity = models.IntegerField()
    available_copies = models.IntegerField()
    language = models.CharField(max_length=50)
    shelf_no = models.CharField(max_length=20)
    issue_date = models.DateField()
    return_date = models.DateField()

# Create your models here.