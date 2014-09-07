from django.contrib import admin
from books.models import Publisher, Author, Book

#Allows customization of fields visable on admin "change list"
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')
class BookAdmin(admin.ModelAdmin):
    ist_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)

    
admin.site.register(Publisher)
# "Register the Author model with the AuthorAdmin options."
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

