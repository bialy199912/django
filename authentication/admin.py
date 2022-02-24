from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email', 'is_staff')
    list_per_page = 10   # ile rekordów na stronie ma sie wyswietlac w panelu admina

admin.site.register(User, UserAdmin)
