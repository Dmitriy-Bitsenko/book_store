from django.contrib import admin
from .models import book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'cover_type')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price', 'publication_date')
    list_editable = ('price', 'cover_type')
    list_filter = ('cover_type',)


admin.site.register(book, BookAdmin)
