from django.contrib import admin
from tp_book.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['name','author',  'get_description','fav','created_at']
    list_display_links = ['name','author',  'get_description','fav','created_at']
    search_fields = ['name','author',  'get_description',]
    list_filter = ['fav','created_at']
    list_per_page = 10


admin.site.register(Book, BookAdmin)


