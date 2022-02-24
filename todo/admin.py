from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'discription', 'is_completed')
    search_fields = ('title', 'discription', 'is_completed')
    list_per_page = 10   # ile rekordów na stronie ma sie wyswietlac w panelu admina


admin.site.register(Todo, TodoAdmin)
