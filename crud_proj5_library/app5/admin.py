from django.contrib import admin
from app5.models import Library

class LibraryAdmin(admin.ModelAdmin):
    list_display = [
        'sno',
        'book_name',
        'author_name',
        'publisher',
        'price',
        'quantity',
        'available_copies',
        'language',
        'shelf_no',
        'issue_date',
        'return_date',
    ]

admin.site.register(Library, LibraryAdmin)