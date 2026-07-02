from django.contrib import admin
from app2.models import Grocery
class GroceryAdmin(admin.ModelAdmin):
	list_display=['name','quantity','price']
admin.site.register(Grocery,GroceryAdmin)

# Register your models here.


# Register your models here.
