from django.contrib import admin

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
	date_hierarchy = 'read_on'
	list_display = ('title', 'isbn', 'read_on')

admin.site.register(Book, BookAdmin)