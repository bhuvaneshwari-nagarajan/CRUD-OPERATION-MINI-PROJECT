from django.contrib import admin
from app3.models import Product
class ProductAdmin(admin.ModelAdmin):
	list_display=['pno','pname','pquantity','pprice']
admin.site.register(Product,ProductAdmin)

# Register your models here.
