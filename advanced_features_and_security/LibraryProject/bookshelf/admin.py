from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book
from bookshelf.models import CustomUser


# Register your models here.
class BookAdmin(admin.ModelAdmin):
  list_filter = ('title', 'author','publication_year')
  search_fields = ('title', 'author')


admin.site.register(Book, BookAdmin)



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)