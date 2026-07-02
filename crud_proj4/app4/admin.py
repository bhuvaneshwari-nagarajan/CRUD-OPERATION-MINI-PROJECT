from django.contrib import admin
from app4.models import Banking
class BankingAdmin(admin.ModelAdmin):
	list_display=['account_no','name','deposit','balance']
admin.site.register(Banking,BankingAdmin)


# Register your models here.
